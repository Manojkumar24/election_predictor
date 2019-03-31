# Generated by Django 2.1.7 on 2019-03-31 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_auto_20190331_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=200)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Party')),
            ],
        ),
    ]
