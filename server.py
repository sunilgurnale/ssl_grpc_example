import signal
from concurrent import futures

import grpc

import service_pb2
import service_pb2_grpc


class ServerServicer(service_pb2_grpc.ServerServicer):
    def Foo(self, request, context):
        return service_pb2.Empty()


def main():
    port = '1337'

    with open('server.key', 'rb') as f:
        private_key = f.read()
    with open('server.crt', 'rb') as f:
        certificate_chain = f.read()

    server_credentials = grpc.ssl_server_credentials(
      ((private_key, certificate_chain,),))

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    service_pb2_grpc.add_ServerServicer_to_server(ServerServicer(), server)

    server.add_secure_port('[::]:'+port, server_credentials)

    server.start()
    try:
        while True:
            signal.pause()
    except KeyboardInterrupt:
        pass
    server.stop(0)

if __name__ == '__main__':
    main()
