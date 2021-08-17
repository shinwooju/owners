#from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class ownersview(View):
    def post(self, request):
        data    = json.loads(request.body) #py과 js의 다른 언어를 json 형태로 변환해준다.
                 
        owner   = Owner.objects.create(
            name    = data['name'], #Owner에서 name이라는 값을 가진 키를 가져오겠다.
            email   = data['email'],
            age     = data['owner_age'],
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)
    
    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
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
        owners = Dog.objects.all()
        results = []
        for dog in owners:
            results.append(
                {
                    "dog"       :dog.name,
                    "dog_age"   :dog.age,
                    "owner"     :dog.owner.name,
                }
            )
        return JsonResponse({'results':results}, status=200)