# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='getMallItemInfo208.proto',
  package='proto.shop.shop208',
  serialized_pb='\n\x18getMallItemInfo208.proto\x12\x12proto.shop.shop208\"F\n\x16getMallItemInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x12\n\ncategories\x18\x02 \x02(\x05\x12\x0c\n\x04page\x18\x03 \x02(\x05\"j\n\x17getMallItemInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12.\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32 .proto.shop.shop208.ResponseData\"\x9d\x01\n\x0cResponseData\x12\x0f\n\x07\x63urpage\x18\x01 \x01(\x05\x12\x12\n\ncategories\x18\x02 \x01(\x05\x12\x0c\n\x04goal\x18\x03 \x01(\x05\x12+\n\x05items\x18\x04 \x03(\x0b\x32\x1c.proto.shop.shop208.ItemIifo\x12-\n\x07zxItems\x18\x05 \x03(\x0b\x32\x1c.proto.shop.shop208.ItemIifo\"l\n\x08ItemIifo\x12\x12\n\ntemplateId\x18\x01 \x02(\x05\x12\x0c\n\x04type\x18\x02 \x02(\x05\x12\r\n\x05price\x18\x03 \x02(\x05\x12\r\n\x05\x63ount\x18\x04 \x02(\x05\x12\x0e\n\x06itemID\x18\x05 \x02(\x05\x12\x10\n\x08priceNow\x18\x06 \x01(\x05*5\n\x0cMallItemType\x12\t\n\x05NOMAL\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\x07\n\x03HOT\x10\x02\x12\x08\n\x04SALL\x10\x03')

_MALLITEMTYPE = descriptor.EnumDescriptor(
  name='MallItemType',
  full_name='proto.shop.shop208.MallItemType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='NOMAL', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='NEW', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='HOT', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SALL', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=498,
  serialized_end=551,
)


NOMAL = 0
NEW = 1
HOT = 2
SALL = 3



_GETMALLITEMINFOREQUEST = descriptor.Descriptor(
  name='getMallItemInfoRequest',
  full_name='proto.shop.shop208.getMallItemInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='proto.shop.shop208.getMallItemInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='categories', full_name='proto.shop.shop208.getMallItemInfoRequest.categories', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='page', full_name='proto.shop.shop208.getMallItemInfoRequest.page', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=48,
  serialized_end=118,
)


_GETMALLITEMINFORESPONSE = descriptor.Descriptor(
  name='getMallItemInfoResponse',
  full_name='proto.shop.shop208.getMallItemInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='proto.shop.shop208.getMallItemInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='proto.shop.shop208.getMallItemInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='proto.shop.shop208.getMallItemInfoResponse.data', index=2,
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
  serialized_end=226,
)


_RESPONSEDATA = descriptor.Descriptor(
  name='ResponseData',
  full_name='proto.shop.shop208.ResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='curpage', full_name='proto.shop.shop208.ResponseData.curpage', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='categories', full_name='proto.shop.shop208.ResponseData.categories', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='goal', full_name='proto.shop.shop208.ResponseData.goal', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='items', full_name='proto.shop.shop208.ResponseData.items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='zxItems', full_name='proto.shop.shop208.ResponseData.zxItems', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=229,
  serialized_end=386,
)


_ITEMIIFO = descriptor.Descriptor(
  name='ItemIifo',
  full_name='proto.shop.shop208.ItemIifo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='templateId', full_name='proto.shop.shop208.ItemIifo.templateId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='proto.shop.shop208.ItemIifo.type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='price', full_name='proto.shop.shop208.ItemIifo.price', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='proto.shop.shop208.ItemIifo.count', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='itemID', full_name='proto.shop.shop208.ItemIifo.itemID', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='priceNow', full_name='proto.shop.shop208.ItemIifo.priceNow', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=388,
  serialized_end=496,
)

_GETMALLITEMINFORESPONSE.fields_by_name['data'].message_type = _RESPONSEDATA
_RESPONSEDATA.fields_by_name['items'].message_type = _ITEMIIFO
_RESPONSEDATA.fields_by_name['zxItems'].message_type = _ITEMIIFO
DESCRIPTOR.message_types_by_name['getMallItemInfoRequest'] = _GETMALLITEMINFOREQUEST
DESCRIPTOR.message_types_by_name['getMallItemInfoResponse'] = _GETMALLITEMINFORESPONSE
DESCRIPTOR.message_types_by_name['ResponseData'] = _RESPONSEDATA
DESCRIPTOR.message_types_by_name['ItemIifo'] = _ITEMIIFO

class getMallItemInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETMALLITEMINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:proto.shop.shop208.getMallItemInfoRequest)

class getMallItemInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETMALLITEMINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:proto.shop.shop208.getMallItemInfoResponse)

class ResponseData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEDATA
  
  # @@protoc_insertion_point(class_scope:proto.shop.shop208.ResponseData)

class ItemIifo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMIIFO
  
  # @@protoc_insertion_point(class_scope:proto.shop.shop208.ItemIifo)

# @@protoc_insertion_point(module_scope)
