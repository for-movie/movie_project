# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-12 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('is_supper', models.BooleanField(default=False, verbose_name='超级管理员')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Adminlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, verbose_name='登录IP')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='登录时间')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Admin', verbose_name='管理员')),
            ],
        ),
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='权限名')),
                ('url', models.CharField(max_length=255, unique=True, verbose_name='地址')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='电影名')),
                ('url', models.CharField(max_length=255, unique=True, verbose_name='地址')),
                ('info', models.TextField(verbose_name='简介')),
                ('logo', models.CharField(max_length=255, unique=True, verbose_name='封面')),
                ('star', models.IntegerField(verbose_name='星级')),
                ('playnum', models.IntegerField(verbose_name='播放量')),
                ('commentnum', models.IntegerField(verbose_name='评论量')),
                ('area', models.CharField(max_length=100, verbose_name='上映地区')),
                ('release_time', models.DateField(blank=True, null=True, verbose_name='上映时间')),
                ('lenght', models.CharField(max_length=15, verbose_name='播放时长')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Moviecol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Movie', verbose_name='电影名')),
            ],
        ),
        migrations.CreateModel(
            name='Oplog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, verbose_name='登录IP')),
                ('reason', models.CharField(max_length=600, verbose_name='操作原因')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='登录时间')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Admin', verbose_name='管理员')),
            ],
        ),
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='电影名')),
                ('logo', models.CharField(max_length=100, unique=True, verbose_name='封面')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='名称')),
                ('auths', models.CharField(max_length=600, verbose_name='权限列表')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='标签名')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('nickname', models.CharField(max_length=100, verbose_name='昵称')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='电话')),
                ('info', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('face', models.CharField(max_length=100, unique=True, verbose_name='头像')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('uuid', models.CharField(max_length=100, unique=True, verbose_name='唯一标识符')),
            ],
        ),
        migrations.CreateModel(
            name='Userlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, verbose_name='登录IP')),
                ('addtime', models.DateField(auto_now_add=True, verbose_name='登录时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.User', verbose_name='所属会员')),
            ],
        ),
        migrations.AddField(
            model_name='moviecol',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Tag', verbose_name='所属标签'),
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Movie', verbose_name='电影名'),
        ),
        migrations.AddField(
            model_name='comment',
            name='preview',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Preview', verbose_name='预告'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='admin',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Role', verbose_name='角色'),
        ),
    ]