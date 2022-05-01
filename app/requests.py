import urllib.request,json
# from app import app
from .models import Source

#getting the api key
api_key = None

#getting the news base url
base_url = None




def configure_request(app):
	global api_key,base_url
	api_key = app.config['NEWS_API_KEY']
	base_url = app.config['NEWS_API_BASE_URL']
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
