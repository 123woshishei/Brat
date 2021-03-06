# Generated by Django 2.1.1 on 2018-09-28 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('World', '0003_auto_20180928_0401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='label_relationship',
            name='lr_entity',
        ),
        migrations.AddField(
            model_name='label_relationship',
            name='lr_labelA',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lr_labelA_set', to='World.Label', verbose_name='标签A'),
        ),
        migrations.AddField(
            model_name='label_relationship',
            name='lr_labelB',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lr_labelB_set', to='World.Label', verbose_name='标签B'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='entity_name',
            field=models.CharField(max_length=32, verbose_name='实体名称'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relationship_entities',
            field=models.ManyToManyField(through='World.Label_RelationShip', to='World.RelationShip'),
        ),
    ]
