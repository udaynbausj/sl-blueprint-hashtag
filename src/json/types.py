from pydantic import BaseModel


class TweetModelType(BaseModel):
    id: int
    text: str
    userId: int
    client_type: str
    parent_tweet_id: int
    region_id: int
    status: int
