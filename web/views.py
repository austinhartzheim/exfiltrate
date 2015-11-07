from django.http import HttpResponse
from django.shortcuts import render
from . import forms, models


def web_list_public(request):
    public_files = models.UploadedFile.objects.filter(private=False)
    return render(request, 'web/list_public_files.html', {'files': public_files})

def web_upload_public_form(request):
    form = forms.UploadPublicForm()
    return render(request, "web/upload_public_form.html", {'form': form})

def web_upload_public_submit(request):
    if request.method != 'POST':
        return HttpResponse('Non-POST request.')  # TODO: better return value
    
    form = forms.UploadPublicForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse('Ok!')  # TODO: better return value
    else:
        return render(request, "web/upload_public_form.html", {'form': form})
        return HttpResponse('Form invalid.')  # TODO: better return value
