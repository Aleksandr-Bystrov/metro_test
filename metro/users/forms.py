from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


from metro.settings import MAX_LENGH_POST, MAX_SIZE_IMAGE, MIN_LENG_POST

User = get_user_model()


class UserForm(forms.ModelForm):
    """Класс формы редактирования профиля пользователя."""

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if bio and len(bio) < MIN_LENG_POST:
            raise ValidationError('Слишком короткая биография')
        if bio and len(bio) > MAX_LENGH_POST:
            raise ValidationError('Слишком длинная биография')
        return bio

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            if avatar.size > MAX_SIZE_IMAGE * 1024 * 1024:
                raise ValidationError(
                    f"Размер файла не должен превышать {MAX_SIZE_IMAGE} МБ.")
        return avatar

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'bio',
            'date_of_birth',
            'avatar',
        )
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'},
            )
        }


class RegisterForm(UserCreationForm):
    """Форма для регистрации нового пользователя."""

    class Meta:
        model = User
        fields = ('username', 'email')
