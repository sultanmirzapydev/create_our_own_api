
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from get_data.api_logic import call_api
from django.template import loader
from get_data.models import DataModel
from django.core.paginator import Paginator
from .models import DataModel


def do_show(request):

    if request.method == "GET":
        col_names = [col.name for col in DataModel._meta.fields] 
        dataset = DataModel.objects.all().values()
        dataset = aggregate(dataset)
        paginator = Paginator(list(dataset), 100) 
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        template = loader.get_template('./get_data/show.html') 
        return HttpResponse(template.render({"dataset": page_obj,'columns': col_names}))  
    return render(request, './get_data/show_loading.html', )


def aggregate(dataset):
    dataset = list(dataset)
    for idx, item in enumerate(dataset):
        co_name = item['ercs'] 
        
        for loc, value in enumerate(dataset[idx+1:]):
            
            if co_name == value['ercs']:
                for i in item:
                    if type(item[i]) == str:
                        continue
                    if type(item[i]) == type(None):
                        continue
                    if type(value[i]) == type(None):
                        continue
                    
                    item[i] += value[i]
                   
                try:
                    dataset.pop(loc)
                except:
                    print(len(dataset))
    return dataset


            







    