# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/getServerVersion.proto',
  package='protoFile',
  serialized_pb='\n protoFile/getServerVersion.proto\x12\tprotoFile\"%\n\x12getVersionResponse\x12\x0f\n\x07version\x18\x01 \x02(\t')




_GETVERSIONRESPONSE = descriptor.Descriptor(
  name='getVersionResponse',
  full_name='protoFile.getVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version', full_name='protoFile.getVersionResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=47,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['getVersionResponse'] = _GETVERSIONRESPONSE

class getVersionResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETVERSIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.getVersionResponse)

# @@protoc_insertion_point(module_scope)
