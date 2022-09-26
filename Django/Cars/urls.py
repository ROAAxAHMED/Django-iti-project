from django.urls import path
from cars.views import booksIndex, CarsDetails, CreateCarsView,EditCarsView, DeleteCarsView
urlpatterns = [
    path('index',carsIndex ),
    path('<int:pk>',CarsDetails.as_view(), name='cars.show'),
    path('create', CreateCarsView.as_view()),
    path('edit/<int:pk>',EditCarsView.as_view(), name='cars.edit'),
    path('delete/<int:pk>',DeleteCarsView.as_view(), name='cars.delete'),
]
