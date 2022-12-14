"""firstpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from greetings import views

from calculator import views as cview
from django.contrib import admin
from django.urls import path
from greetings import views
from calculator import views as cview
from blogapi import views as bview
from mobile.views import mobileviews,mobiledetailsviews
from cloth.views import ClothsView,ClothDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('goodmorning/',views.GoodmorningView.as_view()),
    path('greetings/',views.GreetingsView.as_view()),
    path('operations/add/',cview.AddView.as_view()),
    path('operations/sub/',cview.subView.as_view()),
    path('operations/mul/',cview.mulView.as_view()),
    path('operations/fact/', cview.facView.as_view()),
    path('social/post/', bview.postView.as_view()),
    path("social/post/<int:pid>",bview.PostDetailview.as_view()),
    path("api/v1/mobiles",mobileviews.as_view()),
    path("api/v1/mobiles/<int:qs>",mobiledetailsviews.as_view()),
    path("api/cloth",ClothsView.as_view()),
    path("api/cloth/<int:id>",ClothDetailView.as_view())
]