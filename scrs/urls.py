
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .settings import MEDIA_ROOT,MEDIA_URL
urlpatterns = [
    path('admin/', admin.site.urls),

]
urlpatterns+= static(MEDIA_URL, document_root=MEDIA_ROOT)#biz buni nastroyki(settings)ga jalgadiq biraq sayttin o'zine qosiw ushin kk
