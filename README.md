# Example gRPC - client and server

Generate RSA key pair for the server. Uses `openssl`.

```
make gen_key
```

Install gRPC Python packages.

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
