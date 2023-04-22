from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from sailors_app.models import Position, Sailor, Task, TaskType

ENTER_URL = reverse("sailors_app:index")
POSITION_LIST_URL = reverse("sailors_app:position-list")
TASK_LIST_URL = reverse("sailors_app:task-list")
SAILOR_LIST_URL = reverse("sailors_app:sailor-list")


class PublicIndexTests(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(ENTER_URL)
        self.assertNotEqual(res.status_code, 200)


class PublicPositionListTests(TestCase):
    def test_login_required(self):
        response = self.client.get(POSITION_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivatePositionTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="sailor",
            password="pass1234",
            position=Position.objects.create(name="test_position"),
            board_number="$HЕ_344537"
        )
        self.client.force_login(self.user)

    def test_retrieve_positions(self):
        Position.objects.create(name="test1",)
        Position.objects.create(name="test2",)

        response = self.client.get(POSITION_LIST_URL)
        positions = Position.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["position_list"]),
            list(positions)
        )
        self.assertTemplateUsed(response, "sailors_app/position_list.html")


class PrivateTaskTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="sailor",
            password="pass1234",
            position=Position.objects.create(name="test_position"),
            board_number="$HЕ_345357"
        )
        self.client.force_login(self.user)

    def test_retrieve_tasks(self):
        Task.objects.create(
            name="test_task",
            description="test_description",
            deadline=date(2023, 4, 24),
            is_completed=True,
            priority="high",
            task_type=TaskType.objects.create(name="test_task_type")
        )
        Task.objects.create(
            name="test_task",
            description="test_description",
            deadline=date(2023, 4, 24),
            is_completed=True,
            priority="high",
            task_type=TaskType.objects.create(name="test_task_type")
        )

        response = self.client.get(TASK_LIST_URL)
        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed(response, "sailors_app/task_list.html")


class PublicSailorListTests(TestCase):
    def test_login_required(self):
        response = self.client.get(SAILOR_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateSailorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="sailor",
            password="pass1234",
            position=Position.objects.create(name="test_position"),
            board_number="$QY_343487"
        )
        self.client.force_login(self.user)

    def test_retrieve_sailors(self):
        get_user_model().objects.create_user(
            username="test_sailor",
            password="pass1234",
            position=Position.objects.create(name="test_position"),
            board_number="$HЕ_344537"
        )

        get_user_model().objects.create_user(
            username="test_sailor2",
            password="pass1234",
            position=Position.objects.create(name="test_position2"),
            board_number="$TЕ_342637"
        )

        response = self.client.get(SAILOR_LIST_URL)
        sailors = Sailor.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["sailor_list"]),
            list(sailors)
        )
        self.assertTemplateUsed(response, "sailors_app/sailor_list.html")


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
            username=form["username"]
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
