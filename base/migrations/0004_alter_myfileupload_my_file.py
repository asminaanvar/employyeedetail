# Generated by Django 4.2.3 on 2023-07-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_myfileupload_my_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfileupload',
            name='my_file',
            field=models.FileField(upload_to=''),
        ),
    ]