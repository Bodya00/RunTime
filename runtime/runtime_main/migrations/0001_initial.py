# Generated by Django 2.0.5 on 2018-05-22 22:29

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=56)),
                ('l_name', models.CharField(max_length=56)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField(default=0)),
                ('height', models.PositiveIntegerField(default=0)),
                ('age', models.PositiveIntegerField(default=0)),
                ('food_hours', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(1)])),
                ('food_calories', models.PositiveIntegerField(default=0)),
                ('active_hours', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('activity_rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('comfort_rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('sleep_hours', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(1)])),
                ('sleep_duration', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(1)])),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 5, 22, 22, 29, 19, 424150))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to='runtime_main.MyUser')),
            ],
        ),
    ]
