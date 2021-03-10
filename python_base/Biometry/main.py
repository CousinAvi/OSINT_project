import json
import requests
import base64


class Biometry:
	def __init__(self, image):
		self.image = image
		self.x_authorization_token = "YOUR_TOKEN_HERE"
		self.url = "https://search4faces.com/api/json-rpc/v1"
		self.headers = {'content-type': 'application/json', "x-authorization-token":"YOUR_TOKEN_HERE"}

	def detectFaces(self, image_base64):
		payload = {
			"jsonrpc": "2.0",
			"method": "detectFaces",
			"id": "some-id",
			"params": {"image": image_base64}
			}

		return requests.post(self.url, data=json.dumps(payload), headers=self.headers)

	def main(self):
		image_base64 = base64.b64encode(self.image)
		r = self.detectFaces(image_base64.decode("utf-8"))
		if len(r.json()["result"]["faces"]) == 0:
			return None
		face = r.json()["result"]["faces"][0]
		image_url = r.json()["result"]["image"]

		payload = {
			"jsonrpc": "2.0",
			"method": "searchFace",
			"id": "some-id",
			"params": {
				"image": image_url,
				"face": face,
				"source": "vkok_avatar",
				"results": "20"
				}
			}

		return requests.post(self.url, data=json.dumps(payload), headers=self.headers)
