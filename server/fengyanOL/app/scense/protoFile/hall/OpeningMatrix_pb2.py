# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/hall/OpeningMatrix.proto',
  package='protoFile.hall.OpeningMatrix',
  serialized_pb='\n\"protoFile/hall/OpeningMatrix.proto\x12\x1cprotoFile.hall.OpeningMatrix\"z\n\x14OpeningMatrixRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08matrixId\x18\x02 \x02(\x05\x12\x44\n\x0ematrixListInfo\x18\x03 \x03(\x0b\x32,.protoFile.hall.OpeningMatrix.MatrixListInfo\"-\n\x0eMatrixListInfo\x12\x0e\n\x06roleId\x18\x01 \x01(\x05\x12\x0b\n\x03pos\x18\x02 \x01(\x05\"8\n\x15OpeningMatrixResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_OPENINGMATRIXREQUEST = descriptor.Descriptor(
  name='OpeningMatrixRequest',
  full_name='protoFile.hall.OpeningMatrix.OpeningMatrixRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.hall.OpeningMatrix.OpeningMatrixRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='matrixId', full_name='protoFile.hall.OpeningMatrix.OpeningMatrixRequest.matrixId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='matrixListInfo', full_name='protoFile.hall.OpeningMatrix.OpeningMatrixRequest.matrixListInfo', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=68,
  serialized_end=190,
)


_MATRIXLISTINFO = descriptor.Descriptor(
  name='MatrixListInfo',
  full_name='protoFile.hall.OpeningMatrix.MatrixListInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roleId', full_name='protoFile.hall.OpeningMatrix.MatrixListInfo.roleId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos', full_name='protoFile.hall.OpeningMatrix.MatrixListInfo.pos', index=1,
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
  serialized_start=192,
  serialized_end=237,
)


_OPENINGMATRIXRESPONSE = descriptor.Descriptor(
  name='OpeningMatrixResponse',
  full_name='protoFile.hall.OpeningMatrix.OpeningMatrixResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.hall.OpeningMatrix.OpeningMatrixResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.hall.OpeningMatrix.OpeningMatrixResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=239,
  serialized_end=295,
)

_OPENINGMATRIXREQUEST.fields_by_name['matrixListInfo'].message_type = _MATRIXLISTINFO
DESCRIPTOR.message_types_by_name['OpeningMatrixRequest'] = _OPENINGMATRIXREQUEST
DESCRIPTOR.message_types_by_name['MatrixListInfo'] = _MATRIXLISTINFO
DESCRIPTOR.message_types_by_name['OpeningMatrixResponse'] = _OPENINGMATRIXRESPONSE

class OpeningMatrixRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPENINGMATRIXREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.hall.OpeningMatrix.OpeningMatrixRequest)

class MatrixListInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MATRIXLISTINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.hall.OpeningMatrix.MatrixListInfo)

class OpeningMatrixResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPENINGMATRIXRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.hall.OpeningMatrix.OpeningMatrixResponse)

# @@protoc_insertion_point(module_scope)