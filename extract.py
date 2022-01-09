import requests

subscription_key = "1eb8442bd80c4f52a04a578621c3750b"
base_url = "https://pictext.cognitiveservices.azure.com/"

def extractTextFromImage(image):
	path = "vision/v3.2/ocr"
	headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
	params = {'language': 'unk', 'detectOrientation': 'true'}
	constructed_url = base_url + path
	image_data = image.read()
	response = requests.post(constructed_url, headers=headers, params=params, data=image_data)
		
	return response.content