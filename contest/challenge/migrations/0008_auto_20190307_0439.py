# Generated by Django 2.1.7 on 2019-03-07 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0007_auto_20190307_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='filepath',
            field=models.FileField(default='', upload_to='submit_files/', verbose_name=''),
        ),
    ]
