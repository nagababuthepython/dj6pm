from django.conf.urls import include,url
from django.contrib import  admin
from tempapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$',views.home)

]
