import time
import hashlib
import hmac
import base64
from src.models.base import NCloudCredential


class Singleton:
    def __init__(self, credential: NCloudCredential, **params):
        self.timestamp = str(int(time.time() * 1000))
        self.credential = credential
    
    def build_signature(self):
        pass
    
    def query(self):
        pass

def	make_signature():
	access_key = "{accessKey}"				# access key id (from portal or sub account)
	secret_key = "{secretKey}"				# secret key (from portal or sub account)
	secret_key = bytes(secret_key, 'UTF-8')

	method = "GET"
	uri = "/photos/puppy.jpg?query1=&query2"

	message = method + " " + uri + "\n" + self.timestamp + "\n" + access_key
	message = bytes(message, 'UTF-8')
	signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
	return signingKey