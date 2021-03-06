# Generated by Django 3.0.5 on 2020-08-19 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhisicalExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(choices=[('stan dobry', 'stan dobry'), ('stan średni', 'stan średni'), ('stan ciężki', 'stan ciężki')], max_length=255)),
                ('p2', models.CharField(max_length=255)),
                ('p3', models.CharField(max_length=255)),
                ('p4', models.CharField(max_length=255)),
                ('p5', models.CharField(choices=[('normosteniczna', 'normosteniczna'), ('hyposteniczna', 'hyposteniczna'), ('hypersteniczna', 'hypersteniczna')], max_length=255)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralAnamnesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w1', models.CharField(default='do rozważenia dosłowny zapis pierwszych zdań pacjenta', max_length=1000)),
                ('w2', models.CharField(max_length=255)),
                ('w3a', models.CharField(choices=[('obecne', 'obecne'), ('nieobecne', 'nieobecne')], max_length=255)),
                ('w3b', models.CharField(max_length=255)),
                ('w4', models.CharField(max_length=255)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
            ],
        ),
    ]
