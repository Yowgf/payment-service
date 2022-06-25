# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: store.proto

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
  name='store.proto',
  package='proto.store',
  syntax='proto3',
  serialized_pb=_b('\n\x0bstore.proto\x12\x0bproto.store\"\x18\n\x16GetProductPriceRequest\"(\n\x17GetProductPriceResponse\x12\r\n\x05price\x18\x01 \x01(\r\"%\n\x12SellProductRequest\x12\x0f\n\x07orderId\x18\x01 \x01(\x0c\"$\n\x13SellProductResponse\x12\r\n\x05price\x18\x01 \x01(\x05\"\x13\n\x11KillServerRequest\"*\n\x12KillServerResponse\x12\x14\n\x0cstoreBalance\x18\x01 \x01(\x05\x32\x8c\x02\n\x05Store\x12^\n\x0fGetProductPrice\x12#.proto.store.GetProductPriceRequest\x1a$.proto.store.GetProductPriceResponse\"\x00\x12R\n\x0bSellProduct\x12\x1f.proto.store.SellProductRequest\x1a .proto.store.SellProductResponse\"\x00\x12O\n\nKillServer\x12\x1e.proto.store.KillServerRequest\x1a\x1f.proto.store.KillServerResponse\"\x00\x62\x06proto3')
)




_GETPRODUCTPRICEREQUEST = _descriptor.Descriptor(
  name='GetProductPriceRequest',
  full_name='proto.store.GetProductPriceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=28,
  serialized_end=52,
)


_GETPRODUCTPRICERESPONSE = _descriptor.Descriptor(
  name='GetProductPriceResponse',
  full_name='proto.store.GetProductPriceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='proto.store.GetProductPriceResponse.price', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=54,
  serialized_end=94,
)


_SELLPRODUCTREQUEST = _descriptor.Descriptor(
  name='SellProductRequest',
  full_name='proto.store.SellProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderId', full_name='proto.store.SellProductRequest.orderId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=96,
  serialized_end=133,
)


_SELLPRODUCTRESPONSE = _descriptor.Descriptor(
  name='SellProductResponse',
  full_name='proto.store.SellProductResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='proto.store.SellProductResponse.price', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=135,
  serialized_end=171,
)


_KILLSERVERREQUEST = _descriptor.Descriptor(
  name='KillServerRequest',
  full_name='proto.store.KillServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=173,
  serialized_end=192,
)


_KILLSERVERRESPONSE = _descriptor.Descriptor(
  name='KillServerResponse',
  full_name='proto.store.KillServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='storeBalance', full_name='proto.store.KillServerResponse.storeBalance', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=194,
  serialized_end=236,
)

DESCRIPTOR.message_types_by_name['GetProductPriceRequest'] = _GETPRODUCTPRICEREQUEST
DESCRIPTOR.message_types_by_name['GetProductPriceResponse'] = _GETPRODUCTPRICERESPONSE
DESCRIPTOR.message_types_by_name['SellProductRequest'] = _SELLPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['SellProductResponse'] = _SELLPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['KillServerRequest'] = _KILLSERVERREQUEST
DESCRIPTOR.message_types_by_name['KillServerResponse'] = _KILLSERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetProductPriceRequest = _reflection.GeneratedProtocolMessageType('GetProductPriceRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTPRICEREQUEST,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:proto.store.GetProductPriceRequest)
  ))
_sym_db.RegisterMessage(GetProductPriceRequest)

GetProductPriceResponse = _reflection.GeneratedProtocolMessageType('GetProductPriceResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTPRICERESPONSE,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:proto.store.GetProductPriceResponse)
  ))
_sym_db.RegisterMessage(GetProductPriceResponse)

SellProductRequest = _reflection.GeneratedProtocolMessageType('SellProductRequest', (_message.Message,), dict(
  DESCRIPTOR = _SELLPRODUCTREQUEST,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:proto.store.SellProductRequest)
  ))
_sym_db.RegisterMessage(SellProductRequest)

SellProductResponse = _reflection.GeneratedProtocolMessageType('SellProductResponse', (_message.Message,), dict(
  DESCRIPTOR = _SELLPRODUCTRESPONSE,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:proto.store.SellProductResponse)
  ))
_sym_db.RegisterMessage(SellProductResponse)

KillServerRequest = _reflection.GeneratedProtocolMessageType('KillServerRequest', (_message.Message,), dict(
  DESCRIPTOR = _KILLSERVERREQUEST,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:proto.store.KillServerRequest)
  ))
_sym_db.RegisterMessage(KillServerRequest)

KillServerResponse = _reflection.GeneratedProtocolMessageType('KillServerResponse', (_message.Message,), dict(
  DESCRIPTOR = _KILLSERVERRESPONSE,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:proto.store.KillServerResponse)
  ))
_sym_db.RegisterMessage(KillServerResponse)



_STORE = _descriptor.ServiceDescriptor(
  name='Store',
  full_name='proto.store.Store',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=239,
  serialized_end=507,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetProductPrice',
    full_name='proto.store.Store.GetProductPrice',
    index=0,
    containing_service=None,
    input_type=_GETPRODUCTPRICEREQUEST,
    output_type=_GETPRODUCTPRICERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SellProduct',
    full_name='proto.store.Store.SellProduct',
    index=1,
    containing_service=None,
    input_type=_SELLPRODUCTREQUEST,
    output_type=_SELLPRODUCTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='KillServer',
    full_name='proto.store.Store.KillServer',
    index=2,
    containing_service=None,
    input_type=_KILLSERVERREQUEST,
    output_type=_KILLSERVERRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STORE)

DESCRIPTOR.services_by_name['Store'] = _STORE

# @@protoc_insertion_point(module_scope)
