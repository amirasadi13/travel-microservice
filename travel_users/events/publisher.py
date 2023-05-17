import json
import os

from django.core.serializers.json import DjangoJSONEncoder
from kafka import KafkaProducer


class EventPublisher:
    def __init__(self):
        self.producer = self.initial_producer()

    @staticmethod
    def initial_producer():
        return KafkaProducer(bootstrap_servers=[os.getenv('KAFKA_SERVER')])

    def get_producer(self):
        return self.producer

    @staticmethod
    def encode_data(method, body, route_key):
        return json.dumps({'data': body,
                           'method': method,
                           'route_key': route_key
                           },
                          cls=DjangoJSONEncoder).encode('utf-8')

    def publish_data(self, method, body, route_key, topic):
        data_encoded = self.encode_data(method, body, route_key)
        try:
            self.producer.send(topic, data_encoded)
        except Exception as e:
            print(str(e))
