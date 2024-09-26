from django.shortcuts import render
from datetime import datetime
import requests
from .forms import ContactForm
from .models import Contact


def home(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    api_url = "https://dummyjson.com/quotes/1"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()  
    except requests.exceptions.HTTPError as http_err:
        data = {"error": f"HTTP error occurred: {http_err}"}  
    except requests.exceptions.RequestException as req_err:
        data = {"error": f"Request error occurred: {req_err}"} 
    
    form = ContactForm()   
    
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Bind data to the form
        if form.is_valid():
           form.save()
           return render(request, 'success.html') 
             
        
    context = {
        'current_time': current_time,
        'data':data,
        'form': form 
    }
    return render(request, 'index.html', context)