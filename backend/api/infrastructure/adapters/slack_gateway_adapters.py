from api.application.ports import SlackGateway


class SlackGatewayAdapter(SlackGateway):

    def notify_about_winning_auction(self, auction_id: int, winner_id: int) -> None:
        pass
