from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('moderators/',include('Moderators.urls')),
    #path('experts/', include('Experts.urls')),
    #path('users/', include('Users.urls'))
]
