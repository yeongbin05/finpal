# Generated by Django 4.2.4 on 2023-11-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RESULT', models.IntegerField()),
                ('CUR_UNIT', models.CharField(max_length=200)),
                ('CUR_NM', models.CharField(max_length=200)),
                ('TTB', models.CharField(max_length=200)),
                ('TTS', models.CharField(max_length=200)),
                ('DEAL_BAS_R', models.CharField(max_length=200)),
                ('BKPR', models.CharField(max_length=200)),
                ('YY_EFEE_R', models.CharField(max_length=200)),
                ('TEN_DD_EFEE_R', models.CharField(max_length=200)),
                ('KFTC_DEAL_BAS_R', models.CharField(max_length=200)),
                ('KFTC_BKPR', models.CharField(max_length=200)),
            ],
        ),
    ]
