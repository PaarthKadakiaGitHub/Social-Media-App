# Generated by Django 3.2.16 on 2023-07-12 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20230712_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='likepost',
            name='f',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.TextField(default='3e2a9fac-ecd0-49bd-a301-d896287590be', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.TextField(default='bb094174-5d2c-47c3-8a4b-059616dda1c4', primary_key=True, serialize=False),
        ),
    ]
