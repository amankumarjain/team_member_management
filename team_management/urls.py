#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Default Framework App
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

# Custom App Import
from members.urls import routers as member_routers

urlpatterns = [
    # Register custom urls
    url("^api/v1/", include(member_routers.urls)),
    url(r'^docs/', include_docs_urls(title='Member API Docs'))
]
