# Generated by Django 5.2.1 on 2025-06-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('egcs', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('ercs', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('errAtt', models.IntegerField(blank=True, default=None, null=True)),
                ('erInv', models.IntegerField(blank=True, default=None, null=True)),
                ('erUnq', models.IntegerField(blank=True, default=None, null=True)),
                ('erLop', models.IntegerField(blank=True, default=None, null=True)),
                ('erLmt', models.IntegerField(blank=True, default=None, null=True)),
                ('ecAtt', models.IntegerField(blank=True, default=None, null=True)),
                ('ecBsy', models.IntegerField(blank=True, default=None, null=True)),
                ('ecCng', models.IntegerField(blank=True, default=None, null=True)),
                ('ecCon', models.IntegerField(blank=True, default=None, null=True)),
                ('ecMin', models.IntegerField(blank=True, default=None, null=True)),
                ('eccPDD', models.IntegerField(blank=True, default=None, null=True)),
                ('ecAsr', models.IntegerField(blank=True, default=None, null=True)),
                ('ecAcd', models.IntegerField(blank=True, default=None, null=True)),
                ('erChg', models.IntegerField(blank=True, default=None, null=True)),
                ('ecChg', models.IntegerField(blank=True, default=None, null=True)),
                ('mrgn', models.IntegerField(blank=True, default=None, null=True)),
                ('mpct', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
