import os
from PIL import Image


def generate_ios_icons(input_image_path, output_folder='ios_icons'):
  # 1. Проверяем, существует ли исходный файл
  if not os.path.exists(input_image_path):
    print(f"ОШИБКА: Файл '{input_image_path}' не найден.")
    print("Убедитесь, что картинка лежит в одной папке с этим скриптом.")
    return

  # 2. Создаем папку для иконок
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  # 3. Загружаем изображение
  try:
    img = Image.open(input_image_path)
  except Exception as e:
    print(f"Ошибка при открытии изображения: {e}")
    return

  # Проверка на квадратность (предупреждение)
  if img.width != img.height:
    print("Предупреждение: Ваше изображение не квадратное. Иконки могут быть искажены.")

  # 4. Список размеров для iPhone (iOS 15+)
  # Формат: (Имя файла, Размер в пикселях)
  icon_sizes = [
    # --- App Store (Master) ---
    ('AppStore-1024.png', 1024),

    # --- iPhone Home Screen (60pt) ---
    ('Icon-60@2x.png', 120),  # iPhone SE, 8, др.
    ('Icon-60@3x.png', 180),  # iPhone Pro, Max, Plus

    # --- Spotlight Search (40pt) ---
    ('Icon-40@2x.png', 80),
    ('Icon-40@3x.png', 120),

    # --- Settings (29pt) ---
    ('Icon-29@2x.png', 58),
    ('Icon-29@3x.png', 87),

    # --- Notifications (20pt) ---
    ('Icon-20@2x.png', 40),
    ('Icon-20@3x.png', 60),
  ]

  print(f"Начинаю нарезку из файла: {input_image_path}...")

  for filename, size in icon_sizes:
    # Используем LANCZOS для максимальной четкости линий при уменьшении
    resized_img = img.resize((size, size), Image.Resampling.LANCZOS)

    # Сохраняем в папку
    save_path = os.path.join(output_folder, filename)
    resized_img.save(save_path)
    print(f"Сохранено: {filename} ({size}x{size})")

  print(f"\nГотово! Папка с иконками создана: {os.path.abspath(output_folder)}")


# --- ЗАПУСК ---
# Скрипт возьмет именно ваш файл
generate_ios_icons('img/BrandNewLogo.png')
