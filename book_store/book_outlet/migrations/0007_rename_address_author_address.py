# Generated by Django 4.2.2 on 2023-06-25 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_address_remove_author_email_author_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='Address',
            new_name='address',
        ),
    ]
