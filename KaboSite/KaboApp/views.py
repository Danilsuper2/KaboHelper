from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django import forms


# Для приёма файлов
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def handle_uploaded_file(f):
    with open('../table.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
# Для приёма файлов


def index(request):
    return render(request, 'index.html')


def table(request):
    if request.method == 'POST':
        if not request.FILES:
            messages.warning(request, 'Файл не загружен')
        elif str(request.FILES['table']).split('.')[1].lower() == 'csv':
            handle_uploaded_file(request.FILES['table'])
            messages.info(request, 'Файл загружен')
        else:
            messages.warning(request, 'Неверный формат файла')
        return render(request, 'get_table.html')
    else:
        return render(request, 'get_table.html')