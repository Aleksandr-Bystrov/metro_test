from django import forms
from django.core.exceptions import ValidationError

from metro.settings import MAX_LENGH_POST, MAX_SIZE_IMAGE, MIN_LENG_POST
from .models import CustomUser


class UserForm(forms.ModelForm):
    """Класс формы редактирования профиля пользователя."""
    
    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) < MIN_LENG_POST:
            raise ValidationError('Слишком короткая биография')
        if len(bio) > MAX_LENGH_POST:
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
        model = CustomUser
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
