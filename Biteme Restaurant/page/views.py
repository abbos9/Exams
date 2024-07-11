from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from page.models import (
    FoodGalleryModel, ReservationModel, SubscribeModel, MenuModel, Comment,
    Events, ChefModel
)
from page.forms import ReservationForm , SubscribeForm

# Create your views here.

# class PAGESLISTVIEW(ListView):
def PageHomeView(request):
    all = FoodGalleryModel.objects.filter(category__name__icontains="all").order_by('-pk')
    desert_first = FoodGalleryModel.objects.filter(category__name__icontains="Desert").order_by('-pk')
    lunch = FoodGalleryModel.objects.filter(category__name__icontains="Lunch").order_by('-pk')
    dinner_first = FoodGalleryModel.objects.filter(category__name__icontains="Dinner").order_by('-pk')
    breakfast = FoodGalleryModel.objects.filter(category__name__icontains="Breakfast").order_by('-pk')
    snack = MenuModel.objects.filter(category__name__icontains="Snacks").order_by('-pk')
    dinner_second = MenuModel.objects.filter(category__name__icontains="Dinner").order_by('-pk')
    desert_second = MenuModel.objects.filter(category__name__icontains="Desert").order_by('-pk')
    fresh_food = MenuModel.objects.filter(category__name__icontains="FreshFood").order_by('-pk')
    popular_dishes = MenuModel.objects.all().order_by("-pk")[:3]
    comment = Comment.objects.all().order_by("-pk")
    event = Events.objects.all().order_by("-pk")
    chef = ChefModel.objects.all().order_by("-pk")
    context = {
        'All': all,
        'deserts': desert_first,
        'lunchs': lunch,
        'dinners': dinner_first,
        'breakfasts': breakfast,
        'snacks': snack,
        'dinner_seconds':dinner_second,
        'desert_seconds': desert_second,
        'fresh_foods':fresh_food,
        'popular': popular_dishes,
        'comments': comment,
        'events': event,
        'chefs': chef,
    }
    return render(request, template_name='index.html', context=context)

class PageReservationView(CreateView):
    model = ReservationModel
    form_class = ReservationForm
    template_name = 'index.html'
    success_url = reverse_lazy('pages:home')


def PageSubscribeView(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            existing_instance = SubscribeModel.objects.filter(email=form.cleaned_data['email']).exists()
            if not existing_instance:
                form.save()
                return redirect('pages:home')
            else:
                return render(request, 'index.html')
    else:
        form = SubscribeForm()

    return render(request, 'index.html')



