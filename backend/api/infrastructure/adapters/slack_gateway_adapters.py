from api.application.ports import SlackGateway
from django.conf import settings

from slack_sdk import WebClient

from slack_sdk.errors import SlackApiError

class SlackGatewayAdapter(SlackGateway):
    def notify_user(self, email: str, msg: str) -> bool:
        users = []
        try:
            self.client = WebClient(token=settings.SLACK_API_TOKEN)
            response = self.client.users_list()
            users = response["members"]
        except Exception as e:
            return False
        flag = 0
        for user in users:
            if 'email' in user['profile'] and email == user['profile']['email'] and flag == 0:
                flag = 1
                try:
                    response = self.client.chat_postMessage(
                        channel=user['id'],
                        text=msg
                        )
                except SlackApiError as e:
                    return False
        if flag == 1:
            return True
        else:
            return False
