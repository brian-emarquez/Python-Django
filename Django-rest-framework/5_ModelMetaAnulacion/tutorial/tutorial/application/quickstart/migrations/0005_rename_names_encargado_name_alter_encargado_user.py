# Generated by Django 4.0.4 on 2022-05-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelRelacion', '0002_alter_membership_invite_reason'),
        ('quickstart', '0004_encargado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encargado',
            old_name='names',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='encargado',
            name='user',
            field=models.ManyToManyField(to='modelRelacion.person'),
        ),
    ]
