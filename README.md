# Sample Python gRPC test for OpenShift 

## Certificate

Generate certificate for the server. Uses `openssl`. 

For the CN, use the `*.apps.apps.<cluster_name>.<base_domain>` wildcard hostname for OpenShift:

```
$ oc get ingresses.config/cluster -o jsonpath='{.spec.domain}'
apps.cluster-d3f6.d3f6.example.opentlc.com
```

```
make gen_key
```

## Enable http/2

```
$ oc annotate ingresses.config/cluster ingress.operator.openshift.io/default-enable-http2=true
```

## Create Server

You can either build the image using S2I or deploy a prebuilt image from quay.io

```
$ oc new-app https://github.com/tsailiming ssl_grpc_example --name grpc
```

```
$ oc new-app --docker-image=quay.io/ltsai/python-grpc-demo --name=grpc
```

Configure TLS and expose route:
```
$ oc create secret tls tls-secret --cert=tls/tls.crt --key=tls/tls.key 
$ oc set volume dc/grpc --name=tls-secret --type=secret --secret-name=tls-secret --mount-path=/opt/app-root/src/tls --add
$ oc create route passthrough grpc --service=grpc
```


## Run Client

Using gRPCurl:

```
$ HOSTNAME=`oc get route grpc -o jsonpath='{.spec.host}'`
$ grpcurl  -import-path . -proto service.proto -insecure -cert tls/tls.crt -key tls/tls.key $HOSTNAME:443 Server.Foo
{
  "message": "Hello! Current time is Thu Sep 24 14:47:30 2020"
}
```

# Credit

This repository was originally from http://www.sandtable.com/using-ssl-with-grpc-in-python/

