# Generated by Django 3.1 on 2020-09-02 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(blank=True, max_length=12)),
                ('instructor_name', models.CharField(max_length=20)),
                ('instructor_badge', models.CharField(blank=True, max_length=10)),
                ('course_image', models.ImageField(blank=True, upload_to='images/')),
                ('video_lenght', models.CharField(blank=True, max_length=30)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Course_Title', models.CharField(max_length=200)),
                ('Course_Subtitle', models.CharField(max_length=300)),
                ('Language', models.CharField(blank=True, max_length=80)),
                ('Requirement_1', models.CharField(blank=True, max_length=100)),
                ('Requirement_2', models.CharField(blank=True, max_length=100)),
                ('Requirement_3', models.CharField(blank=True, max_length=100)),
                ('Description', models.TextField()),
                ('What_you_ll_learn_1', models.CharField(blank=True, max_length=100)),
                ('What_you_ll_learn_2', models.CharField(blank=True, max_length=100)),
                ('What_you_ll_learn_3', models.CharField(blank=True, max_length=100)),
                ('errol', models.URLField()),
            ],
        ),
    ]
