# Generated by Django 3.0.8 on 2022-02-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220209_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.TextField()),
            ],
        ),
    ]
