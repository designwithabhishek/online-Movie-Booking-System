# Generated by Django 2.2.3 on 2019-07-18 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditorium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audi_name', models.CharField(max_length=40)),
                ('seat_count', models.IntegerField()),
                ('audi_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cover_page', models.ImageField(default=False, null=True, upload_to='movies')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('show_time', models.DateTimeField()),
                ('layout', models.AutoField(primary_key=True, serialize=False)),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('message', models.TextField()),
                ('image', models.ImageField(default='adult-boy-casual-220453.jpg', upload_to='user')),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Layouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.IntegerField()),
                ('row', models.CharField(max_length=1)),
                ('layout_no', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('auditorium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Auditorium')),
            ],
        ),
        migrations.CreateModel(
            name='Audi_layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.IntegerField()),
                ('row', models.CharField(max_length=1)),
                ('auditorium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Auditorium')),
            ],
        ),
    ]
