# Generated by Django 5.0.6 on 2024-08-16 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0008_emailsettings_generalsettings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GeneralSettings',
        ),
    ]
