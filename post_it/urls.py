"""post_it URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from core import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='core-home'),
    path('profile/', views.profile, name='core-profile'),
    path('post/<int:pk>', views.post, name='core-post'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('createpost/', views.post_new, name='post_new'),
    path('post/vote/<int:pk>', views.vote_on_post, name='core-post-vote'),
    path(
        'post/<int:pk>/createcomment/',
        views.create_comment,
        name='create_comment')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
