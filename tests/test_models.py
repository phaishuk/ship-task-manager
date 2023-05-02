from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from sailors_app.models import Position, Task, TaskType


class ModelsTests(TestCase):

    def test_position_str(self):
        position = Position.objects.create(name="test_position",)
        self.assertEqual(
            str(position),
            f"{position.name}"
        )

    def test_task_str(self):
        task = Task.objects.create(
            name="test_task",
            description="test_description",
            deadline=date(2023, 4, 24),
            is_completed=True,
            priority="high",
            task_type=TaskType.objects.create(name="test_task_type"),
        )
        self.assertEqual(str(task), f"{task.name}")

    def test_sailor_str(self):
        sailor = get_user_model().objects.create_user(
            username="sailor",
            password="pass1234",
            position=Position.objects.create(name="test_position"),
            board_number="$HЕ_344537"
        )
        self.assertEqual(
            str(sailor),
            f"{sailor.username} ({sailor.position})"
        )

    def test_board_number_and_position_exists(self):
        username = "test"
        password = "test12345"
        board_number = "$HЕ_344537"
        position = Position.objects.create(name="test_position")
        sailor = get_user_model().objects.create_user(
            username=username,
            password=password,
            position=position,
            board_number=board_number,
        )

        self.assertEqual(sailor.username, username)
        self.assertTrue(sailor.check_password(password))
        self.assertEqual(sailor.board_number, board_number)
        self.assertEqual(sailor.position, position)
