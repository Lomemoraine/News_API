import urllib.request,json
# from app import app
from .models import Source,Articles

#getting the api key
api_key = None

#getting the news base url
base_url = None
#getting the articlces url
articles_url = None




def configure_request(app):
	global api_key,base_url,articles_url
	api_key = app.config['NEWS_API_KEY']
	base_url = app.config['NEWS_API_BASE_URL']
	articles_url = app.config['ARTICLES_BASE_URL']
pass
def get_sources(category):
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = base_url.format(category,api_key)
	# print(get_sources_url,api_key)
 

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)
        

	return sources_results
	
def process_sources(sources_list):
	'''
	Function that processes the news sources results and turns them into a list of objects
	Args:
		sources_list: A list of dictionaries that contain sources details
	Returns:
		sources_results: A list of sources objects
	'''
	sources_results = []

	for source_item in sources_list:
		id = source_item.get('id') 
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')
		language = source_item.get('language')
		country = source_item.get('country')


		sources_object = Source(id,name,description,url,category,country,language)
		# print(sources_object)
		sources_results.append(sources_object)
    	


	return sources_results
def get_articles(source_name):
	'''
	Function that processes the articles and returns a list of articles objects
	'''
	get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(source_name,api_key)
	print(get_articles_url)
	with urllib.request.urlopen(get_articles_url) as url:
		get_data = url.read()
		get_response = json.loads(get_data)

         
		results = None
		if get_response['articles']:
			results_list = get_response['articles']
			results = process_articles(results_list)
	return results
	
def process_articles(articles_list):
	'''
	'''
	articles_object = []
	for article in articles_list:
		id = article.get('id')
		author = article.get('author')
		title = article.get('title')
		description = article.get('description')
		url = article.get('url')
		urlToImage = article.get('urlToImage')
		publishedAt = article.get('publishedAt')
        
		
		if urlToImage:
			articles_result = Articles(id,author,title,description,url,urlToImage,publishedAt)
			articles_object.append(articles_result)	
			print(articles_object)
		

		return articles_object
def search_article(article):
    search_article_url = 'https://newsapi.org/v2/everything?q={}&from=2022-04-30&language=en&sortBy=publishedAt&apiKey={}'.format(article,api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_articles(search_article_list)
    return search_article_list

