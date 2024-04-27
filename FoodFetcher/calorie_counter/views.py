from django.shortcuts import render
import requests, os, json


def homepage(request):
    if request.method == "POST":
        query = request.POST['query']

        api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
        api_key = os.environ['API_KEY']
        response = requests.get(api_url, headers={'X-Api-Key': api_key})

        try:
            api = json.loads(response.content)
        except Exception as e:
            api = "error"
            print(e)

        return render(request=request, template_name='homepage.html', context={'api': api})

    return render(request=request, template_name='homepage.html', context={'query': 'Enter a valid query'})
