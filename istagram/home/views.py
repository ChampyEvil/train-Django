from django.shortcuts import render

# Create your views here.
def home(request):
    data = {"greeting": "ว่าไง"}
    data["price"] = 3000
    return render(request, "home.html", data)