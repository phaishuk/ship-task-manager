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


class SailorUpdateForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Sailor
        fields = (
            "username", "old_password", "new_password", "confirm_password",
            "first_name", "last_name", "email", "position", "board_number",
        )

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.instance.check_password(old_password):
            raise forms.ValidationError(
                "The old password is incorrect."
            )
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password and confirm_password and (
                new_password != confirm_password
        ):
            raise forms.ValidationError(
                "The new passwords do not match."
            )
        return cleaned_data

    def save(self, commit=True):
        sailor = super().save(commit=False)
        new_password = self.cleaned_data.get("new_password")
        if new_password:
            sailor.set_password(new_password)
        if commit:
            sailor.save()
        return sailor

    def clean_board_number(self):
        board_number = self.cleaned_data["board_number"]
        return validate_board_number(board_number)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"

    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


class SearchSailors(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by sailor's name"}
        ),
    )


class SearchTasks(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by task's name"}
        ),
    )


class SearchPositions(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by position's name"}
        ),
    )
