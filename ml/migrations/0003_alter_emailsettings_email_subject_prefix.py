# Generated by Django 5.0.6 on 2024-08-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0002_emailsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsettings',
            name='email_subject_prefix',
            field=models.CharField(default='QuickDiag', max_length=255),
        ),
    ]