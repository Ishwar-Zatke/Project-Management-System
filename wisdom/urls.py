from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path ('login/',views.login),
    path('viewdata/',views.Viewdata),
    path('Updata/<int:id>/',views.updatedata),
    path('Deldata/<int:id>/',views.deldata),
    path('searchEmp/',views.SearchEmployee),
    path('addData/',views.AddStudent),
    path('studentdata/',views.studentdata)
]
