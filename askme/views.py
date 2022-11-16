from django.http import HttpResponse, Http404
from django.template import loader
from django.core.paginator import Paginator, InvalidPage
from askme.models import *

mock_users = [
    {"id": "1", "avatar_url": "https://github.com/mdo.png", "name": "Dr. Pepper"},
    {"id": "2", "avatar_url": "https://github.com/blackplayerten.png", "name": "Artem"},
]

mock_tags = [
    {"id": 1, "human_name": "Pascal"},
    {"id": 3, "human_name": "C++"},
    {"id": 15, "human_name": "Python"},
]

mock_questions = [
    {"id": "675", "asker": mock_users[1], "title": "Test Title", "rating": 15, "my_rating": 1, "answers_cnt": 5,
     "tags": [mock_tags[1], mock_tags[0]],
     "teaser": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore "
               "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
               "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse "
               "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa "
               "qui officia deserunt mollit anim id est laborum."},
    {"id": "675", "asker": mock_users[0], "title": "Test Title", "rating": 15, "my_rating": 1, "answers_cnt": 5,
     "tags": [mock_tags[0], mock_tags[1], mock_tags[2]],
     "teaser": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore "
               "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
               "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse "
               "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa "
               "qui officia deserunt mollit anim id est laborum."},
    {"id": "675", "asker": mock_users[1], "title": "Test Title", "rating": 15, "my_rating": 1, "answers_cnt": 5,
     "tags": [mock_tags[1], mock_tags[0]],
     "teaser": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore "
               "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
               "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse "
               "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa "
               "qui officia deserunt mollit anim id est laborum."},
]


def main_view(request):
    paginator = Paginator(Question.objects.all(), 10)
    page_num = request.GET.get('page')
    if page_num is None:
        page_num = 1
    try:
        questions_now = paginator.page(page_num)
    except InvalidPage:
        raise Http404('Page is not found')

    template = loader.get_template("askme/index.html")
    context = {"tab": "new", "user": mock_users[0], "page_objs": questions_now, "popular_tags": mock_tags,
               "best_members": mock_users}
    return HttpResponse(template.render(context, request))


def hot_view(request):
    template = loader.get_template("askme/index.html")
    context = {"tab": "hot", "user": None, "questions": [mock_questions[i % len(mock_questions)] for i in range(15)],
               "popular_tags": [mock_tags[i % len(mock_tags)] for i in range(10)],
               "best_members": [mock_users[i % len(mock_users)] for i in range(10)]}
    return HttpResponse(template.render(context, request))


def tag_view(request, tag_name):
    return HttpResponse("Hello, world. Tag {}".format(tag_name))


def question_view(request, question_id):
    return HttpResponse("Hello, world. Question {}".format(question_id))


def login_view(request):
    return HttpResponse("Hello, world. Login")


def signup_view(request):
    return HttpResponse("Hello, world. Signup")


def ask_view(request):
    return HttpResponse("Hello, world. Ask")


def settings_view(request, user_id):
    return HttpResponse("Hello, world. Settings {}".format(user_id))


def logout_view(request):
    return HttpResponse("Hello, world. Logout")
