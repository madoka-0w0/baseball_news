class BaseResponse:
    def __init__(self, speech_text, should_end_session, session_attributes=None):
        self.response = {
            'version': '1.0',
            'sessionAttributes': session_attributes,
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': speech_text
                },
                'shouldEndSession': should_end_session,
            },
        }


class AlexaHandler:
    def __init__(self, help_message):
        self.help_message = help_message

    def lambda_handler(self, event, context):
        request = event['request']
        request_type = request['type']

        if request_type == 'LaunchRequest':
            return self.help()
        elif request_type == 'IntentRequest':
            return self.on_intent(request, event['session'])

    def on_intent(self, intent_request, session):
        intent = intent_request['intent']
        intent_name = intent['name']

        if intent_name in {'AMAZON.CancelIntent', 'AMAZON.StopIntent'}:
            return self.stop()

        elif intent_name == 'AMAZON.HelpIntent':
            return self.help()

    def stop(self):
        return self.emit("")

    def help(self):
        return BaseResponse(self.help_message, False).response

    def emit(self, speech_text):
        return BaseResponse(speech_text, True).response
