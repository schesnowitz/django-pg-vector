# Generated by Django 4.2.5 on 2023-09-30 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='CnnVectors',
        ),
    ]
