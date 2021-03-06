# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import locationv1_pb2 as locationv1__pb2


class location_serviceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.convert_location = channel.unary_unary(
        '/locationservice.location_service/convert_location',
        request_serializer=locationv1__pb2.location.SerializeToString,
        response_deserializer=locationv1__pb2.map_coordinate.FromString,
        )


class location_serviceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def convert_location(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_location_serviceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'convert_location': grpc.unary_unary_rpc_method_handler(
          servicer.convert_location,
          request_deserializer=locationv1__pb2.location.FromString,
          response_serializer=locationv1__pb2.map_coordinate.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'locationservice.location_service', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
