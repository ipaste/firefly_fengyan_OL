# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/beginners/beginnersRegist.proto',
  package='protoFile.beginners.beginnersRegist',
  serialized_pb='\n)protoFile/beginners/beginnersRegist.proto\x12#protoFile.beginners.beginnersRegist\">\n\x16\x62\x65ginnersRegistRequest\x12\x12\n\nbeginnerId\x18\x01 \x02(\x05\x12\x10\n\x08nickname\x18\x02 \x02(\t\"H\n\x17\x62\x65ginnersRegistResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x05')




_BEGINNERSREGISTREQUEST = descriptor.Descriptor(
  name='beginnersRegistRequest',
  full_name='protoFile.beginners.beginnersRegist.beginnersRegistRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='beginnerId', full_name='protoFile.beginners.beginnersRegist.beginnersRegistRequest.beginnerId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nickname', full_name='protoFile.beginners.beginnersRegist.beginnersRegistRequest.nickname', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=82,
  serialized_end=144,
)


_BEGINNERSREGISTRESPONSE = descriptor.Descriptor(
  name='beginnersRegistResponse',
  full_name='protoFile.beginners.beginnersRegist.beginnersRegistResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.beginners.beginnersRegist.beginnersRegistResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.beginners.beginnersRegist.beginnersRegistResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.beginners.beginnersRegist.beginnersRegistResponse.data', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  extension_ranges=[],
  serialized_start=146,
  serialized_end=218,
)

DESCRIPTOR.message_types_by_name['beginnersRegistRequest'] = _BEGINNERSREGISTREQUEST
DESCRIPTOR.message_types_by_name['beginnersRegistResponse'] = _BEGINNERSREGISTRESPONSE

class beginnersRegistRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BEGINNERSREGISTREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.beginners.beginnersRegist.beginnersRegistRequest)

class beginnersRegistResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BEGINNERSREGISTRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.beginners.beginnersRegist.beginnersRegistResponse)

# @@protoc_insertion_point(module_scope)
