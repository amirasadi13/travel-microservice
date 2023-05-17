import json
import threading
from kafka import KafkaConsumer
from flight.callbacks import FlightItemCallbackHandler
from hotel.callbacks import HotelItemCallbackHandler
from users.callbacks import UserItemCallbackHandler

FLIGHT_TOPIC = 'flight_users'
HOTEL_TOPIC = 'hotel_users'
USERS_TOPIC = 'users_users'


class KafkaEvent(threading.Thread):
    def run(self):
        print('Users Consumer Is Running .... ')
        try:
            flight_consumer = KafkaConsumer(FLIGHT_TOPIC, bootstrap_servers=['kafka:29092'])
            hotel_consumer = KafkaConsumer(HOTEL_TOPIC, bootstrap_servers=['kafka:29092'])
            users_consumer = KafkaConsumer(USERS_TOPIC, bootstrap_servers=['kafka:29092'])
            flight_consumer.subscribe([FLIGHT_TOPIC, HOTEL_TOPIC, USERS_TOPIC])

            for message in flight_consumer:
                self.message_handler(message)
            flight_consumer.commit()

            for message in hotel_consumer:
                self.message_handler(message)
            hotel_consumer.commit()

            for message in users_consumer:
                self.message_handler(message)
            users_consumer.commit()

        except Exception as e:
            print(f'Error ---> {e}')

    @staticmethod
    def message_handler(message):
        message_content = json.loads(message.value)
        route_key = message_content['route_key']
        data = message_content['data']
        method = message_content['method']
        if message.topic == FLIGHT_TOPIC:
            FlightItemCallbackHandler(route_key, data, method)
        if message.topic == HOTEL_TOPIC:
            HotelItemCallbackHandler(route_key, data, method)
        if message.topic == USERS_TOPIC:
            UserItemCallbackHandler(route_key, data, method)


