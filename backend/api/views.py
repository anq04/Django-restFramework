from dataclasses import fields
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse
from products.models import Product
# Create your views here.
def api_home(request, *args, **kwargs):
   model_data=Product.objects.all().order_by("?").first()
   data={}
   if model_data:
    data=model_to_dict(model_data, fields['title','content'])
#     json_datastr=json.dumps(data)
# #     data["title"]=Product.title
# #     data['content']=Product.content
# #     data['price']=Product.price
#    return HttpResponse(json_datastr,headers={"content-type":"application/json"})
    return JsonResponse(data)