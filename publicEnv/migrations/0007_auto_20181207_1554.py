# Generated by Django 2.0.1 on 2018-12-07 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20180814_1419'),
        ('publicEnv', '0006_auto_20181127_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.CharField(default='', max_length=50)),
                ('end_time', models.CharField(default='', max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('ip', models.CharField(default='', max_length=500)),
                ('user', models.CharField(default='', max_length=500)),
                ('passw', models.CharField(default='', max_length=500)),
                ('testlog_path', models.CharField(default='', max_length=500)),
                ('baselog_path', models.CharField(default='', max_length=500)),
                ('testres_list', models.TextField(default='')),
                ('baseres_list', models.TextField(default='')),
                ('errorlog', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='AnalyHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('user', models.CharField(default='', max_length=500)),
                ('passw', models.CharField(default='', max_length=500)),
                ('status', models.IntegerField(default=0)),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analy_user', to='rbac.UserInfo', to_field='username')),
            ],
        ),
        migrations.AddField(
            model_name='analydetail',
            name='h',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analy_host', to='publicEnv.AnalyHost'),
        ),
    ]
