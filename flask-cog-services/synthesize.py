import os, requests, time

# TODO: keep subscribtion key in secrets
class TextToSpeech(object):
    def __init__(self, input_text, voice_font):
        subscription_key = '8b88b34ccbad483bb5e1f30defb01305'
        self.subscription_key = subscription_key
        self.input_text = input_text
        self.voice_font = voice_font
        self.timestr = time.strftime('%Y%m%d-%H%M')
        self.access_token = None

    # This function performs the token exchange.
    def get_token(self):
        fetch_token_url = 'https://westeurope.api.cognitive.microsoft.com/sts/v1.0/issuetoken'
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    # This function calls the TTS endpoint with the access token.
    def save_audio(self):
        constructed_url = 'https://westeurope.tts.speech.microsoft.com/cognitiveservices/v1'
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'ResourceGroup1'
        }
        # Build the SSML request with ElementTree
        # The body must be encoded as UTF-8 to handle non-ascii characters.
        body = '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US"><voice name="{}">{}</voice></speak>'.format(self.voice_font, self.input_text)

        #Send the request
        response = requests.post(constructed_url, headers=headers, data=body)
        
        # Write the response as a wav file for playback. The file is located
        # in the same directory where this sample is run.
        return response.content