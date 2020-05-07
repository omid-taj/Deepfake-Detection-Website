from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View

from utilities import save_file


class EvaluationView(LoginRequiredMixin, View):

    def get(self, request):
        files = request.user.files.all()
        return render(request, 'eval.html', {'files': files})

    def post(self, request):
        try:
            myfile = request.FILES['myFile']
            save_file(myfile, request.user)
            return redirect('home')
        except:
            files = request.user.files.all()
            return render(request, 'eval.html', {'files': files})