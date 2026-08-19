from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from metro.settings import POSTS_ON_THE_PAGE
from .forms import PostForm
from .models import Post


class OnlyAuthorMixin(UserPassesTestMixin):
    """Миксин ограничения доступа к чужим объектам."""

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):
    """Класс создания поста."""

    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:index')


class PostListView(ListView):
    """Класс для отображения домашней страницы с постами."""

    model = Post
    template_name = 'posts/index.html'
    paginate_by = POSTS_ON_THE_PAGE
    ordering = ['-created_at']


class PostUpdateView(OnlyAuthorMixin, UpdateView):
    """Класс редактирования поста."""

    model = Post
    form_class = PostForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/create.html'

    def get_success_url(self):
        return reverse('posts:index')


class PostDeleteView(OnlyAuthorMixin, DeleteView):
    """Класс удаления поста."""

    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/create.html'
    success_url = reverse_lazy('posts:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm(instance=self.get_object())
        return context


class PostView(DetailView):
    """Класс просмотра конкретного поста."""

    model = Post
    template_name = 'posts/detail.html'
    pk_url_kwarg = 'post_id'
