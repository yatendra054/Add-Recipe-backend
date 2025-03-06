from django.contrib import admin
from django.urls import path
from home.views import *
from recepe.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("", home ,name="home"),
    path("recepies/", recepies ,name="recepies"),
    
    path("delete_recepie/<id>/", delete_recepie ,name="delete_recepie"),
    path("update_recepie/<id>/", update_recepie, name="update_recepie"),
    
    path("login/", login_page ,name = "login_page"),
    path("logout/",logout_page,name="logout_page"),
    
    path("register/",register,name="register"),
    
    path("admin/", admin.site.urls),
    path("profile/",profile,name="profile"),
    path("About/",About,name="About"),
    path("forget/",forget,name="forget"),
    path("breakfast/",breakfast,name="breakfast"),
    
    path("lunch/",lunch,name="lunch"),
    
    path("dinner/",dinner,name="dinner"),
    
    path("connect/",connect,name="connect")
    
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
    
urlpatterns +=staticfiles_urlpatterns()