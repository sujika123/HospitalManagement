# Generated by Django 4.2.6 on 2023-11-22 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Start_time', models.TimeField()),
                ('End_time', models.TimeField()),
                ('Doc_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospitalapp.doctor')),
            ],
        ),
    ]
