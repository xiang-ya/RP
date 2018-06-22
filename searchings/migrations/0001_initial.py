# Generated by Django 2.0.6 on 2018-06-14 04:23

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
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=20)),
                ('college_introduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneralClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_introduction', models.TextField()),
                ('class_prerequisite', models.CharField(max_length=20)),
                ('class_type', models.CharField(max_length=20)),
                ('class_credit', models.FloatField()),
                ('class_college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searchings.College')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_name', models.CharField(max_length=30)),
                ('prof_introduction', models.TextField()),
                ('prof_college', models.ManyToManyField(to='searchings.College')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_rating', models.FloatField()),
                ('overall_difficulty_number', models.FloatField()),
                ('class_graded', models.CharField(max_length=5)),
                ('overall_difficulty', models.CharField(max_length=100)),
                ('overall_looking', models.CharField(max_length=20)),
                ('attendance_requirement', models.CharField(choices=[('未知', "it's still a secret"), ('每周必点', '100% take attendance'), ('人少就点', 'if there seems like not enough people'), ('基本不管', "doesn't really care the attendance"), ('纯看心情', "depends on the days or professor's mood")], default='未知', max_length=30)),
                ('prof_personality_tag', models.CharField(max_length=50, null=True)),
                ('student_learning_tag', models.CharField(max_length=50, null=True)),
                ('class_atmosphere_tag', models.CharField(max_length=30, null=True)),
                ('homework_requirement_tag', models.CharField(max_length=30, null=True)),
                ('teaching_style_tag', models.CharField(max_length=30, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('prof_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searchings.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=20)),
                ('school_introduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SpecificClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_section', models.IntegerField()),
                ('class_code', models.IntegerField()),
                ('class_period', models.CharField(max_length=20)),
                ('class_remain_seat', models.IntegerField()),
                ('class_introduction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searchings.GeneralClass')),
            ],
        ),
        migrations.AddField(
            model_name='professor',
            name='prof_school',
            field=models.ManyToManyField(to='searchings.School'),
        ),
        migrations.AddField(
            model_name='post',
            name='rating_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searchings.Rating'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='generalclass',
            name='class_major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searchings.Major'),
        ),
        migrations.AddField(
            model_name='generalclass',
            name='class_prof',
            field=models.ManyToManyField(to='searchings.Professor'),
        ),
    ]
