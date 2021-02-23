from api.application.ports import SlackGateway
import os

from slack import WebClient

from slack.errors import SlackApiError

class SlackGatewayAdapter(SlackGateway):
    def __init__(self):
        self.client = WebClient(token=os.environ["SLACK_API_TOKEN"])
        
    def notify_user(self, email: str, msg: str) -> bool:
        response = client.users_list()
        users = client.users_list()["members"]
        flag = 0
        for user in users:
            if email == user['profile']['email'] and flag == 0:
                flag = 1
                try:
                    response = self.client.chat_postMessage(
                        channel=user['id'],
                        text=msg
                    )
                except SlackApiError as e:
                    assert e.response["error"] 
        if flag == 1:
            return True
        else:
            return False
