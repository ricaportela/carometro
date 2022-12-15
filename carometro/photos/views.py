import time

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm
from .models import Photo


class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/progress_bar_upload/progress.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.title = photo.file.name
            photo.image = photo.file
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url, 'title': photo.file.name}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))

def list_photos(request):
    photos_list = Photo.objects.all()
    return render(request, 'photos/listing_photos/list.html', {'photos': photos_list})