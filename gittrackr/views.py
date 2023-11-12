from django.shortcuts import render, redirect
from .forms import CreateFolderForm
from apps.utilities.forms import AddRepositoryForm
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from master.models import Folders

# Create your views here.
def index(request):
    return render(request, "base/home_unlogged.html")

def indexLogged(request):
    form = CreateFolderForm()

    return render(request, "base/home_logged.html", {'form': form})

def add_folder(request):
    form = AddRepositoryForm()
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')

        # # Gunakan user yang sudah login
        # user = request.user

        # Simpan repository ke dalam database
        folders = Folders(Folder_Name=folder_name)
        folders.save()
    return render(request, "utilities/add_repo.html", {'form': form})
