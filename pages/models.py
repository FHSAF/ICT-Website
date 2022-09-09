from django.db import models
from accounts.models import UserProfile


class BlogsModel(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=120)
    headline = models.CharField(max_length=200)
    tag = models.CharField(max_length=150)
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class BodyModel(models.Model):
    body = models.TextField()
    blog = models.ForeignKey(to=BlogsModel, on_delete=models.CASCADE)


class CommentModel(models.Model):
    comment_text = models.TextField(max_length=1000)
    last_updated = models.DateTimeField(auto_now_add=True)
    related_blog = models.ForeignKey(
        BlogsModel, related_name='comments', on_delete=models.CASCADE)
    commented_by = models.ForeignKey(
        UserProfile, related_name='comments', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.commented_by.firstname


class ReplyCommentModel(models.Model):
    reply_comment_text = models.TextField(max_length=4000)
    comment = models.ForeignKey(
        CommentModel, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        UserProfile, related_name='replies', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        UserProfile, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)


class Packages(models.Model):
    package_type = models.CharField(choices=(
        ('Hostel', 'Hostel'), ('Home', 'Home'), ('Enterprise', 'Enterprise')), max_length=100)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    package_speed = models.CharField(max_length=100)
    package_category = models.CharField(
        choices=(('limited', 'limited'), ('unlimited', 'unlimited')), max_length=100)
    validity = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
