# Generated by Django 5.1.7 on 2025-03-10 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_account_groups_account_is_active_account_is_admin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='desciption',
            new_name='description',
        ),
    ]
