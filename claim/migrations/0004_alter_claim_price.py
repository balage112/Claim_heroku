# Generated by Django 4.1.1 on 2022-10-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0003_claim_rename_f_name_users_address_remove_users_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]