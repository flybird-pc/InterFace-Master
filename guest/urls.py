"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,re_path
from sign import views #导入sign应用views文件


urlpatterns = [
    path('', views.index),  # 添加首页配置路径
    path('admin/', admin.site.urls),
    path('index/',views.index),#添加index/配置路径
    path('accounts/login/',views.index),
    path('home/',views.home),#添加home/配置路径
    path('login_action/',views.login_action),
    path('login_success/',views.login_success),
    path('search_name/',views.search_name),
    path('guest_manage/',views.guest_manage),
    re_path(r'sign_index/(?P<eid>[0-9]+)/$',views.sign_index),
    re_path(r'sign_index_action/(?P<eid>[0-9]+)/$',views.sign_index_action),
    path('logout/',views.logout),
]
handler404 = views.page_not_found
handler500 = views.page_error