#!/usr/bin/env bash

if [ "$HOSTNAME" == "cyb3rhq-master" ]; then
  mkdir -p /var/ossec/etc/decoders/subdir
  chown -R cyb3rhq:cyb3rhq /var/ossec/etc/decoders/subdir
  sed -i -e "/<decoder_dir>etc\/decoders<\/decoder_dir>/a \    <decoder_dir>etc/decoders/subdir</decoder_dir>" /var/ossec/etc/ossec.conf
  mkdir -p /var/ossec/etc/rules/subdir
  chown -R cyb3rhq:cyb3rhq /var/ossec/etc/rules/subdir
  sed -i -e "/<rule_dir>etc\/rules<\/rule_dir>/a \   <rule_dir>etc/rules/subdir</rule_dir>" /var/ossec/etc/ossec.conf
fi
