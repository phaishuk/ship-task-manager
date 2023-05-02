from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from sailors_app.models import Position


class PrivateCreateSailor(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test12345",
            position=Position.objects.create(name="test_position"),
            board_number="$HF_348537"
        )
        self.client.force_login(self.user)

    def test_create_sailor(self):
        form = {
            "username": "Username",
            "password1": "passworD123!@#",
            "password2": "passworD123!@#",
            "board_number": "$GR_344537",
            "position": Position.objects.create(name="test_position").id
        }
        self.client.post(reverse("sailors_app:sailor-create"), data=form)
        new_user = get_user_model().objects.get(
            board_number=form["board_number"]
        )
        response = self.client.post(
            reverse("sailors_app:sailor-create"), data=form
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            new_user.board_number, form["board_number"]
        )
        self.assertEqual(
            new_user.position.id, form["position"]
        )
