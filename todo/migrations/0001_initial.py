# Generated by Django 3.2.3 on 2021-05-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=255)),
                ('is_completed', models.BooleanField(default=False)),
                ('due_date', models.DateField()),
            ],
        ),
    ]
