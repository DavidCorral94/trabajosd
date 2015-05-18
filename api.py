from flask import *
from twitter import *
import facebook


app = Flask(__name__)

@app.route("/buscar", methods=['POST'])
def buscar():
	termino = request.form['text'] 
	
	OAUTH_TOKEN = '3109989214-bMXrg7waapFhXJvhgCQv5nNlgD6Pw4LzR5zZf0V'
	OAUTH_TOKEN_SECRET = '5IlN7XgSBbqFOVnllyxhjWhadiTWKBj16kPNQmdZGwJe5'
	CONSUMER_KEY = 'ZnmCputaOKC95ipb99ew2S2ql'
	CONSUMER_SECRET = 'A3tdzlBPCJITNUcAJiDKxHIEWdTr2Mo8KWWIhZ3KzkDUntYWrf'
	t = Twitter(auth=OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET))
	t.statuses.update(status=termino)
	s = 'Acabas de  twittear: ' + termino
	cfg = {
    "page_id"      : "1835871383304661",  # Step 1
    "access_token" : "CAAIZCf3kySroBANLlNmK07nQZBxqbUgZBijGpWZAM0IePpqtiQWbohRCl0AmZA1lAhxNjAHQZBMEon8o2GBxOszh2nAZCwxWFhUaCTzlXwBLBkwlkgrfKZAiT4rc0vZBtnkklZAep52rDrkZCmR4fWD5VBNhWJRZAF4udmZCJQ95K8T3gtqFHe3H4vaofQZBQDY4wIWfZALAG1RPZABHs2Akpomi2DBrSHMLC4SMLHYZD"   # Step 3
    }

	api = get_api(cfg)
	msg = termino
	status = api.put_wall_post(msg)
	return s 

def get_api(cfg):
	graph = facebook.GraphAPI(cfg['access_token'])
	# Get page token to post as the page. You can skip 
	# the following if you want to post as yourself. 
	resp = graph.get_object('me/accounts')
	page_access_token = 'access_token'
	for page in resp['data']:
		if page['id'] == cfg['page_id']:
			page_access_token = page['access_token']
	graph = facebook.GraphAPI(page_access_token)
	return graph

@app.route("/twittear", methods=['POST'])
def twittear():
	termino = request.form['textT'] 
	
	OAUTH_TOKEN = '3109989214-bMXrg7waapFhXJvhgCQv5nNlgD6Pw4LzR5zZf0V'
	OAUTH_TOKEN_SECRET = '5IlN7XgSBbqFOVnllyxhjWhadiTWKBj16kPNQmdZGwJe5'
	CONSUMER_KEY = 'ZnmCputaOKC95ipb99ew2S2ql'
	CONSUMER_SECRET = 'A3tdzlBPCJITNUcAJiDKxHIEWdTr2Mo8KWWIhZ3KzkDUntYWrf'
	t = Twitter(auth=OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET))
	t.statuses.update(status=termino)
	s = 'Acabas de  twittear: ' + termino
	return s

@app.route("/pubFacebook", methods=['POST'])
def pubFacebook():
	termino = request.form['textF']

	cfg = {
    "page_id"      : "1835871383304661",  # Step 1
    "access_token" : "CAAIZCf3kySroBANLlNmK07nQZBxqbUgZBijGpWZAM0IePpqtiQWbohRCl0AmZA1lAhxNjAHQZBMEon8o2GBxOszh2nAZCwxWFhUaCTzlXwBLBkwlkgrfKZAiT4rc0vZBtnkklZAep52rDrkZCmR4fWD5VBNhWJRZAF4udmZCJQ95K8T3gtqFHe3H4vaofQZBQDY4wIWfZALAG1RPZABHs2Akpomi2DBrSHMLC4SMLHYZD" # Step 3
    }

	api = get_api(cfg)
	msg = termino
	status = api.put_wall_post(msg)
	s = 'Acabas de publicar en facebook: ' + termino
	return s

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
