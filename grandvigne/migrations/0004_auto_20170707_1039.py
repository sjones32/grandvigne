# Generated by Django 2.0.dev20170614170706 on 2017-07-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandvigne', '0003_auto_20170705_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='levelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_option', models.CharField(default='SOME STRING', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='interactionstatement',
            name='vignette',
        ),
        migrations.RemoveField(
            model_name='levels',
            name='vignette',
        ),
        migrations.RemoveField(
            model_name='descriptionstatement',
            name='vignette',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='vignette',
        ),
        migrations.RemoveField(
            model_name='vignette',
            name='level_count',
        ),
        migrations.RemoveField(
            model_name='vignette',
            name='level_option',
        ),
        migrations.RemoveField(
            model_name='vignette',
            name='variable_text',
        ),
        migrations.AddField(
            model_name='descriptionstatement',
            name='variable_text',
            field=models.ManyToManyField(blank=True, to='grandvigne.Variable'),
        ),
        migrations.AlterField(
            model_name='descriptionstatement',
            name='description_text',
            field=models.CharField(max_length=200),
        ),
        migrations.RemoveField(
            model_name='vignette',
            name='description_text',
        ),
        migrations.AddField(
            model_name='vignette',
            name='description_text',
            field=models.ManyToManyField(blank=True, to='grandvigne.descriptionStatement'),
        ),
        migrations.DeleteModel(
            name='interactionStatement',
        ),
        migrations.DeleteModel(
            name='Levels',
        ),
        migrations.AddField(
            model_name='variable',
            name='levels',
            field=models.ManyToManyField(blank=True, to='grandvigne.levelModel'),
        ),
    ]
