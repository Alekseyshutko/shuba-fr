import os
# from dotenv import load_dotenv


class Config:
    API_URL = os.getenv("API_URL", "https://shubabackend.herokuapp.com")
    SECRET_KEY = os.getenv("SECRET_KEY")
    BUCKET_NAME = os.getenv("BUCEKT_NAME", "shuba")
    S3_LOCATION = os.getenv("S3_LOCATION", "eu-central-1")
    # DEBUG = False
    # DEVELOPMENT = False
#
# class ProductionConfig(Config):
#     pass
#
# class StagingConfig(Config):
#     DEBUG = True
#
#
# class DevelopmentConfig(Config):
#     DEBUG = True
#     DEVELOPMENT = True
