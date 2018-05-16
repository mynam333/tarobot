import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('bot_token', 'NDQ2MjcwNTk4NTE2MzEwMDE3.Dd4oLw.42gJ0sj3OUQ2ywG8RGMo_TufDpA')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue))
        worker.work()
