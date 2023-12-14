import json

from neo4j import Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import Credentials
from botocore.auth import (
  SigV4Auth,
  _host_from_url,
)

import boto3

SCHEME = "basic"
REALM = "realm"
SERVICE_NAME = "neptune-db"
DUMMY_USERNAME = "username"
HTTP_METHOD_HDR = "HttpMethod"
HTTP_METHOD = "GET"
AUTHORIZATION = "Authorization"
X_AMZ_DATE = "X-Amz-Date"
X_AMZ_SECURITY_TOKEN = "X-Amz-Security-Token"
HOST = "Host"


class NeptuneAuthToken(Auth):
  def __init__(
    self,
    region: str,
    url: str,
    **parameters
  ):
    


    print(region, "received region", " ")
    print(url, "recieved url", " ")
    
    credentials = boto3.Session().get_credentials()

    credentials = Credentials(access_key=credentials.access_key, secret_key=credentials.secret_key, token=credentials.token)

    print(credentials.access_key, credentials.secert_key, credentials.token)

    # Do NOT add "/opencypher" in the line below if you're using an engine version older than 1.2.0.0
    request = AWSRequest(method=HTTP_METHOD, url= url + "/opencypher")

    print(request,"before header")

    request.headers.add_header("Host", _host_from_url(request.url))

    print(request, "after header")

    sigv4 = SigV4Auth(credentials, SERVICE_NAME, region)
    print(sigv4, "initalised correctly")
    sigv4.add_auth(request)
    print(sigv4, "requests added nicely.")
  

    auth_obj = {
      hdr: request.headers[hdr]
      for hdr in [AUTHORIZATION, X_AMZ_DATE, X_AMZ_SECURITY_TOKEN, HOST]
    }

    print(auth_obj, "reached to auth obj")


    auth_obj[HTTP_METHOD_HDR] = request.method
    creds: str = json.dumps(auth_obj)
    super().__init__(SCHEME, DUMMY_USERNAME, creds, REALM, **parameters) 