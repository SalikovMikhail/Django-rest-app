# Generated by Django 3.1 on 2020-09-24 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('user', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=70)),
                ('description', models.TextField(blank=True)),
                ('release_date', models.DateField(blank=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='author.author')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='category.category')),
                ('lessee', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='user.user')),
            ],
        ),
    ]
