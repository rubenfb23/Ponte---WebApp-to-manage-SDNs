# Generated by Django 5.0.1 on 2024-02-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponte', '0004_alter_red_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='ip_privada',
            field=models.CharField(default='192.168.0.122', max_length=20),
            preserve_default=False,
        ),
    ]