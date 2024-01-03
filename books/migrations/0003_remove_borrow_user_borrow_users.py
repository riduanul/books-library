# Generated by Django 4.2.7 on 2024-01-03 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_useraccount_borrow_book_and_more'),
        ('books', '0002_category_slug_alter_category_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='user',
        ),
        migrations.AddField(
            model_name='borrow',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.useraccount'),
        ),
    ]
