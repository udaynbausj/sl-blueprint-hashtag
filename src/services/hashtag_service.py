from src.json import types
from src.configs import redis


def extract_hashtags(text: str):
    hashtags = []
    tag = ""
    is_hash_tag = False
    for char in text:
        if char == '#':
            tag += char
            is_hash_tag = True
        elif char == ' ':
            hashtags.append(tag)
            tag = ""
            is_hash_tag = False
        else:
            if is_hash_tag:
                tag += char
    return hashtags


def process_kafka_message(model: types.TweetModelType):
    print("getting hashtags for tweet-id : %s", model.id)
    hashtags = extract_hashtags(model.text)
    for i in hashtags:
        redis.redis_conn.incr(i, 1)
