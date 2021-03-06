"""OKFSsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from home.views import home_view,about_view,photo_gallery_view,home2_view,contact_form
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
	path('', home_view, name='home'),
    path('about/',about_view, name='about'),
    path('gallery/', photo_gallery_view, name='gallery'),
    path('home/', home2_view, name='home2'),
    path('contact/', contact_form, name='contact'),
    path('admin/', admin.site.urls),
    path('Elibrary/', include('Elibrary.urls')),
    path('SRMS/', include('SRMS.urls')),
    path('TMS/', include('TMS.urls')),
    path('Payments/', include('Payments.urls')),
    path('Admission/', include('Admission.urls')),
]