# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import engine_pb2 as engine__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='request_response.proto',
  package='com.cyb3rhq.api.engine.test',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16request_response.proto\x12\x1b\x63om.cyb3rhq.api.engine.test\x1a\x0c\x65ngine.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xaa\x01\n\x07Request\x12\x12\n\ndefaultStr\x18\x01 \x01(\t\x12\x12\n\ndefaultInt\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65\x66\x61ultBool\x18\x03 \x01(\x08\x12\x18\n\x0bvalueString\x18\x04 \x01(\tH\x00\x88\x01\x01\x12,\n\x07\x61nyJSON\x18\x05 \x01(\x0b\x32\x16.google.protobuf.ValueH\x01\x88\x01\x01\x42\x0e\n\x0c_valueStringB\n\n\x08_anyJSON\"\xc4\x01\n\x08Response\x12\x34\n\x06status\x18\x01 \x01(\x0e\x32$.com.cyb3rhq.api.engine.ReturnStatus\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12-\n\x08valueObj\x18\x03 \x01(\x0b\x32\x16.google.protobuf.ValueH\x01\x88\x01\x01\x12\x18\n\x0bvalueString\x18\x04 \x01(\tH\x02\x88\x01\x01\x42\x08\n\x06_errorB\x0b\n\t_valueObjB\x0e\n\x0c_valueStringb\x06proto3'
  ,
  dependencies=[engine__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='com.cyb3rhq.api.engine.test.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='defaultStr', full_name='com.cyb3rhq.api.engine.test.Request.defaultStr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='defaultInt', full_name='com.cyb3rhq.api.engine.test.Request.defaultInt', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='defaultBool', full_name='com.cyb3rhq.api.engine.test.Request.defaultBool', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valueString', full_name='com.cyb3rhq.api.engine.test.Request.valueString', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='anyJSON', full_name='com.cyb3rhq.api.engine.test.Request.anyJSON', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_valueString', full_name='com.cyb3rhq.api.engine.test.Request._valueString',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_anyJSON', full_name='com.cyb3rhq.api.engine.test.Request._anyJSON',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=100,
  serialized_end=270,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='com.cyb3rhq.api.engine.test.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='com.cyb3rhq.api.engine.test.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='com.cyb3rhq.api.engine.test.Response.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valueObj', full_name='com.cyb3rhq.api.engine.test.Response.valueObj', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valueString', full_name='com.cyb3rhq.api.engine.test.Response.valueString', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_error', full_name='com.cyb3rhq.api.engine.test.Response._error',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_valueObj', full_name='com.cyb3rhq.api.engine.test.Response._valueObj',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_valueString', full_name='com.cyb3rhq.api.engine.test.Response._valueString',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=273,
  serialized_end=469,
)

_REQUEST.fields_by_name['anyJSON'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_REQUEST.oneofs_by_name['_valueString'].fields.append(
  _REQUEST.fields_by_name['valueString'])
_REQUEST.fields_by_name['valueString'].containing_oneof = _REQUEST.oneofs_by_name['_valueString']
_REQUEST.oneofs_by_name['_anyJSON'].fields.append(
  _REQUEST.fields_by_name['anyJSON'])
_REQUEST.fields_by_name['anyJSON'].containing_oneof = _REQUEST.oneofs_by_name['_anyJSON']
_RESPONSE.fields_by_name['status'].enum_type = engine__pb2._RETURNSTATUS
_RESPONSE.fields_by_name['valueObj'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_RESPONSE.oneofs_by_name['_error'].fields.append(
  _RESPONSE.fields_by_name['error'])
_RESPONSE.fields_by_name['error'].containing_oneof = _RESPONSE.oneofs_by_name['_error']
_RESPONSE.oneofs_by_name['_valueObj'].fields.append(
  _RESPONSE.fields_by_name['valueObj'])
_RESPONSE.fields_by_name['valueObj'].containing_oneof = _RESPONSE.oneofs_by_name['_valueObj']
_RESPONSE.oneofs_by_name['_valueString'].fields.append(
  _RESPONSE.fields_by_name['valueString'])
_RESPONSE.fields_by_name['valueString'].containing_oneof = _RESPONSE.oneofs_by_name['_valueString']
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'request_response_pb2'
  # @@protoc_insertion_point(class_scope:com.cyb3rhq.api.engine.test.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'request_response_pb2'
  # @@protoc_insertion_point(class_scope:com.cyb3rhq.api.engine.test.Response)
  })
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
