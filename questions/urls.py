from django.urls import path
from .views import question_list, question_details, register, create_question, update_question

urlpatterns = [
    path('', question_list, name='question_list'),
    path("question/<slug:slug>/", question_details, name="question_details"),
    path("register/", register, name="register"),
    path("create/", create_question, name="create_question"),
    path("update/<slug:slug>/", update_question, name="update_question"),
]