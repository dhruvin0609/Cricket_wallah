# Generated by Django 4.1.7 on 2023-02-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playername', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='team',
            name='teamname',
            field=models.CharField(max_length=100),
        ),
    ]
