# Generated by Django 4.0.6 on 2022-10-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_isbn_livro_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(related_name='livros', to='core.autor'),
        ),
    ]
