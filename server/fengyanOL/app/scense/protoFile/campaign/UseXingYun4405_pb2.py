# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/campaign/UseXingYun4405.proto',
  package='protoFile.campaign.UseXingYun4405',
  serialized_pb='\n\'protoFile/campaign/UseXingYun4405.proto\x12!protoFile.campaign.UseXingYun4405\"-\n\x11UseXingYunRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04type\x18\x02 \x02(\x05\"5\n\x12UseXingYunResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08')




_USEXINGYUNREQUEST = descriptor.Descriptor(
  name='UseXingYunRequest',
  full_name='protoFile.campaign.UseXingYun4405.UseXingYunRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.campaign.UseXingYun4405.UseXingYunRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.campaign.UseXingYun4405.UseXingYunRequest.type', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=78,
  serialized_end=123,
)


_USEXINGYUNRESPONSE = descriptor.Descriptor(
  name='UseXingYunResponse',
  full_name='protoFile.campaign.UseXingYun4405.UseXingYunResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.campaign.UseXingYun4405.UseXingYunResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.campaign.UseXingYun4405.UseXingYunResponse.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=125,
  serialized_end=178,
)

DESCRIPTOR.message_types_by_name['UseXingYunRequest'] = _USEXINGYUNREQUEST
DESCRIPTOR.message_types_by_name['UseXingYunResponse'] = _USEXINGYUNRESPONSE

class UseXingYunRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USEXINGYUNREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.UseXingYun4405.UseXingYunRequest)

class UseXingYunResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USEXINGYUNRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.UseXingYun4405.UseXingYunResponse)

# @@protoc_insertion_point(module_scope)
