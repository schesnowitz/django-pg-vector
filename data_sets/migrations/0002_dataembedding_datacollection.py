# Generated by Django 4.2.5 on 2023-10-02 00:25

from django.db import migrations, models
import pgvector.django


class Migration(migrations.Migration):

    dependencies = [
        ('data_sets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataEmbedding',
            fields=[
                ('embedding', pgvector.django.VectorField(dimensions=1536)),
                ('document', models.CharField(blank=True, null=True)),
                ('cmetadata', models.TextField(blank=True, null=True)),
                ('custom_id', models.CharField(blank=True, null=True)),
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'data_embedding',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataCollection',
            fields=[
                ('name', models.CharField(blank=True, null=True)),
                ('cmetadata', models.TextField(blank=True, null=True)),
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'data_collection',
                'managed': True,
            },
        ),
    ]