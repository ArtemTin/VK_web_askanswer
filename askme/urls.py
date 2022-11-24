from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("hot/", views.hot_view, name="hot_view"),
    path("settings/<int:user_id>", views.settings_view, name="settings_view"),
    path("tag/<str:tag_name>", views.tag_view, name="tag_view"),
    path("question/<int:question_id>", views.question_view, name="question_view"),
    path("ask/", views.ask_view, name="ask_view"),

    path("login/", views.login_view, name="login_view"),
    path("signup/", views.signup_view, name="signup_view"),
    path("logout/", views.logout_view, name="logout_view"),
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]
