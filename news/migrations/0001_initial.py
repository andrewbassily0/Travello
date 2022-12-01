# Generated by Django 4.1.3 on 2022-12-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=4000)),
                ('image', models.ImageField(upload_to='media/pic')),
                ('day', models.DateField(auto_now_add=True)),
                ('month', models.DateField(auto_now_add=True)),
            ],
        ),
    ]