"""
URL configuration for finance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import (handler400,handler404,handler500)
# from .views import current_user
# from .views import handle_404

# handler400 = 'django.views.defaults.bad_request'
# handler404 = 'django.views.defaults.page_not_found'
# handler400 = 'django.views.defaults.server_error'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('exchangerates/', include('exchangerates.urls')),
    path('fininfos/', include('fininfos.urls')),
    path('api/v1/', include('articles.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('profile/', include('accounts.urls')),
    # path('api/current_user/', current_user),
]
# handler404 = handle_404