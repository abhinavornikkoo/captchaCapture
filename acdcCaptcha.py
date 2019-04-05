''' 
version 1.0
Build on Windows platform
By - Abhinav

'''
import requests
import subprocess
import re

def captcha(cookies,headers):
	captcha_url = 'http://results.vtu.ac.in/resultsvitavicbcs_19/captcha_new.php'
	t = requests.get(captcha_url, headers=headers,cookies = cookies)
	with open("capt.png","wb") as f:
		f.write(t.content)
		f.close()
	subprocess.call(['C:\\Program Files\\Tesseract-OCR\\tesseract.exe', 'capt.png', 'output'])
	f = open('output.txt', 'r')
	c = f.read().replace('\n\x0c', '' )
	return c

def getInfo():
	link1 = 'http://results.vtu.ac.in/resultsvitavicbcs_19/resultpage.php'
	headers = {'User-Agent': 'Mozilla/5.0'}
	session = requests.Session()
	resp = session.post(link1, headers = headers)
	cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))
	token = re.findall('[a-zA-Z0-9+/]{142}==', resp.text)
	captain = captcha(cookies,headers)
	usn = '1ay17cs001'
	payload = {'lns': usn,
		'captchacode':captain,
		'token': token,
		'current_url': 'http://results.vtu.ac.in/resultsvitavicbcs_19/index.php'
		}
	resp = session.post(link1, headers=headers,data = payload, cookies = cookies,allow_redirects=True)
	return ([token, captain, cookies,link1])
