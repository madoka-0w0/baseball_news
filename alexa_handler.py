from alexa.alexa_listener import AlexaListener


def lambda_handler(event, context):
    return AlexaListener().lambda_handler(event, context)
