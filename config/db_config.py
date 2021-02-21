import json

redis_test = {
    "host": "localhost",
    "port": 6379,
    "password": None,
    # 'db': 0,
    "decode_responses": True,
}

redis_15 = {
    "host": "172.16.16.15",
    "port": 6379,
    "password": "20A3NBVJnWZtNzxumYOz",
    # 'db': 1,
    "decode_responses": True,
}

redis_30 = {
    "host": "172.16.0.30",
    "port": 6379,
    "password": "20A3NBVJnWZtNzxumYOz",
    # 'db': 1,
    "decode_responses": True,
}

aioredis_test = {
    "address": ("localhost", 6379),
    "password": None,
    # "db": 0,
    "encoding": "utf-8",
}

aioredis_15 = {
    "address": ("172.16.16.15", 6379),
    "password": "20A3NBVJnWZtNzxumYOz",
    # "db": 1,
    "encoding": "utf-8",
}
aioredis_30 = {
    "address": ("172.16.0.30", 6379),
    "password": "20A3NBVJnWZtNzxumYOz",
    # "db": 1,
    "encoding": "utf-8",
}

mysql_test = {
    "host": "localhost",
    "port": 3306,
    "user": "wangxin",
    "password": "965213",
    "db": "mysql",
}

kafka_test = {
    "bootstrap_servers": ["kafka01:9092", " kafka02:9092", "kafka03:9092"],
    "value_serializer": lambda m: json.dumps(m).encode("utf8"),
    "key_serializer": str.encode,
}

REDIS_CONF = {
    "test": redis_test,
    "redis15": redis_15,
    "redis30": redis_30,
    "aio_test": aioredis_test,
    "aio_redis15": aioredis_15,
    "aio_redis30": aioredis_30,
}

MYSQL_CONF = {"test": mysql_test}

KAFKA_CONF = {"test": kafka_test}
