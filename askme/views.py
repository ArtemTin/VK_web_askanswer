from django.http import HttpResponse


def main_view(request):
    return HttpResponse("Hello, world. Main")


def hot_view(request):
    return HttpResponse("Hello, world. Hot")


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
