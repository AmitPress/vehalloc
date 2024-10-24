from pydantic_settings import BaseSettings

class EnvironmentVariables(BaseSettings):
    MONGO_USER : str
    MONGO_PASS : str
    CONNECTION_STRING : str
    DB_NAME : str
    REDIS_HOST : str
    class Config:
        env_file = '.env'
        extra    = 'ignore'

env = EnvironmentVariables()