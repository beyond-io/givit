# Generated by Django 3.1.1 on 2020-09-13 19:08

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.BooleanField(
                    default=False, verbose_name='confirmed')),
                ('student_id', models.CharField(max_length=10, validators=[
                 django.core.validators.RegexValidator(message='ID must be 9 digits long.', regex='[0-9]{8,9}')])),
                ('gender', models.CharField(choices=[
                 ('male', 'male'), ('female', 'female'), ('other', 'other')], default='other', max_length=10)),
                ('phone_number', models.CharField(help_text='example: 0544544554', max_length=10, validators=[django.core.validators.RegexValidator(
                    message='Phone number must be entered in the format: 05XXXXXXXX.', regex='^05[0-68-9][0-9]{7}$')])),
                ('date_of_birth', models.DateField(
                    help_text='mm/dd/yyyy', max_length=8)),
                ('address_street_name', models.CharField(
                    max_length=50, verbose_name='street')),
                ('address_house_number', models.CharField(
                    max_length=3, verbose_name='home_number')),
                ('address_city', models.CharField(
                    max_length=50, verbose_name='city')),
                ('field_of_study', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Business', 'Business'), ('Sustainability', 'Sustainability'), ('Communications', 'Communications'), (
                    'Economics', 'Economics'), ('Law', 'Law'), ('Psychology', 'Communications'), ('Government, Diplomacy and Strategy', 'Government, Diplomacy and Strategy')], default='Computer Science', max_length=100)),
                ('degree', models.CharField(choices=[('BA', 'BA'), ('BSC', 'BSC'), (
                    'MA', 'MA'), ('MSC', 'MSC'), ('PHD', 'PHD')], default='BA', max_length=100)),
                ('scholarship', models.CharField(max_length=100)),
                ('membership_type', models.CharField(choices=[
                 ('friend', 'friend'), ('coordinator', 'coordinator')], default='friend', max_length=100)),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
