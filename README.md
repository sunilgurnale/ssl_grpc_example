# Example gRPC - client and server

Generate public-private key for server. Uses openssl.

```
make gen_key
```

Install grpc packages.

```
pip install -r requirements.txt
```

Create the gRPC stubs:

```
make stubs
```

Run server:
```
make server
```

Run client
```
make client
```
