#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Global Imports
import uuid

# Django Imports
from django.db import models


class Members(models.Model):

    CHOICE_ROLE = (
        (1, 'Admin'),
        (2, 'Regular')
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField()
    role = models.PositiveSmallIntegerField(choices=CHOICE_ROLE)

    class Meta:
        db_table = "db_member"
        app_label = "members"
        verbose_name = "Member"
