from django.db import models

# Create your models here.

class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    Google_UserID = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Access_Token = models.CharField(max_length=255)
    Refresh_Token = models.CharField(max_length=255)
    Created_At = models.DateTimeField()

class Folders(models.Model):
    FolderID = models.AutoField(primary_key=True)
    Folder_Name = models.CharField(max_length=255, unique=True)
    Created_At = models.DateTimeField(auto_now_add=True)

class Repository(models.Model):
    RepositoryID = models.AutoField(primary_key=True)
    Repository_Name = models.CharField(max_length=255, unique=True)
    Url = models.TextField()

class History(models.Model):
    HistoryID = models.AutoField(primary_key=True)
    Timestap = models.DateTimeField()
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    FolderID = models.ForeignKey(Folders, on_delete=models.CASCADE)