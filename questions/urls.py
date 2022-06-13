from django.urls import path
from .views import question_list, question_details

urlpatterns = [
    path('', question_list, name='question_list'),
    path("question/<slug:slug>/", question_details, name="question_details"),
]