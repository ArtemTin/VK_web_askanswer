from django.db import models


# Managers

class QuestionManager(models.Manager):

    def get_new(self):
        return super().order_by("date", "rating")

    def get_hot(self):
        return super().order_by("rating", "date")
# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=80)
    avatar = models.CharField(max_length=255)
    signup_date = models.DateTimeField(auto_now_add=True)
    def questions(self):
        return self.question_set



class Tag(models.Model):
    name = models.CharField(max_length=80)
    questions = models.ManyToManyField("Question")


class Question(models.Model):
    objects = QuestionManager
    title = models.CharField(max_length=80)
    body = models.TextField()
    asker = models.ForeignKey("Profile", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")
    date = models.DateTimeField(auto_now_add=True)
    # рейтинг высчитывается
    def rating(self):
        return self.questionlike_set.filter(value__exact=1).count() - self.questionlike_set.filter(value__exact=-1).count()


class Answer(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    answerer = models.ForeignKey("Profile", on_delete=models.CASCADE)
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


