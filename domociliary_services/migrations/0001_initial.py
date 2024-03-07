# Generated by Django 2.0.9 on 2023-12-21 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allocate_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='areaallocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AREA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.area')),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('feedback', models.CharField(max_length=200)),
                ('CUSTOMER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.customer')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('usertype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='requestss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('CUSTOMER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.customer')),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('CATEGORY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.category')),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffname', models.CharField(max_length=200)),
                ('staffpost', models.CharField(max_length=200)),
                ('staffplace', models.CharField(max_length=200)),
                ('staffpin', models.CharField(max_length=200)),
                ('staffcontact_no', models.CharField(max_length=200)),
                ('staffemail', models.CharField(max_length=200)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.login')),
            ],
        ),
        migrations.AddField(
            model_name='requestss',
            name='SERVICE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.service'),
        ),
        migrations.AddField(
            model_name='payment',
            name='REQUEST',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.requestss'),
        ),
        migrations.AddField(
            model_name='customer',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.login'),
        ),
        migrations.AddField(
            model_name='areaallocation',
            name='STAFF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.staff'),
        ),
        migrations.AddField(
            model_name='allocate_service',
            name='REQUEST',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.requestss'),
        ),
        migrations.AddField(
            model_name='allocate_service',
            name='STAFF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domociliary_services.login'),
        ),
    ]
