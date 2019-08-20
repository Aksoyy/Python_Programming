# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from app.request.models import Request
from django.http import HttpResponse
from rest_framework import serializers
from app.request.serializers import RequestSerializer
from django.contrib.auth.models import User
import requests


class UserView():
    def get( self, request, *args, **kwargs):
        link_="https://randomuser.me/api/?results=200"
        response = requests.get(link_)
        if response.ok:
            response = response.json()
            results = response.get("results")
            for result in results:
                username = result["name"]["first"]
                lastname = result["name"]["last"]
                Request.objects.create(
                    name = username,
                    lastname = lastname
                )
        return HttpResponse("Created User")

    # def post(self, request, *args, **kwargs):
    #     DATA=[]
    #     DATA.append(
    #         Request(
    #             name = username,
    #             lastname = lastname
    #         )
    #     )
    #     Request.objects.bulk_create(DATA)
    #     serializer = Request(DATA,many=True)
    #     return HttpResponse(serializer.data,status=201)
