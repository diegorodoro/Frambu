from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from products.models import Product
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import OrderSerializers, OrderSerializers2
 
# Create your views here.
@login_required
def home(request):
    list=[]
    
    orders = Order.objects.all()
    products = Product.objects.all()
    # orders = Order.objects.all().select_related('client')

    for i in orders:
        total=0
        for j in products:
            if j.name.lower()==str(i.product):
                total=j.price*i.quantityRequested                
        list.append({
            "id":i.pk,
            "client": i.client,
            "product":i.product,
            "created_at":i.created_at,
            "updated_at":i.updated_at,
            "quantityRequested":i.quantityRequested,
            "order_state":i.order_state,
            "total":total
        })
    
    return render(request, 'home.html', {'orders': list,'products':products})
 
@login_required
def order_list(request):
    list=[]
    
    orders = Order.objects.all()
    products = Product.objects.all()
    # orders = Order.objects.all().select_related('client')

    for i in orders:
        total=0
        for j in products:
            if j.name.lower()==str(i.product):
                total=j.price*i.quantityRequested                
        list.append({
            "id":i.pk,
            "client": i.client,
            "product":i.product,
            "created_at":i.created_at,
            "updated_at":i.updated_at,
            "quantityRequested":i.quantityRequested,
            "order_state":i.order_state,
            "total":total
        })
    
    return render(request, 'order_list.html', {'orders': list,'products':products})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    products = Product.objects.all()

    total=0
    for j in products:
        if j.name.lower()==str(order.product):
            total=j.price*order.quantityRequested                
    order={
        "id":order.pk,
        "client": order.client,
        "product":order.product,
        "created_at":order.created_at,
        "updated_at":order.updated_at,
        "quantityRequested":order.quantityRequested,            
        "order_state":order.order_state,
        "total":total
        }

    return render(request, 'order_detail.html', {'order': order})
 
@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})
 
@login_required
def order_update(request):
    orders = Order.objects.all()
    return render(request, 'order_update.html', {'orders': orders})
 
@login_required
def order_updated(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request,'order_form.html', {'form': form})
 
@login_required
def order_delete(request):
    orders = Order.objects.all()
    return render(request, 'order_delete.html', {'orders': orders})
 
@login_required
def order_deleted(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})

class OrderAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def post(self, request, *args, **kwargs):
        try:
            print("Entre")
            order_id = request.data.get('id')
            print(order_id)

            order = Order.objects.get(id=order_id)
            # order.order_state = 'ready'
            # order.save()

            # Actualizar el estado de la orden si está pagada

            if order.is_paid:
                print('esta pagada')
                current_index = [choice[0] for choice in Order.STATE_CHOICES].index(order.order_state)
                print(current_index)
                if current_index < len(Order.STATE_CHOICES) - 1:
                    next_state = Order.STATE_CHOICES[current_index + 1][0]
                    print(next_state)
                    order.order_state = next_state
                    order.save()
            else:
                print("no esta pagada")
            return Response({"id": order.id, "is_paid": order.is_paid}, status=200)
        except Order.DoesNotExist:
            return
        
class OrderAPIView2(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers2