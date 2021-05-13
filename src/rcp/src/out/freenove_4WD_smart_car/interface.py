# rcp: INTERFACE MODULE
# rcp: auto-generated ros foreign interface file
# rcp: do not edit this file

import redis

SERVER_ADDR = "0.0.0.0"
SERVER_PORT = 6379
SERVER_DRDB = 0


class RedisWrapper:
    def __init__(self, host=SERVER_ADDR, port=SERVER_PORT, db=SERVER_DRDB):
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis_pubsub = self._redis.pubsub()

    def publish(self, topic, data):
        return self._redis_pubsub.publish(topic, data)

    def subscribe(self, topic):
        return self._redis_pubsub.subscribe(topic)