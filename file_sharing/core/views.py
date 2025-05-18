from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import SharedFile

def index(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileUploadForm()
    
    files = SharedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'index.html', {'form': form, 'files': files})
