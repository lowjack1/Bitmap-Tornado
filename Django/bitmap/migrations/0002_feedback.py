# Generated by Django 2.1.7 on 2019-03-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitmap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userfb', models.TextField()),
            ],
        ),
    ]
