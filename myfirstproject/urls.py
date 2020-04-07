"""myfirstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, social_view, about_view, contact_view
from products.views import ( product_detial_view,
                             product_create_view,
                             render_initial_data,
                             dynamic_lookup_view,
                             product_list_view
                             )
urlpatterns = [
    path('home/', home_view, name='home'),
    path('about/',about_view, name='about'),
    path('products/',product_list_view, name='product-list'),
    path('product/<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('social/', social_view, name='social'),
    path('create/', render_initial_data, name='create'),
    path('contact/', contact_view, name='conntact'),
    path('admin/', admin.site.urls),
]
