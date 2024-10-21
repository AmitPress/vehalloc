from pydantic_settings import BaseSettings

class EnvironmentVariables(BaseSettings):
    MONGO_USER : str
    MONGO_PASS : str
    CONNECTION_STRING : str
    DB_NAME : str
    class Config:
        env_file = '.env'

env = EnvironmentVariables()