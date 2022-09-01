from types import LambdaType
from aws_lambda_typing import context as context_, events
from aws_lambda_typing import *


def lambda_handler(
    event: events.APIGatewayProxyEventV2,
    context: context_.Context
) -> dict:
    message = "Hello {} {}!".format(event["first_name"], event["last_name"])
    print(context.get_remaining_time_in_millis())
    return {"message": message}
