# Generated by Django 2.2.3 on 2019-08-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20190803_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='cast_image',
            field=models.TextField(null=True),
        ),
    ]