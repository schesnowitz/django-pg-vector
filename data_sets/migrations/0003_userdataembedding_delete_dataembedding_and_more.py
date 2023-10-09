# Generated by Django 4.2.5 on 2023-10-08 23:34

from django.db import migrations, models
import django.db.models.deletion
import pgvector.django


class Migration(migrations.Migration):

    dependencies = [
        ('data_sets', '0002_dataembedding_datacollection'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDataEmbedding',
            fields=[
                ('embedding', pgvector.django.VectorField(dimensions=1536)),
                ('document', models.CharField(blank=True, null=True)),
                ('cmetadata', models.TextField(blank=True, null=True)),
                ('custom_id', models.CharField(blank=True, null=True)),
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'data_embedding',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='DataEmbedding',
        ),
        migrations.RenameModel(
            old_name='DataCollection',
            new_name='UserDataCollection',
        ),
        migrations.AddField(
            model_name='userdataembedding',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='embedding', to='data_sets.userdatacollection'),
        ),
    ]