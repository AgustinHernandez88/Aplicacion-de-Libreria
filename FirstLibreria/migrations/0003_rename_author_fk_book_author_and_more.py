# Generated by Django 4.2.4 on 2023-10-31 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstLibreria', '0002_alter_author_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_fk',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='genre_fk',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publisher_fk',
            new_name='publisher',
        ),
    ]