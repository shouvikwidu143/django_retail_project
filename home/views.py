from django.shortcuts import render, HttpResponse
from .controllers import *

# Create your views here.
def home(request):
    json_data = fetch_json_from_api("https://jsonplaceholder.typicode.com/todos?userId=1")
    context = {
        "json_data" : json_data
    }
    return render(request, "home\index.html", context)
