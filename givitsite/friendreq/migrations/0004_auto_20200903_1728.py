# Generated by Django 3.1 on 2020-09-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendreq', '0003_auto_20200902_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsfound',
            name='match',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='itemrequest',
            name='item',
            field=models.CharField(choices=[('20009', 'closet'), ('20016', 'bed'), ('20008', 'chair'), (
                '10006', 'fridge'), ('10029', 'Washing machine'), ('20017', 'sofa')], default='20009', max_length=40),
        ),
    ]
