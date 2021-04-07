from confluent_kafka import Consumer, KafkaError, KafkaException


def consume_tweet_events(consumer: Consumer, topic: str):
    try:
        consumer.subscribe(topic)
        while True:
            msg = consumer.poll()

            if msg.error() == KafkaError:
                print("kafka-error while consuming events. closing consumer. err : %s", msg.error())
                raise KafkaException(msg.error())
            elif msg is None:
                continue
            else:
                print("got kafka event : %s", msg)

    except Exception as e:
        print("error while consuming events. err : %s", e)
    finally:
        consumer.close()
