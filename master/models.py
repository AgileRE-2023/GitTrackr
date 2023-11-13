from django.db import models
# from social_django.models import UserSocialAuth
from django.contrib.auth.models import User

class Folders(models.Model):
    FolderID = models.AutoField(primary_key=True)
    Folder_Name = models.CharField(max_length=255, unique=True)
    Created_At = models.DateTimeField(auto_now_add=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

class Repository(models.Model):
    RepositoryID = models.AutoField(primary_key=True)
    Repository_Name = models.CharField(max_length=255, unique=True)
    Url = models.TextField()

class History(models.Model):
    HistoryID = models.AutoField(primary_key=True)
    Timestap = models.DateTimeField()
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    FolderID = models.ForeignKey(Folders, on_delete=models.CASCADE)
