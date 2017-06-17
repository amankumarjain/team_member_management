#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework.routers import SimpleRouter

from members.views import MemberModelViewSet

routers = SimpleRouter()
routers.register("members", MemberModelViewSet, base_name="Members")
