from django.urls import path
from django.views.generic.base import TemplateView
from .views import index,place_order,logout_view,login_view,settings_,delivery_order,items_,create_item,update_item,delete_item

app_name="app"
urlpatterns = [
	path('',index,name="index"),
	path('place_order/',place_order,name="place_order"),
	path('logout/',logout_view,name="logout"),
	path('login/',login_view,name="login"),
	path('login_template/',TemplateView.as_view(template_name="login.html"),name="login_template"),
	path('settings/',settings_,name="settings"),
	path('delivery_order/<int:id>',delivery_order,name="delivery_order"),
	path('items/',items_,name="items_"),
	path('items/create',create_item,name="create_item"),
	path('items/update/<int:pk>',update_item,name="update_item"),
	path('items/delete/<int:pk>',delete_item,name="delete_item"),
]
