from confluent_kafka import Consumer
import os

config = {
    'bootstrap.server': os.environ.get('kafka_bootstrap_servers'),
    'group.id': os.environ.get('kafka_group_id'),
    'auto.offset.reset': os.environ.get('kafka_auto_offset_reset')
}

consumer = Consumer(config=config)
