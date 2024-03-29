# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import store_pb2 as store__pb2


class StoreStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetProductPrice = channel.unary_unary(
        '/proto.store.Store/GetProductPrice',
        request_serializer=store__pb2.GetProductPriceRequest.SerializeToString,
        response_deserializer=store__pb2.GetProductPriceResponse.FromString,
        )
    self.SellProduct = channel.unary_unary(
        '/proto.store.Store/SellProduct',
        request_serializer=store__pb2.SellProductRequest.SerializeToString,
        response_deserializer=store__pb2.SellProductResponse.FromString,
        )
    self.KillServer = channel.unary_unary(
        '/proto.store.Store/KillServer',
        request_serializer=store__pb2.KillServerRequest.SerializeToString,
        response_deserializer=store__pb2.KillServerResponse.FromString,
        )


class StoreServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetProductPrice(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SellProduct(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KillServer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetProductPrice': grpc.unary_unary_rpc_method_handler(
          servicer.GetProductPrice,
          request_deserializer=store__pb2.GetProductPriceRequest.FromString,
          response_serializer=store__pb2.GetProductPriceResponse.SerializeToString,
      ),
      'SellProduct': grpc.unary_unary_rpc_method_handler(
          servicer.SellProduct,
          request_deserializer=store__pb2.SellProductRequest.FromString,
          response_serializer=store__pb2.SellProductResponse.SerializeToString,
      ),
      'KillServer': grpc.unary_unary_rpc_method_handler(
          servicer.KillServer,
          request_deserializer=store__pb2.KillServerRequest.FromString,
          response_serializer=store__pb2.KillServerResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.store.Store', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
