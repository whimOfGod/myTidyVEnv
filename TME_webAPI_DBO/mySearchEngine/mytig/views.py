import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl

# Create your views here.
class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

# Create your views here.
class RedirectionListeDeShippoints(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'shipPoints/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class RedirectionDetailProduit(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

class RedirectionDetailShippoint(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl+'shipPoint'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"



from mytig.models import ProduitEnPromotion
from mytig.serializers import ProduitEnPromotionSerializer
from django.http import Http404
from django.http import JsonResponse

class PromoList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

class RedirectionListeDeIsAvailableProducts(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl + 'products/')
        jsondata = response.json()

#Filtrer les produits avec availability=True
        available_products = [product for product in jsondata if product.get('availability') == True]

        return Response(available_products)
#def post(self, request, format=None):
#NO DEFITION of post --> server will return "405 NOT ALLOWED"
class RedirectionListeDeIsAvailableProduct(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl + 'product/' + str(pk) + '/')
            product_data = response.json()

#Vérifier si le produit est disponible avant de le renvoyer
            if product_data.get('availability') == True:
                return Response(product_data)
            else:
                return Response({'detail': 'Ce produit nest pas disponible.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            raise Http404 