# Generated by Django 2.0.5 on 2018-05-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_faq_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(default='Not Answered', max_length=1000),
        ),
    ]
