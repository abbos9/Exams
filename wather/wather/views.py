from django.shortcuts import render
from wather.models import history
import requests
# Create your views here.
def index(request):
    q = request.GET.get('q')
    api_key = 'e1408599974bfafd4add9fe2282cd73e'
    city = f'{q}'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        response = requests.get(url)
        data = response.json()

        temperature = data['main']['temp']
        if q:
            history_entry = history.objects.create(title=q, temprature=temperature)
            history_entry.save()
        return render(request, template_name='index.html', context={'temperature': temperature, 'city': city})

    except requests.exceptions.RequestException as e:
        return render(request, template_name='index.html', context={'error': str(e)})

def history_search(request):
    date = history.objects.all()
    return render(request, template_name='history.html', context={'history':date})