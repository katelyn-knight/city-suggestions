from src.config.dev_config import DevConfig
from src.config.prod_config import ProdConfig


class Config:
    def __init__(self):
        self.dev = DevConfig()
        self.prod = ProdConfig()

    def get_config(self, env):
        if env == 'development':
            return self.dev
        if env == 'production':
            return self.prod
        return self.dev