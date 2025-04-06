from django.shortcuts import render, redirect
from django.views import View
from .forms import ProfileUpdateForm
from .models import Profile

class ProfileUpdateView(View):
    def get(self, request):
        profile = request.user.profile
        form = ProfileUpdateForm(instance=profile)
        return render(request, 'profileinfo/profileinfo.html', {'form': form})

    def post(self, request):
        profile = request.user.profile
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            print(form.cleaned_data['image'])
            form.save()
            return redirect('users:profile')
        form = ProfileUpdateForm()
        return render(request, 'profileinfo/profileinfo.html', {'form': form})