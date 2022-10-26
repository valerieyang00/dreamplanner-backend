# Generated by Django 4.1.2 on 2022-10-26 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('budget', models.FloatField()),
                ('photo', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('transportation', 'Transportation'), ('lodging', 'Lodging'), ('food', 'Food'), ('activities', 'Activities'), ('misc', 'Miscellaneous')], max_length=50)),
                ('merchant', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('details', models.CharField(max_length=250)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='dreamplanner.destination')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='dreamplanner.user')),
            ],
        ),
        migrations.AddField(
            model_name='destination',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='dreamplanner.user'),
        ),
    ]
