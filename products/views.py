#from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View

from products.models import Owner, Dog

class ownersview(View):
    def post(self, request):
        data    = json.loads(request.body) #py과 js의 다른 언어를 json 형태로 변환해준다.
                 
        owner   = Owner.objects.create(
            name    = data['name'],#owner라는 값을 가진 키를 가져오겠다.
            email   = data['email'],
            age     = data['owner_age'],
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)
    
    def get(self, request):
        products = Owner.objects.all()
        results = []
        for owner in products:
            results.append(
                {
                    "name"      : owner.name,
                    "email"     : owner.email,
                    "owner_age" : owner.age,
                }
            )
        return JsonResponse({'results':results}, status=200)

class dogsview(View):
    def post(self, request):
        data    = json.loads(request.body)

        dog     = Dog.objects.create(
            name    = data['name'],
            age     = data['dog_age'],
            owner_id   = data['owner_id']
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        products = Dog.objects.all()
        results = []
        for dog in products:
            results.append(
                {
                    "dog"       :dog.name,
                    "dog_age"   :dog.age,
                    "owner"     :dog.owner.name,
                }
            )
        return JsonResponse({'results':results}, status=200)