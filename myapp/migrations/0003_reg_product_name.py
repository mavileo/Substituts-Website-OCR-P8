# Generated by Django 2.1.7 on 2019-04-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190417_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg_product',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
