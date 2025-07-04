# Generated by Django 5.1.7 on 2025-05-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeekerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('bio', models.CharField(default='add bio', max_length=1000)),
                ('interview', models.IntegerField(blank=True, null=True)),
                ('cv', models.FileField(upload_to='media/seeker/')),
            ],
            options={
                'verbose_name_plural': 'Job Seeker Model',
            },
        ),
    ]
