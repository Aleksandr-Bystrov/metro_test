from posts.forms import PostForm
from metro.tests.conftest import Test


class TestContent(Test):
    """Класс тестов контента."""

    def test_authorized_client_has_form(self):
        """
        Проверка доступа к форме создания поста для авторизованного
        пользователя.
        """
        urls = (self.ADD_URL, self.EDIT_URL)
        for url in urls:
            with self.subTest():
                response = self.author_client.get(url)
                self.assertIn('form', response.context)
                self.assertIsInstance(response.context['form'], PostForm)
