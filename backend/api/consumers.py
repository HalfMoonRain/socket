import json
from channels.generic.websocket import WebsocketConsumer

class ConsumerCls(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Redis를 통해 메시지 전달 등 작업 가능
        self.send(text_data=json.dumps({
            'message': message
        }))