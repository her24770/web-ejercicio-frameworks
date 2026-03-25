from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from polls.models import Poll, Option


class Command(BaseCommand):
    help = "Crea el superusuario y la encuesta de ejemplo"

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(username="admin", password="admin123", email="admin@demo.com")
            self.stdout.write(self.style.SUCCESS("Superusuario 'admin' creado."))

        if not Poll.objects.exists():
            poll = Poll.objects.create(question="¿Cuál es el mejor framework de desarrollo web?")
            for texto in ["React", "Svelte", "Vue", "Angular"]:
                Option.objects.create(poll=poll, text=texto)
            self.stdout.write(self.style.SUCCESS("Encuesta de ejemplo creada."))
