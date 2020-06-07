# Generated by Django 2.2.3 on 2019-08-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20190803_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('character', models.CharField(max_length=30)),
                ('cast_image', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='movies',
            name='cast',
            field=models.ManyToManyField(to='booking.Cast'),
        ),
    ]