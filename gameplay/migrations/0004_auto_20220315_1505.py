# Generated by Django 3.2.9 on 2022-03-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0003_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.CharField(choices=[('ANIMALS', 'Animals'), ('CITIES', 'Cities'), ('MOVIES', 'Movies')], default='ANIMALS', max_length=20),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]