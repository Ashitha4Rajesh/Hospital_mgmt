"""
URL configuration for Hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django .conf import settings
from django.conf.urls.static import static
from blog import views
app_name="blog"
urlpatterns = [
    path('admin/', admin.site.urls),
path("create_post",views.create_post,name="create_post"),
path("view_post",views.view_post,name="view_post"),
path("draft",views.draft,name="draft"),
path('delete/<str:p>',views.delete,name='delete'),
path('delete_draft/<str:p>',views.delete_draft,name='delete_draft'),
path('category_post',views.category_post,name='category_post'),
path('postview/<str:p>',views.postview,name='postview'),
]

