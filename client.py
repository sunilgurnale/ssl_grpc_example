import grpc

import service_pb2


def main():
    host = 'localhost'
    port = 1337

    with open('server.crt') as f:
        trusted_certs = f.read()

    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    channel = grpc.secure_channel('{}:{}'.format(host, port), credentials)

    stub = service_pb2.ServerStub(channel)
    stub.Foo(service_pb2.Empty())

if __name__ == '__main__':
    main()
