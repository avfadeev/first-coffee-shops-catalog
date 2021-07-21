from django.shortcuts import render, get_object_or_404
from firstapp.models import Coffee

from firstapp.forms import OrderForm


# Create your views here.
def home(request):
    coffees = Coffee.objects.all()
    return render(request, 'index.html', {'coffees': coffees})


def coffee_detailing(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)
    form = OrderForm(initial={
        'coffee': coffee
    })
    return render(request, 'coffee_detailing.html', {
        'coffee': coffee,
        'form': form
    })
