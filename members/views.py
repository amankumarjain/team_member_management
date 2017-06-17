#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework.exceptions import ValidationError
# RestFramework Imports
from rest_framework.viewsets import ModelViewSet

from members.models import Members
from members.serializers import MemberSerializer, ReadMemberSerializer


class MemberModelViewSet(ModelViewSet):

    """
    create:
    **This will create a new member instance**
    >```
    curl -X POST \
    http://127.0.0.1:8000/api/v1/members/ \
    -H 'content-type: application/json' \
    -d '{"first_name":"Aman", "last_name":"Jain", "phone_number":"8867998100", "email":"admin@codersbyte.in", "role": 1}'
    ```

    list:
    **Return a list of all the existing members**
    >```
    curl -X GET \
    http://127.0.0.1:8000/api/v1/members/ \
    -H 'content-type: application/json' \
    ```

    retrieve:
    **Return the given member**
    >```
    curl -X GET \
    http://127.0.0.1:8000/api/v1/members/31376e06-69a5-47fd-b357-b603cbfb9fba/ \
    -H 'content-type: application/json' \
    ```

    update:
    **Update the given member**
    >```
    curl -X PUT \
    http://127.0.0.1:8000/api/v1/members/ \
    -H 'content-type: application/json' \
    -d '{"first_name":"Aman", "last_name":"Jain", "phone_number":"8867998100", "email":"admin@codersbyte.in", "role": 1}'
    ```

    partial_update:
    **Update partial field for given member**
    >```
    curl -X PATCH \
    http://127.0.0.1:8000/api/v1/members/ \
    -H 'content-type: application/json' \
    -d '{"first_name":"Aman", "last_name":"Jain", "phone_number":"8867998100", "email":"admin@codersbyte.in", "role": 1}'
    ```
    """

    serializers = {
        "create": MemberSerializer,
        "list": ReadMemberSerializer,
        "retrieve": ReadMemberSerializer,
        "update": MemberSerializer,
        "partial_update": MemberSerializer
    }

    def get_queryset(self):
        return Members.objects.filter()

    def get_serializer_class(self):
        print(self.action)
        if self.action in self.serializers.keys():
            return self.serializers[self.action]
        else:
            raise ValidationError({"message": "Not Supported"})
