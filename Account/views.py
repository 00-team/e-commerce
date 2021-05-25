from django.shortcuts import render

from django.http import JsonResponse

def account(r):
    return JsonResponse({"Account":"Acc"})
