from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Poll",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("question", models.CharField(max_length=255, verbose_name="Pregunta")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Creada en")),
            ],
            options={
                "verbose_name": "Encuesta",
                "verbose_name_plural": "Encuestas",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Option",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.CharField(max_length=255, verbose_name="Texto")),
                ("votes", models.PositiveIntegerField(default=0, verbose_name="Votos")),
                (
                    "poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="options",
                        to="polls.poll",
                    ),
                ),
            ],
            options={
                "verbose_name": "Opción",
                "verbose_name_plural": "Opciones",
                "ordering": ["id"],
            },
        ),
    ]
