# Generated by Django 3.2.9 on 2021-12-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('league_number', models.IntegerField(max_length=5)),
                ('team_id', models.IntegerField(max_length=5)),
            ],
        ),
    ]