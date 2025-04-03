from django.shortcuts import render
from . models import *

# Create your views here.
def item_list(request):
    items = Item.objects.all()
    
    date_filter = request.GET.get('date', None)
    order = request.GET.get('order', None)
    
    if date_filter:
        items = items.filter(created_at__gte=date_filter)
    
    if order == 'created_at':
        items = items.order_by('created_at')
    elif order == '-created_at':
        items = items.order_by('-created_at')
    
    return render(request, 'items_list.html', {'items': items, 'date_filter': date_filter, 'order': order})