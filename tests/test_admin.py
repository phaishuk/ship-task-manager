from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from sailors_app.models import Position


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
            position=Position.objects.create(name="admin_position"),
            board_number="$HF_348537"
        )

        self.client.force_login(self.admin_user)
        self.sailor = get_user_model().objects.create_user(
            username="sailor",
            password="pass1234",
            position=Position.objects.create(name="test_position"),
            board_number="$HЕ_344537"
        )

    def test_sailor_display_board_number_and_position_field(self):
        url = reverse("admin:sailors_app_sailor_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.sailor.board_number)
        self.assertContains(res, self.sailor.position.name)

    def test_sailor_display_board_number_and_position_in_details(self):
        url = reverse("admin:sailors_app_sailor_change", args=[self.sailor.id])
        res = self.client.get(url)

        self.assertContains(res, self.sailor.board_number)
        self.assertContains(res, self.sailor.position.name)

