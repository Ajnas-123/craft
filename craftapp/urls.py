from django.urls import path
from craftapp import views

urlpatterns = [
	path('',views.display),
	path('about/',views.about),
	path('blog/',views.blog),
	path('contact/',views.contact),
	path('login/',views.login),
	path('register/',views.register),
	path('user_login/',views.user_login),
	path('user_register/',views.user_register),
	path('logout/',views.logout),
	path('admin_login/',views.admin_login),
	path('admin_page/',views.admin_page),
	path('admin_logout/',views.admin_logout),
	path('add_product/',views.add_product),
	path('product_details/',views.product_details),
	path('approved_products/',views.approved_products),
	path('rejected_products/',views.rejected_products),
	path('view_product/',views.view_product),
	path('user_details/',views.user_details),
	path('query_details/',views.query_details),
	path('contact_details/',views.contact_details),
	path('single_page/',views.single_page),
	path('review/',views.review),
	path('search/',views.search),
	
	









	
	]
