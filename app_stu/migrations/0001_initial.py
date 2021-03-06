# Generated by Django 3.0.6 on 2020-05-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('student_fname', models.CharField(max_length=50)),
                ('student_lname', models.CharField(max_length=50)),
                ('mark', models.IntegerField()),
                ('mail_id', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
            ],
            options={
                'db_table': 'std_table',
            },
        ),
    ]
