# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/campaign/GetXuYuanInfo4404.proto',
  package='protoFile.campaign.GetXuYuanInfo4404',
  serialized_pb='\n*protoFile/campaign/GetXuYuanInfo4404.proto\x12$protoFile.campaign.GetXuYuanInfo4404\"\"\n\x14GetXuYuanInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"~\n\x15GetXuYuanInfoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\x12\x44\n\nxuYuanInfo\x18\x03 \x01(\x0b\x32\x30.protoFile.campaign.GetXuYuanInfo4404.XuYuanInfo\"_\n\nXuYuanInfo\x12\x0f\n\x07xyValue\x18\x01 \x01(\x05\x12@\n\x08usedInfo\x18\x02 \x03(\x0b\x32..protoFile.campaign.GetXuYuanInfo4404.UsedInfo\"&\n\x08UsedInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05')




_GETXUYUANINFOREQUEST = descriptor.Descriptor(
  name='GetXuYuanInfoRequest',
  full_name='protoFile.campaign.GetXuYuanInfo4404.GetXuYuanInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.campaign.GetXuYuanInfo4404.GetXuYuanInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=84,
  serialized_end=118,
)


_GETXUYUANINFORESPONSE = descriptor.Descriptor(
  name='GetXuYuanInfoResponse',
  full_name='protoFile.campaign.GetXuYuanInfo4404.GetXuYuanInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.campaign.GetXuYuanInfo4404.GetXuYuanInfoResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.campaign.GetXuYuanInfo4404.GetXuYuanInfoResponse.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xuYuanInfo', full_name='protoFile.campaign.GetXuYuanInfo4404.GetXuYuanInfoResponse.xuYuanInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=120,
  serialized_end=246,
)


_XUYUANINFO = descriptor.Descriptor(
  name='XuYuanInfo',
  full_name='protoFile.campaign.GetXuYuanInfo4404.XuYuanInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='xyValue', full_name='protoFile.campaign.GetXuYuanInfo4404.XuYuanInfo.xyValue', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='usedInfo', full_name='protoFile.campaign.GetXuYuanInfo4404.XuYuanInfo.usedInfo', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=248,
  serialized_end=343,
)


_USEDINFO = descriptor.Descriptor(
  name='UsedInfo',
  full_name='protoFile.campaign.GetXuYuanInfo4404.UsedInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='protoFile.campaign.GetXuYuanInfo4404.UsedInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.campaign.GetXuYuanInfo4404.UsedInfo.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=345,
  serialized_end=383,
)

_GETXUYUANINFORESPONSE.fields_by_name['xuYuanInfo'].message_type = _XUYUANINFO
_XUYUANINFO.fields_by_name['usedInfo'].message_type = _USEDINFO
DESCRIPTOR.message_types_by_name['GetXuYuanInfoRequest'] = _GETXUYUANINFOREQUEST
DESCRIPTOR.message_types_by_name['GetXuYuanInfoResponse'] = _GETXUYUANINFORESPONSE
DESCRIPTOR.message_types_by_name['XuYuanInfo'] = _XUYUANINFO
DESCRIPTOR.message_types_by_name['UsedInfo'] = _USEDINFO

class GetXuYuanInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETXUYUANINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.GetXuYuanInfo4404.GetXuYuanInfoRequest)

class GetXuYuanInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETXUYUANINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.GetXuYuanInfo4404.GetXuYuanInfoResponse)

class XuYuanInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _XUYUANINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.GetXuYuanInfo4404.XuYuanInfo)

class UsedInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USEDINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.GetXuYuanInfo4404.UsedInfo)

# @@protoc_insertion_point(module_scope)
