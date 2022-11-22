from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('search_result/', views.search_result, name='blog-search_result'),
    path('single_post/', views.single_post, name='blog-single_post'),
    path('category/', views.category, name='blog-category'),
    path('login/', views.login_view, name='login'),
    # path('//', views.redirect_view, name='redirect_view'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]
