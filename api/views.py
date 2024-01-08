from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from base.models import Item

@api_view(['GET'])
def getData(request):
    #userData = {'name':'Moeez', 'age':22}
    #return Response(userData)
    
    items = Item.objects.all()
    serializedItems = ItemSerializer(items, many = True)
    return Response(serializedItems.data)

@api_view(['POST'])
def addItem(request):
    deseralizedItem = ItemSerializer(data = request.data)
    if deseralizedItem.is_valid():
        deseralizedItem.save()
    return Response(deseralizedItem.data)