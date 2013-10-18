# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/shop/NpcShopBuyItem.proto',
  package='protoFile.shop.NpcShopBuyItem',
  serialized_pb='\n#protoFile/shop/NpcShopBuyItem.proto\x12\x1dprotoFile.shop.NpcShopBuyItem\"c\n\x15npcShopBuyItemRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06itemId\x18\x02 \x02(\x05\x12\x0f\n\x07opeType\x18\x03 \x02(\x05\x12\x0e\n\x06\x62uyNum\x18\x04 \x02(\x05\x12\r\n\x05npcId\x18\x05 \x02(\x05\"t\n\x16npcShopBuyItemResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x39\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32+.protoFile.shop.NpcShopBuyItem.ResponseInfo\"\x1f\n\x0cResponseInfo\x12\x0f\n\x07opeType\x18\x01 \x01(\x05')




_NPCSHOPBUYITEMREQUEST = descriptor.Descriptor(
  name='npcShopBuyItemRequest',
  full_name='protoFile.shop.NpcShopBuyItem.npcShopBuyItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.shop.NpcShopBuyItem.npcShopBuyItemRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='itemId', full_name='protoFile.shop.NpcShopBuyItem.npcShopBuyItemRequest.itemId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='opeType', full_name='protoFile.shop.NpcShopBuyItem.npcShopBuyItemRequest.opeType', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buyNum', full_name='protoFile.shop.NpcShopBuyItem.npcShopBuyItemRequest.buyNum', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npcId', full_name='protoFile.shop.NpcShopBuyItem.npcShopBuyItemRequest.npcId', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=70,
  serialized_end=169,
)


_NPCSHOPBUYITEMRESPONSE = descriptor.Descriptor(
  name='npcShopBuyItemResponse',
  full_name='protoFile.shop.NpcShopBuyItem.npcShopBuyItemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.shop.NpcShopBuyItem.npcShopBuyItemResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.shop.NpcShopBuyItem.npcShopBuyItemResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.shop.NpcShopBuyItem.npcShopBuyItemResponse.data', index=2,
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
  serialized_start=171,
  serialized_end=287,
)


_RESPONSEINFO = descriptor.Descriptor(
  name='ResponseInfo',
  full_name='protoFile.shop.NpcShopBuyItem.ResponseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='opeType', full_name='protoFile.shop.NpcShopBuyItem.ResponseInfo.opeType', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=289,
  serialized_end=320,
)

_NPCSHOPBUYITEMRESPONSE.fields_by_name['data'].message_type = _RESPONSEINFO
DESCRIPTOR.message_types_by_name['npcShopBuyItemRequest'] = _NPCSHOPBUYITEMREQUEST
DESCRIPTOR.message_types_by_name['npcShopBuyItemResponse'] = _NPCSHOPBUYITEMRESPONSE
DESCRIPTOR.message_types_by_name['ResponseInfo'] = _RESPONSEINFO

class npcShopBuyItemRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NPCSHOPBUYITEMREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.NpcShopBuyItem.npcShopBuyItemRequest)

class npcShopBuyItemResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NPCSHOPBUYITEMRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.NpcShopBuyItem.npcShopBuyItemResponse)

class ResponseInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.NpcShopBuyItem.ResponseInfo)

# @@protoc_insertion_point(module_scope)