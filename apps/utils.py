import os
from PIL import Image

def convert_image(instance, image_field_name: str, upload_dir: str = "base"):
    image_field = getattr(instance, image_field_name)

    if not image_field or not hasattr(image_field, 'path'):
        return

    image_path = image_field.path
    image = Image.open(image_path)

    if image.mode != "RGB":
        image = image.convert("RGB")

    # Генерируем новое имя и путь
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    webp_name = f"{base_name}.webp"
    webp_path = os.path.join(os.path.dirname(image_path), webp_name)

    # Сохраняем в WebP
    image.save(webp_path, "WEBP", quality=80)

    # Удаляем оригинал
    if os.path.exists(image_path):
        os.remove(image_path)

    # Обновляем путь к файлу в поле модели
    image_field.name = os.path.join(upload_dir, webp_name)

    return image_field.name
