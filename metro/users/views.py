from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import RegisterForm, UserForm

User = get_user_model()

class ProfileView(DetailView):
    """Класс просмотра профиля пользователя."""

    model = User
    template_name = 'posts/profile.html'
    slug_url_kwarg = 'username'
    slug_field = 'username'

    def get_author(self):
        return get_object_or_404(User, username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_author()
        return context

class ProfileEditView(LoginRequiredMixin, UpdateView):
    """Класс редактирования профиля пользователя."""

    model = User
    template_name = 'posts/user.html'
    form_class = UserForm

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse('users:profile',
                       kwargs={
                           'username': self.request.POST.get('username')})


class RegisrationView(CreateView):
    """Класс для регистрации пользователя."""

    template_name = 'registration/registration_form.html'
    form_class = RegisterForm
    success_url = reverse_lazy('posts:index')
