#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# RestFramework Imports
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from members.models import Members


class MemberSerializer(ModelSerializer):

    def validate(self, attrs):
        print(attrs)
        return super(MemberSerializer, self).validate(attrs)

    class Meta:
        model = Members
        fields = ["first_name", "last_name", "phone_number", "email", "role"]


class ReadMemberSerializer(ModelSerializer):
    role = SerializerMethodField()

    def get_role(self, obj):
        return obj.get_role_display()

    class Meta:
        model = Members
        fields = ["id", "first_name", "last_name", "phone_number", "email", "role"]
