# Generated by Django 3.0.5 on 2020-04-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerpost',
            name='postType',
            field=models.CharField(choices=[('Internship', 'Internship'), ('Job', 'Job')], max_length=30),
        ),
    ]