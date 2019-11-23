




from django.shortcuts import render
from django.shortcuts import redirect

from .forms import Client
from .models import Client

def add_client(request):
	if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_clients")
        
	else:
        form = ClientForm()
    return render(request,"add_client.html",{"form":form})

# Create your views here.
