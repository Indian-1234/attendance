"""park URL Configuration

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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from attendance import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),

    path("<str:users>/addnewstaff",views.newstaff),

    path("<str:users>/addstaff",views.addstaffs,),

    path("<str:users>/delete/<int:id>",views.staff_delete),

    path("<str:users>/update/<int:id>",views.staff_update),

    path("<str:users>/departments",views.dep,name="deps"),
    path("<str:users>/studetail",views.studetail,name="studetail"),
    path("admin",views.login,name="admin"),
    path("<str:users>/admin",views.staffviewpage,name="staffviewpage1"),

###################################################################  ihiugiibu   ############
    path("departments",views.login,name="login"),
    path("Logout",views.logout,name="Logout"),
    path("indexhome",views.indexhome,name="il"),
    path("stafflog",views.stafflog,name="la"),
    path("sd",views.sd,name="sd"),
   


####################################################################### home 1 ########################################

    path("",views.institute_login,name="home"),

###################################################################### new college ###################################  

    path("signup",views.signup),


    path("submit",views.submit),
####################################################################

#######################################################################  UPDATE  ###################################

    path("<str:user>/<str:department>/<str:year>/admin/update/<int:id>",views.update),

#############################################################################  DELETE  ##################################

    path("<str:user>/<str:department>/<str:year>/admin/delete/<int:id>",views.delete),

##############################################################################  years ######################################

    path("<str:user>/<str:depart>",views.year),
    
############################################################################## department #################################

    path("<str:user>/<str:department>/<str:year>/",views.department,name="attendance"),
    path("<str:user>/<str:department>/<str:year>/send_attendance/<int:id>",views.send_attendance,name="sendattendance"),


############################################################################## edit #######################################

    path("<str:user>/<str:department>/<str:year>/admin/",views.admin,name="studentAdmin"),
    path("<str:user>/<str:department>/<str:year>/admin/back",views.back),
    
############################################################################## add student ################################

    path("<str:user>/<str:department>/<str:year>/admin/adddata",views.adddata),
    
    path("<str:user>/<str:department>/<str:year>/<str:admin>/newstudent/",views.newstudent,name="newstudent"),

     path("<str:user>/<str:department>/<str:year>/admin/newstudent/adddata",views.adddata),

   

############################################################################ #  attendance #################################
    path("<str:user>/<str:department>/<str:year>/emailsubmit",views.send,name="emailsubmit"),
    path("<str:user>/<str:department>/<str:year>/auto/",views.auto),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
