# Generated by Django 5.0.4 on 2024-06-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booknotes', '0003_notes_author_notes_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='status',
            field=models.CharField(choices=[('To be Read', 'To be Read'), ('Reading', 'Reading'), ('Read', 'Read')], max_length=10, null=True),
        ),
    ]