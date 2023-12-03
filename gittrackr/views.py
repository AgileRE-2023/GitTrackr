from django.shortcuts import render, redirect
from .forms import CreateFolderForm
from apps.utilities.forms import AddRepositoryForm
from django.contrib.auth.decorators import login_required
import requests
from social_django.models import UserSocialAuth
from master.models import Folders

# Create your views here.
def index(request):
    return render(request, "base/home_unlogged.html")

def indexLogged(request):
    form = CreateFolderForm()

    return render(request, "base/home_logged.html", {'form': form})

def create_folder(request):
    form = AddRepositoryForm()
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')

        # Gunakan user yang sudah login
        user = request.user

        # Simpan repository ke dalam database
        folders = Folders.objects.create(Folder_Name=folder_name, UserID=user)
        folders.save()

        # Simpan FolderID ke dalam sesi
        request.session['current_folder_id'] = folders.FolderID

        # Arahkan pengguna ke halaman 'add_repository' untuk folder baru
        return redirect('add_repository_with_folder', folder_id=folders.FolderID)