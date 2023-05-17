import json
import threading
from kafka import KafkaConsumer
from flight.callbacks import FlightItemCallbackHandler
from hotel.callbacks import HotelItemCallbackHandler

FLIGHT_TOPIC = 'flight_admin'
HOTEL_TOPIC = 'hotel_admin'


class KafkaEvent(threading.Thread):
    def run(self):
        print('Admin Consumer Is Running .... ')
        try:
            flight_consumer = KafkaConsumer(FLIGHT_TOPIC, bootstrap_servers=['kafka:29092'])
            hotel_consumer = KafkaConsumer(HOTEL_TOPIC, bootstrap_servers=['kafka:29092'])
            flight_consumer.subscribe([FLIGHT_TOPIC, HOTEL_TOPIC])

            for message in flight_consumer:
                self.message_handler(message)
            flight_consumer.commit()

            for message in hotel_consumer:
                self.message_handler(message)
            hotel_consumer.commit()
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


