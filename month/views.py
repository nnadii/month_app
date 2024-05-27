from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Month


# Create your views here.


# app_settings_func = {
#     "january": "Eat no meat for the entire month!",
#     "febuary": "Walk for at least 20 minutes every day!",
#     "march": "Learn Django for at least 20 minutes every day!",
#     "april": "Eat no meat for the entire month!",
#     "may": "Walk for at least 20 minutes every day!",
#     "june": "Learn Django for at least 20 minutes every day!",
#     "july": "Eat no meat for the entire month!",
#     "august": "Walk for at least 20 minutes every day!",
#     "september": "Learn Django for at least 20 minutes every day!",
#     "october": "Eat no meat for the entire month!",
#     "november": "Walk for at least 20 minutes every day!",
#     "december": "Eat no meat for the entire month!"
# }

# Create your views here.


def index(request):
    all_months = Month.objects.all()
    months = list(all_months)
    return render(request, "month/index.html", {"months": months})


def app_settings_with_number(request, app):
    all_months = Month.objects.all()
    application_month = list(all_months)

    if app > len(application_month):
        return HttpResponseNotFound("<h2>Invalid month</h2>")

    redirect_app = application_month[app - 1]
    redirect_path = reverse("app_challenge", args=[redirect_app])
    return HttpResponseRedirect(redirect_path)


def app_settings(request, app):
    all_months = Month.objects.all()
    try:
        challenge_text = all_months[app]
        return render(request, "month/app.html", {
            "text": challenge_text,
            "month": app.capitalize()
        })
    except:
        return HttpResponseNotFound("<h2>This app is not found!</h2>")
