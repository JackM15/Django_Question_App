from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import UserRegistrationForm, QuestionCreationForm, AnswerForm, QuestionUpdateForm, AnswerUpdateForm, ProfileForm

@login_required
def question_list(request):

    if "search-term" in request.GET:
        q = request.GET["search-term"]
        question_list = Question.objects.filter(title__icontains=q).order_by("-created_at")
    
    else:
        question_list = Question.objects.all().order_by("-created_at")

    return render(request, "question_list.html", {"question_list": question_list})

@login_required
def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    # add an answer
    form = AnswerForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()

            return redirect("question_details", slug=question.slug)
    
    else:
        form = AnswerForm()

    return render(request, "question_details.html", {"question": question, "answer_list": answer_list, "form": form})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return render(request, "register_done.html", {"user_form": user_form})

    else:
        user_form = UserRegistrationForm()
    
    return render(request, "register.html", {"user_form": user_form})


@login_required
def create_question(request):
    if request.method == "POST":
        question_form = QuestionCreationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()

            return redirect("question_list")
    
    else:
        question_form = QuestionCreationForm()
    
    return render(request, "create_question.html", {"question_form": question_form})


@login_required
def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)

    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect("question_list")
    
    return render(request, "update_question.html", {"form": form})


@login_required
def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect("question_list")


@login_required
def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    form = AnswerUpdateForm(request.POST or None, instance=answer)

    if form.is_valid():
        form.save()
        return redirect("question_details", slug=answer.question.slug)
    
    return render(request, "update_answer.html", {"form": form})


@login_required
def delete_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect("question_details", slug=answer.question.slug)


@login_required
def change_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
    
    form = ProfileForm(instance= request.user)

    return render(request, 'registration/profile.html', {'form': form})


@login_required
def list_own_questions_and_answers(request):
    questions = Question.objects.filter(author=request.user).order_by("-created_at")
    answers = Answer.objects.filter(author=request.user).order_by("-created_at")

    return render(request, "own_questions_and_answers.html", {"questions": questions, "answers": answers})