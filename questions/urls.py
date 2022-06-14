from django.urls import path
from .views import question_list, question_details, register, create_question, update_question, delete_question, update_answer, delete_answer, change_profile, list_own_questions_and_answers

urlpatterns = [
    path('', question_list, name='question_list'),
    path("question/<slug:slug>/", question_details, name="question_details"),
    path("register/", register, name="register"),
    path("create/", create_question, name="create_question"),
    path("update/<slug:slug>/", update_question, name="update_question"),
    path("delete/<slug:slug>/", delete_question, name="delete_question"),
    path("answer/update/<int:id>/", update_answer, name="update_answer"),
    path("answer/delete/<int:id>/", delete_answer, name="delete_answer"),
    path("profile/", change_profile, name="change_profile"),
    path("my_qas/", list_own_questions_and_answers, name="my_qas"),
]   