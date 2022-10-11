from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("ask/", views.ask_view, name="ask_view"),
    path("hot/", views.hot_view, name="hot_view"),
    path("tag/<slug:tag_name>", views.tag_view, name="tag_view"),
    # path("tag/", views.tag_view, name="tag_view"),
    path("login/", views.login_view, name="login_view"),
    path("signup/", views.signup_view, name="signup_view"),
    path("question/<int:question_id>", views.question_view, name="question_view"),
    # path("question/", views.question_view, name="question_view"),
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]