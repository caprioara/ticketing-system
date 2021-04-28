# Generated by Django 3.1.7 on 2021-04-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_ticket_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('In asteptare', 'In asteptare'), ('In lucru', 'In lucru'), ('Terminate', 'Terminate')], default='In asteptare', max_length=50),
        ),
    ]