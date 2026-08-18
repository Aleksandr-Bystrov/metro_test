from django import forms
from django.core.exceptions import ValidationError

from metro.settings import MAX_LENGH_POST, MAX_SIZE_IMAGE, MIN_LENG_POST
from .models import Post


class PostForm(forms.ModelForm):
    """Класс формы для создания поста."""

    def clean_content(self):
        """Валидация длинны теста поста."""
        content = self.cleaned_data.get('content')
        if len(content) < MIN_LENG_POST:
            raise ValidationError('Слишком короткий пост')
        if len(content) > MAX_LENGH_POST:
            raise ValidationError('Слишком длинный пост')
        return content

    def clean_image(self):
        """Валидация размера изображения для поста."""
        image = self.cleaned_data.get('image')
        if image:
            if image.size > MAX_SIZE_IMAGE * 1024 * 1024:
                raise ValidationError(
                    f"Размер файла не должен превышать {MAX_SIZE_IMAGE} МБ.")
        return image

    class Meta:
        model = Post
        fields = ('content', 'image')
