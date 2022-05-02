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
@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('article.html',title= title,articles = articles)