# SSL and server-side authentication for gRPC

This repository provides a simple example of using SSL and server-side authentication for gRPC using Python.

## Certificate

Generate certificate for the server. Uses `openssl`.

```
make gen_key
```

## Install gRPC packages

```
pip install -r requirements.txt
```

## Generate gRPC stubs

```
make stubs
```

## Run server

```
make server
```

## Run client

```
make client
```
