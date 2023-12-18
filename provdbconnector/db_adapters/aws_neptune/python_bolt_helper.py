import json

from neo4j import Auth
from botocore.awsrequest import AWSRequest
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


  """
    Provides authentication token for Amazon Neptune using AWS SigV4.

    This class automates the creation of a signed authentication token required by Amazon Neptune
    databases. It takes the AWS region and Neptune database URL, constructs an AWSRequest, and 
    signs it using the SigV4 protocol with the credentials obtained from the boto3 session.

    Arguments:
        region (str): AWS region where the Neptune database is located.
        url (str): URL of the Neptune database.
        **parameters: Additional parameters for the parent Auth class.
    
    Note:
        - This class is designed for Amazon Neptune databases compatible with engine version 1.2.0.0 or newer.
        - Inherits from neo4j.Auth.
  """

  def __init__(
    self,
    region: str,
    url: str,
    **parameters
  ):
    
    
    credentials = boto3.Session().get_credentials()

    # Do NOT add "/opencypher" in the line below if you're using an engine version older than 1.2.0.0
    request = AWSRequest(method=HTTP_METHOD, url= url + "/opencypher")
    request.headers.add_header("Host", _host_from_url(request.url))

    sigv4 = SigV4Auth(credentials, SERVICE_NAME, region)
    sigv4.add_auth(request)
  
    auth_obj = {
      hdr: request.headers[hdr]
      for hdr in [AUTHORIZATION, X_AMZ_DATE, X_AMZ_SECURITY_TOKEN, HOST]
    }

    auth_obj[HTTP_METHOD_HDR] = request.method
    creds: str = json.dumps(auth_obj)
    super().__init__(SCHEME, DUMMY_USERNAME, creds, REALM, **parameters) 