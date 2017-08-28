# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 10:20
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semester_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='semester',
            name='updated_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semester_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companyinterest',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companyinterest_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companyinterest',
            name='semesters',
            field=models.ManyToManyField(blank=True, to='companies.Semester'),
        ),
        migrations.AddField(
            model_name='companyinterest',
            name='updated_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companyinterest_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companycontact',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_contacts', to='companies.Company'),
        ),
        migrations.AddField(
            model_name='companycontact',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companycontact_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companycontact',
            name='updated_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companycontact_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='previous_contacts',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='student_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='updated_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='semesterstatus',
            unique_together=set([('semester', 'company')]),
        ),
        migrations.AlterUniqueTogether(
            name='semester',
            unique_together=set([('year', 'semester')]),
        ),
    ]
