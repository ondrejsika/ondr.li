# Generated by Django 3.1a1 on 2020-06-05 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_suffix', models.CharField(max_length=16)),
                ('target_url', models.URLField()),
                ('utm_source', models.CharField(blank=True, max_length=16, null=True)),
                ('utm_medium', models.CharField(blank=True, max_length=16, null=True)),
                ('utm_term', models.CharField(blank=True, max_length=16, null=True)),
                ('utm_content', models.CharField(blank=True, max_length=16, null=True)),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shortener.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_dt', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('referer', models.URLField()),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.link')),
            ],
        ),
    ]
