from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting general news
    general_news = get_sources('general')
    articles = get_articles('business')
    title = "Home _ Welcome to family news Hub"
    
 
    return render_template('index.html',title = title,general = general_news,articles = articles)
@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
   
	title = f'Articles | {id}'

	return render_template('article.html',title= title,articles = articles)
