import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="leand").exists():
    User.objects.create_superuser("leand", "leandromarqueswalter@gmail.com", "ebac")
    print("Superusuário criado!")
else:
    print("Usuário já existe.")