from django.apps import AppConfig
import os

if os.path.exists("env.py"):
    import env

print(os.getenv("envpy_test"))


class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
