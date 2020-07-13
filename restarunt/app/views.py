from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from . models import Product,Order
from .forms import ProductForm
# Create your views here.

def login_view(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		user=authenticate(username=username,password=password)
		if user:
			login(request,user)
		else:
			messages.success(request, "Invalid Credentails")
			return redirect("app:login_template")
	return redirect("/")
def logout_view(request):
	logout(request)
	return redirect("/")
def index(request):
	products = Product.objects.all()
	return render(request,'index.html',{'products':products})
def place_order(request):
	product_id	=	request.POST.get("product_id")
	product		=	Product.objects.get(id=product_id)
	print(product)
	if product:
		quantity	= request.POST.get("quantity")
		pno 		= request.POST.get("pno")
		# print(type(pno))
		if int(quantity)<1:
			return JsonResponse({"message": "Quantity Must be 1 or greater"}, status=400)
		if len(pno)!=10 or pno[0] not in '6789':
			return JsonResponse({"message": "Phone number should have 10 digits and it should start with 9,8,7,6"}, status=400)
		order=Order(product=product,quantity=quantity,user_phone=pno)
		order.save()
		return JsonResponse({"message": "success"}, status=200)
	else:
		return JsonResponse({"message": "Product Not Found"}, status=400)

	return redirect("/")
@user_passes_test(lambda u: u.is_superuser)
def settings_(request):
	ordered_orders = Order.objects.all().filter(status="Ordered")
	completed_orders = Order.objects.all().filter(status="Deliveried")
	return render(request,'settings.html',{'ordered_orders':ordered_orders,'completed_orders':completed_orders})
@user_passes_test(lambda u: u.is_superuser)
def delivery_order(request,id):
	item=Order.objects.get(id=id)
	if item:
		item.status="Deliveried"
		item.save()
	return redirect('app:settings')

@user_passes_test(lambda u: u.is_superuser)
def items_(request):
    items=Product.objects.all()
    return render(request,'items.html',{'items':items})
@user_passes_test(lambda u: u.is_superuser)
def create_item(request):
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            about=form.save()
            return redirect('app:items_')
    else:
        form=ProductForm()
    return render(request,'create.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def update_item(request,pk):
    instance=Product.objects.get(id=pk)
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            about=form.save()
            return redirect('app:items_')
    else:
        form=ProductForm(instance=instance)
    return render(request,'create.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def delete_item(request,pk):
    instance=Product.objects.get(id=pk)
    if request.method=="POST":
        instance.delete()
        return redirect('app:items_')
    return render(request,'confirm.html',{'instance':instance,'back_url':reverse('app:items_')})