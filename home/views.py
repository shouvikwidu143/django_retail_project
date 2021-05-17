from django.shortcuts import redirect, render, HttpResponse
from .controllers import *

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        json_data = fetch_json_from_api("https://jsonplaceholder.typicode.com/todos?userId=1")
        context = {
            # "json_data" : json_data,
            "title": "Home"
        }
        return render(request, "home/index.html", context)
    else:
        return redirect('products')
