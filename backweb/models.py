from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=150, null=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=150)

    class Meta:
        db_table = 'token'


class Articles(models.Model):
    title = models.CharField(max_length=5)
    desc = models.CharField(max_length=100)
    content = models.TextField()
    icon = models.ImageField(upload_to='article', null=True)
    creat_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'


class Column(models.Model):
    c_name = models.CharField(max_length=10)
    c_keywords = models.CharField(max_length=10)
    c_describe = models.CharField(max_length=100)
    creat_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'column_article'






