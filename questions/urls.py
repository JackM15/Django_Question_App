from django.urls import path
from .views import question_list, question_details, register, create_question

urlpatterns = [
    path('', question_list, name='question_list'),
    path("question/<slug:slug>/", question_details, name="question_details"),
    path("register/", register, name="register"),
    path("create/", create_question, name="create_question"),
]