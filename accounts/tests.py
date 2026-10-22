from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AccountAuthenticationTests(TestCase):
    def test_registration_creates_user_and_logs_them_in(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password1": "A-strong-test-password-928!",
                "password2": "A-strong-test-password-928!",
            },
        )

        self.assertRedirects(response, reverse("home"))
        user = get_user_model().objects.get(username="newuser")
        self.assertTrue(user.check_password("A-strong-test-password-928!"))
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)

    def test_invalid_registration_does_not_create_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password1": "password",
                "password2": "different-password",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(get_user_model().objects.filter(username="newuser").exists())

    def test_login_authenticates_existing_user(self):
        user = get_user_model().objects.create_user(
            username="existing",
            email="existing@example.com",
            password="A-strong-test-password-928!",
        )

        response = self.client.post(
            reverse("login"),
            {"username": "existing", "password": "A-strong-test-password-928!"},
        )

        self.assertRedirects(response, reverse("home"))
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)

    def test_account_page_requires_login(self):
        response = self.client.get(reverse("account"))

        self.assertRedirects(
            response, f"{reverse('login')}?next={reverse('account')}"
        )

    def test_authenticated_user_can_view_account_and_logout(self):
        user = get_user_model().objects.create_user(
            username="signedin",
            email="signedin@example.com",
            password="A-strong-test-password-928!",
        )
        self.client.force_login(user)

        account_response = self.client.get(reverse("account"))
        logout_response = self.client.post(reverse("logout"))

        self.assertEqual(account_response.status_code, 200)
        self.assertContains(account_response, "signedin")
        self.assertRedirects(logout_response, reverse("home"))
        self.assertNotIn("_auth_user_id", self.client.session)
