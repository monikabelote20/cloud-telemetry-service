from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = "cloud-telemetry-service"
    environment: str = Field(default="dev", env="APP_ENV")
    aws_region: str = Field(default="us-east-1", env="AWS_REGION")
    sqs_queue_url: str = Field(default="https://sqs.us-east-1.amazonaws.com/123456789/telemetry-dev", env="SQS_QUEUE_URL")
    batch_size: int = 50
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
