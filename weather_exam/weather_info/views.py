from django.shortcuts import render
import requests
from weather_info.models import History

# Create your views here.

def get_site(request):
    q = request.GET.get('q')
    api_key = 'e1408599974bfafd4add9fe2282cd73e'
    city = f'{q}'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        response = requests.get(url)
        data = response.json()

        temperature = data['main']['temp']
        if q:
            history_entry = History.objects.create(country=q, temperature=temperature)
            history_entry.save()
        return render(request, template_name='base.html', context={'temperature': temperature, 'city': city})

    except requests.exceptions.RequestException as e:
        return render(request, template_name='base.html', context={'error': str(e)})

def history_search(request):
    data = History.objects.all()
    print(data)
    return render(request, template_name='history.html',context= {'history_of_weather':data})