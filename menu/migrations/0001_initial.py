# Generated by Django 4.1.7 on 2023-04-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.IntegerField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
