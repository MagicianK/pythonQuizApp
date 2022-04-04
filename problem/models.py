from django.db import models


# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=50)
    difficulty = models.IntegerField()


class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    solved_task_hard_count = models.IntegerField()
    solved_task_medium_count = models.IntegerField()
    solved_task_easy_count = models.IntegerField()

    def solved_task_count(self):
        return self.solved_task_easy_count + self.solved_task_hard_count + self.solved_task_medium_count


class UserFollowing(models.Model):
    user_id = models.ForeignKey("User", related_name="following", on_delete=models.CASCADE)

    following_user_id = models.ForeignKey("User", related_name="followers", on_delete=models.CASCADE)

    # You can even add info about when user started following
    created = models.DateTimeField(auto_now_add=True)


class submissionHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    status = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
