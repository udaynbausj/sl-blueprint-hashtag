from confluent_kafka import Consumer, KafkaError, KafkaException
from src.constants import constants
from src.services import hashtag_service


def consume_tweet_events(consumer: Consumer):
    try:
        consumer.subscribe(constants.consts.get('tweet_topic'))
        while True:
            msg = consumer.poll()

            if msg.error() == KafkaError:
                print("kafka-error while consuming events. closing consumer. err : %s", msg.error())
                raise KafkaException(msg.error())
            elif msg is None:
                continue
            else:
                print("got kafka event : %s", msg)
                hashtag_service.process_kafka_message(msg)

    except Exception as e:
        print("error while consuming events. err : %s", e)
    finally:
        consumer.close()

