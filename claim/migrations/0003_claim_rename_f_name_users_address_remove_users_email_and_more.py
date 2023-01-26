# Generated by Django 4.1.1 on 2022-10-04 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0002_rename_claim_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter a brief description of the claim', max_length=500)),
                ('price', models.IntegerField()),
                ('date_of_purchase', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(auto_now_add=True)),
                ('purchased', models.BooleanField(default=False)),
                ('remaining_ammount', models.IntegerField(default=0)),
                ('file', models.TextField(blank=True, null=True)),
                ('total_claim_ammount', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-due_date'],
            },
        ),
        migrations.RenameField(
            model_name='users',
            old_name='f_name',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='l_name',
        ),
        migrations.AddField(
            model_name='users',
            name='customer_has_claim',
            field=models.ManyToManyField(to='claim.claim'),
        ),
    ]