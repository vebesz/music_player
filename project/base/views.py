from django.core.files.storage import FileSystemStorage, default_storage
from django.shortcuts import redirect, render

from . import forms


def home(request):
    return render(request, 'base/home.html')


def upload(request):
    if request.method == 'POST':
        form = forms.UploadForm(request.POST, request.FILES)
        image = request.FILES['image']
        audio = request.FILES['audio']

        if form.is_valid():
            fs = FileSystemStorage()
            fs.save(image.name, image)
            fs.save(audio.name, audio)

            return redirect('home')
    else:
        form = forms.UploadForm()

    context = {'form': form}

    return render(request, 'base/upload/upload.html', context)
