# Generated by Django 2.2.7 on 2020-03-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ['-overdue', 'id', 'department', '-checkout_on']},
        ),
        migrations.AlterField(
            model_name='file',
            name='department',
            field=models.CharField(blank=True, choices=[('Administration', 'Administration'), ('Operation', 'Operation'), ('Development', 'Development'), ('Customer', 'Customer')], max_length=100),
        ),
    ]
