import pytest

# sys.path.append(os.pardir)
from common.spider import AsyncSpider
from config.db_setup import AioMysql, AioRedis, MysqlClient, RedisClient

pytestmark = pytest.mark.asyncio


async def test_asyncSpider():
    async with AsyncSpider() as spider:
        data = await spider.request("https://python.org")
        if data:
            assert "python" in data.text


def test_redis_client():
    redis_client = RedisClient()
    new_var = "pytest"
    cache_cycle = 60
    redis_client.set_cache(new_var, "test", "test_pytest", cache_cycle=60, refresh=True)
    assert redis_client.exists(new_var) == 1
    assert redis_client.ttl(new_var) == cache_cycle


def test_mysql_client():
    mysql_client = MysqlClient()
    sql = "INSERT INTO birds (name,description) VALUES ('alix minor','wood duck')"
    r = mysql_client.insert_data(sql)
    mysql_client.close()
    assert r is True


async def test_aioredis():
    async with AioRedis() as redis_client:
        await redis_client.set("my_key", "value")
        data = await redis_client.get("my_key")
        assert data == "value"


async def test_conn_aiomysql():
    sql = "CREATE TABLE if not exists fastapi (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),description TEXT)"
    async with AioMysql() as mysql_client:
        r = await mysql_client.create_table(sql)
        assert r is True


if __name__ == "__main__":
    pass
