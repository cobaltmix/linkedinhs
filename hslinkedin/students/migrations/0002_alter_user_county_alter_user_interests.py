# Generated by Django 4.2.5 on 2024-09-12 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='county',
            field=models.CharField(choices=[('US001', 'Autauga County'), ('US003', 'Baldwin County')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='interests',
            field=models.CharField(choices=[('sports', 'Sports'), ('music', 'Music'), ('technology', 'Technology'), ('reading', 'Reading'), ('traveling', 'Traveling')], max_length=20),
        ),
    ]
