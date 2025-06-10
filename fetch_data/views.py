from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from get_data.api_logic import call_api
from django.template import loader
from get_data.models import DataModel
from django.core.paginator import Paginator


def index(request):
    is_show = False
    if request.GET.get('show_btn'):
        print('executed')
        is_show = True 

    template = loader.get_template('./get_data/index.html')
    return HttpResponse(template.render({"is_show":is_show}))

def do_fetch(request):
    if request.method == 'POST':
        # Your Python code here
        returned_value = call_api() 
        if returned_value == False:
            return HttpResponse("Data couldn't be fetched, try providing a valid token")  
        print('done')
        result = "fetching data from api"
        return HttpResponse(result)
    #return render(request, './get_data/show_loading.html') 


 