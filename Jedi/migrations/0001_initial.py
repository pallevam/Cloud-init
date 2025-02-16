# Generated by Django 3.0.8 on 2020-08-27 17:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('efforts', models.DurationField()),
                ('story', models.CharField(choices=[('1', 'In Progress'), ('2', 'Review'), ('3', 'Done')], default=1, max_length=7)),
                ('sprint_dead_line', models.DateField()),
                ('complete_per', models.FloatField(max_length=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('description', models.TextField(blank=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('upd_date', models.DateField(auto_now=True)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=80)),
                ('story', models.CharField(choices=[('1', 'In Progress'), ('2', 'Review'), ('3', 'Done')], default=1, max_length=7)),
                ('due', models.CharField(choices=[('1', 'On Due'), ('2', 'Overdue'), ('3', 'Done')], default=1, max_length=7)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Jedi.Project')),
            ],
            options={
                'ordering': ['project', 'task_name'],
            },
        ),
    ]
