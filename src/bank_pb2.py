# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bank.proto

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
  name='bank.proto',
  package='proto.bank',
  syntax='proto3',
  serialized_pb=_b('\n\nbank.proto\x12\nproto.bank\"%\n\x11GetBalanceRequest\x12\x10\n\x08walletId\x18\x01 \x01(\t\"%\n\x12GetBalanceResponse\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x05\".\n\nPayRequest\x12\x10\n\x08walletId\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\r\".\n\x0bPayResponse\x12\x0f\n\x07orderId\x18\x01 \x01(\x0c\x12\x0e\n\x06status\x18\x02 \x01(\x05\"J\n\x0fTransferRequest\x12\x16\n\x0etargetWalletId\x18\x01 \x01(\t\x12\x0f\n\x07orderId\x18\x02 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x03 \x01(\r\"\"\n\x10TransferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x13\n\x11KillServerRequest\")\n\x12KillServerResponse\x12\x13\n\x0bnumAccounts\x18\x01 \x01(\r2\xa7\x02\n\x04\x42\x61nk\x12M\n\nGetBalance\x12\x1d.proto.bank.GetBalanceRequest\x1a\x1e.proto.bank.GetBalanceResponse\"\x00\x12\x38\n\x03Pay\x12\x16.proto.bank.PayRequest\x1a\x17.proto.bank.PayResponse\"\x00\x12G\n\x08Transfer\x12\x1b.proto.bank.TransferRequest\x1a\x1c.proto.bank.TransferResponse\"\x00\x12M\n\nKillServer\x12\x1d.proto.bank.KillServerRequest\x1a\x1e.proto.bank.KillServerResponse\"\x00\x62\x06proto3')
)




_GETBALANCEREQUEST = _descriptor.Descriptor(
  name='GetBalanceRequest',
  full_name='proto.bank.GetBalanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='walletId', full_name='proto.bank.GetBalanceRequest.walletId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=26,
  serialized_end=63,
)


_GETBALANCERESPONSE = _descriptor.Descriptor(
  name='GetBalanceResponse',
  full_name='proto.bank.GetBalanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='balance', full_name='proto.bank.GetBalanceResponse.balance', index=0,
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
  serialized_start=65,
  serialized_end=102,
)


_PAYREQUEST = _descriptor.Descriptor(
  name='PayRequest',
  full_name='proto.bank.PayRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='walletId', full_name='proto.bank.PayRequest.walletId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='proto.bank.PayRequest.amount', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=104,
  serialized_end=150,
)


_PAYRESPONSE = _descriptor.Descriptor(
  name='PayResponse',
  full_name='proto.bank.PayResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderId', full_name='proto.bank.PayResponse.orderId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.bank.PayResponse.status', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=152,
  serialized_end=198,
)


_TRANSFERREQUEST = _descriptor.Descriptor(
  name='TransferRequest',
  full_name='proto.bank.TransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetWalletId', full_name='proto.bank.TransferRequest.targetWalletId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderId', full_name='proto.bank.TransferRequest.orderId', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='proto.bank.TransferRequest.amount', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=200,
  serialized_end=274,
)


_TRANSFERRESPONSE = _descriptor.Descriptor(
  name='TransferResponse',
  full_name='proto.bank.TransferResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.bank.TransferResponse.status', index=0,
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
  serialized_start=276,
  serialized_end=310,
)


_KILLSERVERREQUEST = _descriptor.Descriptor(
  name='KillServerRequest',
  full_name='proto.bank.KillServerRequest',
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
  serialized_start=312,
  serialized_end=331,
)


_KILLSERVERRESPONSE = _descriptor.Descriptor(
  name='KillServerResponse',
  full_name='proto.bank.KillServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numAccounts', full_name='proto.bank.KillServerResponse.numAccounts', index=0,
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
  serialized_start=333,
  serialized_end=374,
)

DESCRIPTOR.message_types_by_name['GetBalanceRequest'] = _GETBALANCEREQUEST
DESCRIPTOR.message_types_by_name['GetBalanceResponse'] = _GETBALANCERESPONSE
DESCRIPTOR.message_types_by_name['PayRequest'] = _PAYREQUEST
DESCRIPTOR.message_types_by_name['PayResponse'] = _PAYRESPONSE
DESCRIPTOR.message_types_by_name['TransferRequest'] = _TRANSFERREQUEST
DESCRIPTOR.message_types_by_name['TransferResponse'] = _TRANSFERRESPONSE
DESCRIPTOR.message_types_by_name['KillServerRequest'] = _KILLSERVERREQUEST
DESCRIPTOR.message_types_by_name['KillServerResponse'] = _KILLSERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBalanceRequest = _reflection.GeneratedProtocolMessageType('GetBalanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBALANCEREQUEST,
  __module__ = 'bank_pb2'
  # @@protoc_insertion_point(class_scope:proto.bank.GetBalanceRequest)
  ))
_sym_db.RegisterMessage(GetBalanceRequest)

GetBalanceResponse = _reflection.GeneratedProtocolMessageType('GetBalanceResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETBALANCERESPONSE,
  __module__ = 'bank_pb2'
  # @@protoc_insertion_point(class_scope:proto.bank.GetBalanceResponse)
  ))
_sym_db.RegisterMessage(GetBalanceResponse)

PayRequest = _reflection.GeneratedProtocolMessageType('PayRequest', (_message.Message,), dict(
  DESCRIPTOR = _PAYREQUEST,
  __module__ = 'bank_pb2'
  # @@protoc_insertion_point(class_scope:proto.bank.PayRequest)
  ))
_sym_db.RegisterMessage(PayRequest)

PayResponse = _reflection.GeneratedProtocolMessageType('PayResponse', (_message.Message,), dict(
  DESCRIPTOR = _PAYRESPONSE,
  __module__ = 'bank_pb2'
  # @@protoc_insertion_point(class_scope:proto.bank.PayResponse)
  ))
_sym_db.RegisterMessage(PayResponse)

TransferRequest = _reflection.GeneratedProtocolMessageType('TransferRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERREQUEST,
  __module__ = 'bank_pb2'
  # @@protoc_insertion_point(class_scope:proto.bank.TransferRequest)
  ))
_sym_db.RegisterMessage(TransferRequest)

TransferResponse = _reflection.GeneratedProtocolMessageType('TransferResponse', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERRESPONSE,
  __module__ = 'bank_pb2'
  # @@protoc_insertion_point(class_scope:proto.bank.TransferResponse)
  ))
_sym_db.RegisterMessage(TransferResponse)

KillServerRequest = _reflection.GeneratedProtocolMessageType('KillServerRequest', (_message.Message,), dict(
  DESCRIPTOR = _KILLSERVERREQUEST,
  __module__ = 'bank_pb2'
  # @@protoc_insertion_point(class_scope:proto.bank.KillServerRequest)
  ))
_sym_db.RegisterMessage(KillServerRequest)

KillServerResponse = _reflection.GeneratedProtocolMessageType('KillServerResponse', (_message.Message,), dict(
  DESCRIPTOR = _KILLSERVERRESPONSE,
  __module__ = 'bank_pb2'
  # @@protoc_insertion_point(class_scope:proto.bank.KillServerResponse)
  ))
_sym_db.RegisterMessage(KillServerResponse)



_BANK = _descriptor.ServiceDescriptor(
  name='Bank',
  full_name='proto.bank.Bank',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=377,
  serialized_end=672,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBalance',
    full_name='proto.bank.Bank.GetBalance',
    index=0,
    containing_service=None,
    input_type=_GETBALANCEREQUEST,
    output_type=_GETBALANCERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Pay',
    full_name='proto.bank.Bank.Pay',
    index=1,
    containing_service=None,
    input_type=_PAYREQUEST,
    output_type=_PAYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Transfer',
    full_name='proto.bank.Bank.Transfer',
    index=2,
    containing_service=None,
    input_type=_TRANSFERREQUEST,
    output_type=_TRANSFERRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='KillServer',
    full_name='proto.bank.Bank.KillServer',
    index=3,
    containing_service=None,
    input_type=_KILLSERVERREQUEST,
    output_type=_KILLSERVERRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BANK)

DESCRIPTOR.services_by_name['Bank'] = _BANK

# @@protoc_insertion_point(module_scope)
