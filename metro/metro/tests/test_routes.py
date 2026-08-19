from http import HTTPStatus

from metro.tests.conftest import Test


class TestRoutes(Test):
    """Класс тестов маршрутов и статусов."""

    def test_pages_availability_for_anonymous_user(self):
        """Проверка соответствий ожидаемых статусов."""
        list_of_matches = [
            (self.HOME_URL, self.anon_client, HTTPStatus.OK),
            (self.LOGIN_URL, self.anon_client, HTTPStatus.OK),
            (self.LOGOUT_URL, self.anon_client, HTTPStatus.OK),
            (self.SIGNUP_URL, self.anon_client, HTTPStatus.OK),
            (self.ADD_URL, self.author_client, HTTPStatus.OK),
            (self.EDIT_URL, self.author_client, HTTPStatus.OK),
            (self.DELETE_URL, self.author_client, HTTPStatus.OK),
            (self.DETAIL_URL, self.author_client, HTTPStatus.OK),
            (self.EDIT_URL, self.another_author_client, HTTPStatus.FORBIDDEN),
            (self.DELETE_URL, self.another_author_client,
             HTTPStatus.FORBIDDEN),
            (self.DETAIL_URL, self.another_author_client,
             HTTPStatus.OK),
        ]
        for url, client, expected_status in list_of_matches:
            with self.subTest():
                if url == 'users:logout':
                    response = client.post(url)
                else:
                    response = client.get(url)
                self.assertEqual(response.status_code, expected_status)

    def test_redirect_for_anonymous_client(self):
        """Проверка переадресаций."""
        urls = (
            self.ADD_URL,
            self.EDIT_URL,
            self.DELETE_URL,
        )
        for url in urls:
            with self.subTest(url=url):
                redirect_url = f'{self.LOGIN_URL}?next={url}'
                response = self.client.get(url)
                self.assertRedirects(response, redirect_url)
