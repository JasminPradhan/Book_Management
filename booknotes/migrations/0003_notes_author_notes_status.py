# Generated by Django 5.0.4 on 2024-06-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booknotes', '0002_notes_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='author',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='status',
            field=models.CharField(choices=[('TBR', 'To be Read'), ('RNG', 'Reading'), ('RD', 'Read')], max_length=3, null=True),
        ),
    ]
