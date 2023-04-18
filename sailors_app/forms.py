from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from sailors_app.models import Sailor, Task


def validate_board_number(board_number):
    if not (board_number[0] == "$" and board_number[3] == "_"):
        raise ValidationError(
            "Ensure that the value's first letter is '$' and fourth is '_'"
        )
    if not (board_number[1:3].isupper() and board_number[1:3].isalpha()):
        raise ValidationError(
            "Ensure that the value's second and third letter "
            "starts with  uppercase letters"
        )
    if not board_number[-6:].isdigit():
        raise ValidationError("Ensure that value ends with 6 digits")
    if not len(board_number) == 10:
        raise ValidationError(
            "Ensure that length of your licence exactly 10 characters"
        )
    return board_number


class SailorCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Sailor
        fields = UserCreationForm.Meta.fields + ("position", "board_number",)

    def clean_board_number(self):
        board_number = self.cleaned_data["board_number"]
        return validate_board_number(board_number)


class SailorBoardNumberUpdateForm(forms.ModelForm):
    class Meta:
        model = Sailor
        fields = (
            "username", "password", "first_name", "last_name",
            "email", "position", "board_number",
        )

    def clean_board_number(self):
        board_number = self.cleaned_data["board_number"]
        return validate_board_number(board_number)


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"
