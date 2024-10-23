from redis import Redis
from conf.settings import env
client = Redis(host=env.REDIS_HOST, port=6379, db=0)