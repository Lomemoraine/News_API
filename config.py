import os


class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?{}&language=en&from=2022-04-16&apiKey={}'
    
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?category={}&language=en&from=2022-04-16&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
    

 

    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}