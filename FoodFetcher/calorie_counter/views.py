from django.shortcuts import render
import requests, os


def homepage(request):
    query = 'cum'
    api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
    api_key = os.environ['API_KEY']
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

    return render(request=request, template_name='homepage.html')
