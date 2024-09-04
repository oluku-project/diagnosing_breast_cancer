# Generated by Django 5.0.6 on 2024-08-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_backend', models.CharField(default='django.core.mail.backends.smtp.EmailBackend', max_length=255)),
                ('email_host', models.CharField(default='smtp.example.com', max_length=255)),
                ('email_port', models.IntegerField(default=587)),
                ('email_use_tls', models.BooleanField(default=True)),
                ('email_use_ssl', models.BooleanField(default=False)),
                ('email_host_user', models.CharField(max_length=255)),
                ('email_host_password', models.CharField(max_length=255)),
                ('default_from_email', models.EmailField(default='info.quickdiag@gmail.com', max_length=254)),
                ('email_subject_prefix', models.CharField(default='[QuickDiag', max_length=255)),
            ],
        ),
    ]