# Generated by Django 2.0.2 on 2018-03-19 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('summary', models.TextField(help_text='Enter a brief description of the topic', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('summary', models.TextField(help_text='Enter a brief description of the topic', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('summary', models.TextField(help_text='Enter a brief description of the topic', max_length=1000)),
                ('lesson', models.ForeignKey(help_text='Add lessons for this topic', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Lesson')),
                ('tag', models.ManyToManyField(help_text='Add tags for this topic', to='catalog.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='tag',
            field=models.ManyToManyField(help_text='Add tags for this topic', to='catalog.Tag'),
        ),
    ]
