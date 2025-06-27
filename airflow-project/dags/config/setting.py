from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Config class from env vars"""
    LOCAL_IMAGE_NAME: str = Field(default='sample-image-v0', description='docker image of dbt project')
    DOCKER_URL: str = Field(default='localhost', description='URL to the docker')
    DOCKER_NETWORK: str = Field(default='proj-tier', description='Network used by the local infa')