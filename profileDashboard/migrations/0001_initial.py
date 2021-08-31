# Generated by Django 3.0.7 on 2020-07-05 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('timeSession', models.CharField(choices=[('two', '2'), ('four', '4')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=50)),
                ('experienceTime', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=60)),
                ('portfolioWebsite', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateStarted', models.DateField()),
                ('dateFinished', models.DateField()),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileDashboard.Degree')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=30)),
                ('alumniType', models.CharField(choices=[('Student', 'Student Alumni'), ('Professional', 'Professional Alumni')], max_length=30)),
                ('profilePic', models.ImageField(null=True, upload_to='Profile')),
                ('intro', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='degree',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileDashboard.Department'),
        ),
    ]
