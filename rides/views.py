from django.shortcuts import redirect, render

from .models import Person

# relative import of forms
from .forms import RideForm, NewRideForm

# Create your views here.


def index(request):

  context = {}

  if "search" in request.GET:
    search = request.GET["search"]

    context["people"] = Person.objects.filter(
        origination__icontains=search) | Person.objects.filter(destination_city__icontains=search)

  context["form"] = RideForm()
  context["new_ride_form"] = NewRideForm()

  return render(request, "index_view.html", context)


def create(request):
  context = {}
  context["new_ride_form"] = NewRideForm()

  if request.method == "POST":
    new_ride = NewRideForm(request.POST)
    new_ride.save()
    return redirect("/rides")

  return render(request, "create_new.html", context)
