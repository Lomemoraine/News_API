from flask import render_template
from app import app
from app.requests import get_sources

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting general news
    general_news = get_sources('general')
    print(general_news)
    title = "Home _ Welcome to family news Hub"
    
 
    return render_template('index.html',title = title,general = general_news)