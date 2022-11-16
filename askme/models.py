from django.db import models
from django.db.models import Count, Q, Sum


# Managers

class QuestionManager(models.Manager):

    def get_hot(self):
        objs = super().all()
        objs = objs.annotate(
            rating=Count("questionlike", filter=Q(questionlike__value=1)) - Count("questionlike",
                                                                                  filter=Q(questionlike__value=-1))
        )
        return objs.order_by("-rating")

    def get_new(self):
        return super().all().order_by("-date")


# Create your models here.

class ProfileManager(models.Manager):

    def get_top(self):
        objs = super().all()
        objs = objs.annotate(
            user_rating=Count("question")
        )
        return objs.order_by("-user_rating")


class Profile(models.Model):
    name = models.CharField(max_length=80)
    avatar = models.CharField(max_length=255)  # ImageField!!
    signup_date = models.DateTimeField(auto_now_add=True)
    objects = ProfileManager()

    def questions(self):
        return self.question_set


class Tag(models.Model):
    name = models.CharField(max_length=80)
    questions = models.ManyToManyField("Question")


class Question(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    asker = models.ForeignKey("Profile", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")
    date = models.DateTimeField(auto_now_add=True)
    objects = QuestionManager()

    # рейтинг высчитывается
    def rating(self):
        return self.questionlike_set.filter(value__exact=1).count() - self.questionlike_set.filter(
            value__exact=-1).count()


class Answer(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    answerer = models.ForeignKey("Profile", on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    # рейтинг высчитывается
    def rating(self):
        return self.answerlike_set.filter(value__exact=1).count() - self.answerlike_set.filter(value__exact=-1).count()


class QuestionLike(models.Model):
    class LikeStatus(models.IntegerChoices):
        upvote = 1
        downvote = -1

    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    liker = models.ForeignKey("Profile", on_delete=models.CASCADE)
    value = models.IntegerField(choices=LikeStatus.choices)
    date = models.DateTimeField(auto_now_add=True)


class AnswerLike(models.Model):
    class LikeStatus(models.IntegerChoices):
        upvote = 1
        downvote = -1

    answer = models.ForeignKey("Answer", on_delete=models.CASCADE)
    liker = models.ForeignKey("Profile", on_delete=models.CASCADE)
    value = models.IntegerField(choices=LikeStatus.choices)
    date = models.DateTimeField(auto_now_add=True)
