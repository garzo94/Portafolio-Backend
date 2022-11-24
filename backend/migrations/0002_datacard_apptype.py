# Generated by Django 4.1.3 on 2022-11-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacard',
            name='appType',
            field=models.CharField(choices=[('web', 'Web development'), ('mobile', 'Mobile development'), ('ml', 'Machine Learning')], default='web', max_length=20),
        ),
    ]