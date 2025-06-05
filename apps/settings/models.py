from django.db import models
from apps.utils import convert_image

class Base(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to="base",
        verbose_name='Фото'
    )
    is_active = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )    
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self,  *args, **kwargs):
        is_new = self._state.adding or 'force_inset' in kwargs
        super().save(*args, **kwargs)

        updated_path = convert_image(self, 'image', upload_dir="base")

        if updated_path:
            self.image.name = updated_path
            super().save(update_fields=["image"])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Главная'