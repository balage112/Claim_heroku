# Generated by Django 4.1.1 on 2022-10-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0004_alter_claim_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='file',
            field=models.ImageField(upload_to='images/'),
        ),
    ]