import copy

from django.core.exceptions import BadRequest
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponseBadRequest
from django.shortcuts import render

TAGS = [

]

# Create your views here.
QUESTIONS = [
    {
        'title' : f"Title {i}",
        'id' : i,
        'text': f"This is text for question {i}"
    } for i in range(30)
]

Commentator = [
    {
        'Author' : f"Author {i}",
        'Text' : f"This comment was created by Author {i}"
    } for i in range(30)
]

def Pagin(req, q, num):
    page_num = req.GET.get('page', 1)

    try:
        page_num = int(page_num)
    except ValueError:
        return None, 'Page must be an integer'

    paginator = Paginator(q, num)

    try:
        page = paginator.page(page_num)
    except EmptyPage:
        return None, 'Page does not exist'

    return page, None
def index(request):
    page, error = Pagin(request, Commentator, 5)
    if error:
        return HttpResponseBadRequest(error)
    return render(request, 'home.html', context={'questions': page.object_list, 'page_obj' : page})

def hot(request):
    q = reversed(copy.deepcopy(QUESTIONS))
    return render(request, 'hot.html', context={'questions': q})

def OneQuestions(request, question_id):
    page, error = Pagin(request, Commentator, 5)

    if error:
        return HttpResponseBadRequest(error)

    return render(request, 'oneQuestin.html', context={'question': QUESTIONS[question_id], 'nums': Commentator, 'Com' :page.object_list, 'page_obj' : page })

def registration(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def settings(request):
    return render(request, "set_profile.html")

def new_quest(request):
    return render(request, "NewQuestion.html")

def new_quest(request):
    return render(request, "NewQuestion.html")

def tag_search(request, tag):
    return render(request, "NewQuestion.html", context={"tag": tag})