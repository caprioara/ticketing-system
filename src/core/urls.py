from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm


from . import views

urlpatterns = [
    path('ticket/', include('ticket.urls', namespace='ticket')),
    path('account/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),

    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html",
                                                authentication_form=UserLoginForm), name='login'),

    path('admin/', admin.site.urls),
]
