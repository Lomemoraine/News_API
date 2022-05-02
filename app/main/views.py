from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources
#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting general news
    general_news = get_sources('general')
    business_news = get_sources('business')
    title = "Home _ Welcome to family news Hub"
    
 
    return render_template('index.html',title = title,general = general_news,business = business_news)