# Generated by Django 3.1.6 on 2021-02-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210207_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo_post',
            field=models.TextField(verbose_name='Conteudo'),
        ),
    ]
