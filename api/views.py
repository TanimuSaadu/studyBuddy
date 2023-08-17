import json
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.forms.models import model_to_dict
from products.models import Product

from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
    

# @api_view(["POST"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View
#     """
#     data = request.data
#     return Response(data)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View
#     """
#     # if request.method != "POST":
#     #     return Response({'detail': "GET not allowed"}, status=405)
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return JsonResponse(data)


# def api_home(request, *args, **kwargs):
#     print(request.GET)

#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)