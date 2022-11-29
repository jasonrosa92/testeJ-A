# -*- coding: utf-8 -*-

from django.urls import include, re_path
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('jea.apps.base.urls')),
    re_path(r'^login/', include('jea.apps.login.urls')),
    re_path(r'^cadastro/', include('jea.apps.cadastro.urls')),
    re_path(r'^vendas/', include('jea.apps.vendas.urls')),
    re_path(r'^estoque/', include('jea.apps.estoque.urls')),
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)