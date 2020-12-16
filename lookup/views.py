from django.shortcuts import render

# Create your views here.
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=11DE9788-D416-4FB1-BB53-328F64013C7B
def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=11DE9788-D416-4FB1-BB53-328F64013C7B")
	
	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error...."

	return render(request,'home.html',{'api': api})

def about(request):
	return render(request,'about.html',{})	