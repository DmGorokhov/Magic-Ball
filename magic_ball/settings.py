import os
from dotenv import load_dotenv


class Configs:

    def __init__(self):
        load_dotenv()
        self.SECRET_KEY = os.getenv('SECRET_KEY')

    @property
    def secret_key(self):
        return self.SECRET_KEY
