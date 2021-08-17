from django.urls import path

from products.views import ownersview, dogsview

urlpatterns = [
	path('/owners', ownersview.as_view()),
    path('/dogs', dogsview.as_view()),
]