from traceback import print_tb

from django.core.files.storage import default_storage
from django.shortcuts import redirect, render

from . import forms


def home(request):
    return render(request, 'base/home.html')


def upload(request):
    if request.method == 'POST':
        form = forms.UploadForm(request.POST)
        print("not validated")
        if form.is_valid():
            print("valid")
            print(request.FILES.get('image').name)
            print(request.FILES['audio'].name)
            # save cover image
            #music = form.save(commit=False)
            # music

            # return redirect('home')
    else:
        form = forms.UploadForm()

    context = {'form': form, }

    return render(request, 'base/upload/upload.html', context)
