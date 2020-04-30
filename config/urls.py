from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', TemplateView.as_view(template_name="pages/home.html"), name="home")
]
