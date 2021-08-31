
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from chatApp.views import index
urlpatterns = [ 
    path('',include('accounts.url')),
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('career/',include('career.url')),
    path('successStories/',include('successStories.url')),
    path('tech/', include('techTrend.url')),
    path('api-auth/', include('rest_framework.urls')),
    path('chat/', include('chat.api.urls', namespace='chat')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('alumani/', include('chatApp.url')),
    path('bot/', include('chatBot.url')),
    path('dashboard/',include('profileDashboard.url')),
    path('search/',include('searchAlumni.url')),
    path('forum/',include('disscussionForum.url')),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

