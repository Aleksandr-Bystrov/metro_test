from http import HTTPStatus

from posts.models import Post
from metro.tests.conftest import Test


class TestLogic(Test):
    """Класс тестирования логики работы."""

    @classmethod
    def setUpTestData(cls):
        """Подготовка данных для передачи в формы."""
        super().setUpTestData()
        cls.form_data = {
            'content': 'Пост автора',
        }
        cls.new_form_data = {
            'title': 'Новый пост',
        }

    def test_anonymous_user_cant_create_post(self):
        """Анонимный пользователь не может создать пост."""
        count_before_attempt = Post.objects.count()
        response = self.client.post(self.ADD_URL, data=self.form_data)
        count_after_attempt = Post.objects.count()
        self.assertEqual(count_before_attempt, count_after_attempt)
        redirect_url = f'{self.LOGIN_URL}?next={self.ADD_URL}'
        self.assertRedirects(response, redirect_url)

    def test_user_can_create_post(self):
        """Авторизованный пользователь может создать пост."""
        Post.objects.all().delete()
        self.author_client.post(self.ADD_URL, data=self.form_data)
        posts_count = Post.objects.count()
        self.assertEqual(posts_count, 1)
        new_post = Post.objects.get()
        self.assertEqual(new_post.content, self.form_data['content'])
        self.assertEqual(new_post.author, self.author)

    def test_author_can_edit_post(self):
        """Автор может редактировать свой пост."""
        response = self.author_client.post(
            self.EDIT_URL, data=self.new_form_data)
        updated_post = Post.objects.get(pk=self.post_author.pk)
        self.assertEqual(self.new_form_data['content'], updated_post.content)
        self.assertEqual(self.post_author.author, updated_post.author)

    def test_another_user_cant_edit_post(self):
        """Авторизованный пользователь не может редактировать чужой пост."""
        response = self.another_author_client.post(
            self.EDIT_URL, data=self.new_form_data)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)
        updated_note = Post.objects.get(pk=self.post_author.pk)
        self.assertEqual(self.post_author.content, updated_note.content)
        self.assertEqual(self.post_author.author, updated_note.author)

    def test_author_can_delete_post(self):
        """Автор может удалить свой пост."""
        count_before_attempt = Post.objects.count()
        response = self.author_client.post(self.DELETE_URL)
        count_after_attempt = Post.objects.count()
        self.assertEqual(count_before_attempt - 1, count_after_attempt)

    def test_another_user_cant_delete_post(self):
        """Авторизованный пользователь не может удалить чужой пост."""
        count_before_attempt = Post.objects.count()
        response = self.another_author_client.post(self.DELETE_URL)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)
        count_after_attempt = Post.objects.count()
        self.assertEqual(count_before_attempt, count_after_attempt)
