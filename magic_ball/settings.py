import os
from dotenv import load_dotenv


class Configs:

    def __init__(self):
        load_dotenv()
        self.SECRET_KEY = os.getenv('SECRET_KEY')
        self.SESSION_TYPE = os.getenv('SESSION_TYPE')
        self.SESSION_PERMANENT = os.getenv('SESSION_PERMANENT')

    @property
    def secret_key(self):
        return self.SECRET_KEY

    @property
    def session_type(self):
        return self.SESSION_TYPE

    @property
    def session_permanent(self):
        return self.SESSION_PERMANENT
