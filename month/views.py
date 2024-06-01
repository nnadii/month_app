from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Month


# Create your views here.

def index(request):
    all_months = Month.objects.all()
    months = list(all_months)
    return render(request, "month/index.html", {"months": months})


def app_settings_with_number(request, app):
    all_months = Month.objects.all()
    application_month = list(all_months)

    if app > len(application_month):
        return HttpResponseNotFound("<h3>Invalid month</h3>")

    redirect_app = application_month[app - 1]
    redirect_path = reverse("app_challenge", args=[redirect_app])
    return HttpResponseRedirect(redirect_path)


def app_settings(request, app):
    try:
        challenge_text = list(Month.objects.all())
        for month_challenge in challenge_text:
            return render(request, "month/app.html", {
                "text": month_challenge,
                "month": app.capitalize()
            })
    except:
        return HttpResponseNotFound("<h2>This app is not found!</h2>")
