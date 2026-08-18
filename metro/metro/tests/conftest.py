from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from posts.models import Post

User = get_user_model()


class Test(TestCase):
    """Класс для тестов."""

    @classmethod
    def setUpTestData(cls):
        """Подготовка объектов"""
        cls.author = User.objects.create(username='Автор',
                                         email='author@mail.ru')
        cls.another_author = User.objects.create(username='Другой автор',
                                                 email='anotherauthor@mail.ru')
        cls.post_author = Post.objects.create(
            content='Пост автора',
            author=cls.author,
        )
        cls.author_client = Client()
        cls.author_client.force_login(cls.author)
        cls.another_author_client = Client()
        cls.another_author_client.force_login(cls.another_author)
        cls.anon_client = Client()
        cls.HOME_URL = reverse('posts:index')
        cls.ADD_URL = reverse('posts:create_post')
        cls.EDIT_URL = reverse('posts:edit_post', args=(cls.post_author.pk,))
        cls.DELETE_URL = reverse('posts:delete_post',
                                 args=(cls.post_author.pk,))
        cls.DETAIL_URL = reverse('posts:post_detail',
                                 args=(cls.post_author.pk,))
        cls.LOGIN_URL = reverse('users:login')
        cls.LOGOUT_URL = reverse('users:logout')
        cls.SIGNUP_URL = reverse('registration')
