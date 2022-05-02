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
@main.route('/sources/<source_name>')
def articles(source_name):
    '''
    view articles page
    '''
    articles = get_articles(source_name)
    
    title = f'Articles | {source_name}'
    return render_template('article.html',title= title,articles = articles)
# @main.route('/article')
# def articles():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     #Getting general news
    
#     articles = get_articles('business')
#     title = "Home _ Welcome to family news Hub"
    
 
#     return render_template('article.html',title = title,articles = articles)