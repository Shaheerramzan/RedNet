"""RedNet URL Configuration

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
from django.urls import path, include
from Chat import urls as chat_url
from ConveyanceProvider import urls as conveyance_provider_url
from Donor import urls as donor_url
from Person import urls as person_url
from ReportProblem import urls as report_problem_url
from Society import urls as society_url
from SuperAdmin import urls as super_admin_url
from SocietyAdmin import urls as society_admin_url
from History import urls as history_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/', include('Person.urls')),
    path('chat/', include('Chat.urls')),
    path('conveyance_provider/', include('ConveyanceProvider.urls')),
    path('donor/', include('Donor.urls')),
    path('history/', include('History.urls')),
    path('report_problem/', include('ReportProblem.urls')),
    path('society/', include('Society.urls')),
    path('society_admin/', include('SocietyAdmin.urls')),
    path('super_admin/', include('SuperAdmin.urls')),
]