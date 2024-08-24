
#! /bin/bash
# By Spransy, Derek" <DSPRANS () emory ! edu> and Charlie Scott
# Modified by Cyb3rhq, Inc. <info@wazuh.com>.
# This program is a free software; you can redistribute it and/or modify it under the terms of GPLv2

#####
# This checks for an error and exits with a custom message
# Returns zero on success
# $1 is the message
# $2 is the error code

DIR="/Library/Ossec"

function check_errm
{
    if  [[ ${?} != "0" ]]
        then
        echo "${1}";
        exit ${2};
        fi
}

if [ -d "${DIR}" ]; then
    echo "A Cyb3rhq agent installation was found in ${DIR}. Will perform an upgrade."
    upgrade="true"
    touch "${DIR}/CYB3RHQ_PKG_UPGRADE"

    if [ -f "${DIR}/CYB3RHQ_RESTART" ]; then
        rm -f "${DIR}/CYB3RHQ_RESTART"
    fi

    # Stops the agent before upgrading it

    echo "Backing up configuration files to ${DIR}/config_files/"
    mkdir -p ${DIR}/config_files/
    cp -r ${DIR}/etc/{ossec.conf,client.keys,local_internal_options.conf,shared} ${DIR}/config_files/

    if [ -d ${DIR}/logs/ossec ]; then
        echo "Renaming ${DIR}/logs/ossec to ${DIR}/logs/cyb3rhq"
        mv ${DIR}/logs/ossec ${DIR}/logs/cyb3rhq
    fi

    if [ -d ${DIR}/queue/ossec ]; then
        echo "Renaming ${DIR}/queue/ossec to ${DIR}/queue/sockets"
        mv ${DIR}/queue/ossec ${DIR}/queue/sockets
    fi

    if pkgutil --pkgs | grep -i cyb3rhq-agent-etc > /dev/null 2>&1 ; then
        echo "Removing previous package receipt for cyb3rhq-agent-etc"
        pkgutil --forget com.cyb3rhq.pkg.cyb3rhq-agent-etc
    fi
fi

DSCL="/usr/bin/dscl";
if [[ ! -f "$DSCL" ]]
    then
    echo "Error: I couldn't find dscl, dying here";
    exit
fi


# get unique id numbers (uid, gid) that are greater than 100
echo "Getting unique id numbers (uid, gid)"
unset -v i new_uid new_gid idvar;
declare -i new_uid=0 new_gid=0 i=100 idvar=0;
while [[ $idvar -eq 0 ]]; do
    i=$[i+1]
    if [[ -z "$(${DSCL} . -search /Users uid ${i})" ]] && [[ -z "$(${DSCL} . -search /Groups gid ${i})" ]];
        then
        echo "Found available UID and GID: $i"
        new_uid=$i
        new_gid=$i
        idvar=1
   fi
done

echo "UID available for cyb3rhq user is:";
echo ${new_uid}

# Verify that the uid and gid exist and match
if [[ $new_uid -eq 0 ]] || [[ $new_gid -eq 0 ]];
    then
    echo "Getting unique id numbers (uid, gid) failed!";
    exit 1;
fi
if [[ ${new_uid} != ${new_gid} ]]
    then
    echo "I failed to find matching free uid and gid!";
    exit 5;
fi

# Creating the group
echo "Checking group..."
if [[ $(dscl . -read /Groups/cyb3rhq) ]]
    then
    echo "cyb3rhq group already exists.";
else
    sudo ${DSCL} localhost -create /Local/Default/Groups/cyb3rhq
    check_errm "Error creating group cyb3rhq" "67"
    sudo ${DSCL} localhost -createprop /Local/Default/Groups/cyb3rhq PrimaryGroupID ${new_gid}
    sudo ${DSCL} localhost -createprop /Local/Default/Groups/cyb3rhq RealName cyb3rhq
    sudo ${DSCL} localhost -createprop /Local/Default/Groups/cyb3rhq RecordName cyb3rhq
    sudo ${DSCL} localhost -createprop /Local/Default/Groups/cyb3rhq RecordType: dsRecTypeStandard:Groups
    sudo ${DSCL} localhost -createprop /Local/Default/Groups/cyb3rhq Password "*"
fi

# Creating the user
echo "Checking user..."
if [[ $(dscl . -read /Users/cyb3rhq) ]]
    then
    echo "cyb3rhq user already exists.";
else
    sudo ${DSCL} localhost -create /Local/Default/Users/cyb3rhq
    check_errm "Error creating user cyb3rhq" "77"
    sudo ${DSCL} localhost -createprop /Local/Default/Users/cyb3rhq RecordName cyb3rhq
    sudo ${DSCL} localhost -createprop /Local/Default/Users/cyb3rhq RealName cyb3rhq
    sudo ${DSCL} localhost -createprop /Local/Default/Users/cyb3rhq UserShell /usr/bin/false
    sudo ${DSCL} localhost -createprop /Local/Default/Users/cyb3rhq NFSHomeDirectory /var/cyb3rhq
    sudo ${DSCL} localhost -createprop /Local/Default/Users/cyb3rhq UniqueID ${new_uid}
    sudo ${DSCL} localhost -createprop /Local/Default/Users/cyb3rhq PrimaryGroupID ${new_gid}
    sudo ${DSCL} localhost -append /Local/Default/Groups/cyb3rhq GroupMembership cyb3rhq
    sudo ${DSCL} localhost -createprop /Local/Default/Users/cyb3rhq Password "*"
fi

#Hide the fixed users
echo "Hiding the fixed cyb3rhq user"
dscl . create /Users/cyb3rhq IsHidden 1
