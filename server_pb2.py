# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0cserver.proto\"M\n\x03RFQ\x12\n\n\x02ID\x18\x01 \x01(\x05\x12\x11\n\taccountid\x18\x02 \x01(\x05\x12\x15\n\rproductnumber\x18\x03 \x01(\x05\x12\x10\n\x08quantity\x18\x04 \x01(\x05\x62\x06proto3')
)




_RFQ = _descriptor.Descriptor(
  name='RFQ',
  full_name='RFQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='RFQ.ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accountid', full_name='RFQ.accountid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productnumber', full_name='RFQ.productnumber', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='RFQ.quantity', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['RFQ'] = _RFQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RFQ = _reflection.GeneratedProtocolMessageType('RFQ', (_message.Message,), dict(
  DESCRIPTOR = _RFQ,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:RFQ)
  ))
_sym_db.RegisterMessage(RFQ)


# @@protoc_insertion_point(module_scope)
