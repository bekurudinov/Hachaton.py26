# Generated by Django 4.1.7 on 2023-03-31 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='forgot_password_reset',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]