# Generated by Django 4.2.6 on 2023-11-12 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_entregables_rename_apellidade_profesor_apellido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='apellidade',
            new_name='apellido',
        ),
    ]
