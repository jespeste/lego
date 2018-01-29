# Generated by Django 2.0 on 2018-01-29 21:51

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0013_auto_20171210_1610'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    )
                ),
                (
                    'updated_at',
                    models.DateTimeField(default=django.utils.timezone.now, editable=False)
                ),
                ('deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('answer_text', models.TextField(blank=True, default='', max_length=255)),
                (
                    'created_by',
                    models.ForeignKey(
                        default=None, editable=False, null=True,
                        on_delete=django.db.models.deletion.SET_NULL, related_name='answer_created',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
            options={
                'abstract': False,
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    )
                ),
                (
                    'updated_at',
                    models.DateTimeField(default=django.utils.timezone.now, editable=False)
                ),
                ('deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('option_text', models.TextField(default='', max_length=255)),
                (
                    'created_by',
                    models.ForeignKey(
                        default=None, editable=False, null=True,
                        on_delete=django.db.models.deletion.SET_NULL, related_name='option_created',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
            options={
                'abstract': False,
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    )
                ),
                (
                    'updated_at',
                    models.DateTimeField(default=django.utils.timezone.now, editable=False)
                ),
                ('deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                (
                    'question_type',
                    models.CharField(
                        choices=[
                            ('single_choice', 'single_choice'),
                            ('multiple_choice', 'multiple_choice'), ('text_field', 'text_field')
                        ], max_length=64
                    )
                ),
                ('question_text', models.TextField(max_length=255)),
                ('mandatory', models.BooleanField(default=False)),
                ('relative_index', models.IntegerField(default=1)),
                (
                    'created_by',
                    models.ForeignKey(
                        default=None, editable=False, null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='question_created', to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
            options={
                'ordering': ['relative_index'],
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    )
                ),
                (
                    'updated_at',
                    models.DateTimeField(default=django.utils.timezone.now, editable=False)
                ),
                ('deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                (
                    'created_by',
                    models.ForeignKey(
                        default=None, editable=False, null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='submission_created', to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    )
                ),
                (
                    'updated_at',
                    models.DateTimeField(default=django.utils.timezone.now, editable=False)
                ),
                ('deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('title', models.CharField(max_length=100)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                (
                    'template_type',
                    models.CharField(
                        blank=True, choices=[
                            ('company_presentation',
                             'company_presentation'), ('lunch_presentation', 'lunch_presentation'),
                            ('course', 'course'), ('kid_event', 'kid_event'), ('party', 'party'),
                            ('social', 'social'), ('other', 'other'), ('event', 'event')
                        ], max_length=30, null=True
                    )
                ),
                (
                    'created_by',
                    models.ForeignKey(
                        default=None, editable=False, null=True,
                        on_delete=django.db.models.deletion.SET_NULL, related_name='survey_created',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
                (
                    'event',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to='events.Event'
                    )
                ),
                (
                    'updated_by',
                    models.ForeignKey(
                        default=None, editable=False, null=True,
                        on_delete=django.db.models.deletion.SET_NULL, related_name='survey_updated',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
            options={
                'abstract': False,
                'default_manager_name': 'objects',
            },
        ),
        migrations.AddField(
            model_name='submission',
            name='survey',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='submissions',
                to='surveys.Survey'
            ),
        ),
        migrations.AddField(
            model_name='submission',
            name='updated_by',
            field=models.ForeignKey(
                default=None, editable=False, null=True,
                on_delete=django.db.models.deletion.SET_NULL, related_name='submission_updated',
                to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='surveys',
                to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='questions',
                to='surveys.Survey'
            ),
        ),
        migrations.AddField(
            model_name='question',
            name='updated_by',
            field=models.ForeignKey(
                default=None, editable=False, null=True,
                on_delete=django.db.models.deletion.SET_NULL, related_name='question_updated',
                to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='options',
                to='surveys.Question'
            ),
        ),
        migrations.AddField(
            model_name='option',
            name='updated_by',
            field=models.ForeignKey(
                default=None, editable=False, null=True,
                on_delete=django.db.models.deletion.SET_NULL, related_name='option_updated',
                to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='answers',
                to='surveys.Question'
            ),
        ),
        migrations.AddField(
            model_name='answer',
            name='selected_options',
            field=models.ManyToManyField(
                blank=True, related_name='selected_in_answers', to='surveys.Option'
            ),
        ),
        migrations.AddField(
            model_name='answer',
            name='submission',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='answers',
                to='surveys.Submission'
            ),
        ),
        migrations.AddField(
            model_name='answer',
            name='updated_by',
            field=models.ForeignKey(
                default=None, editable=False, null=True,
                on_delete=django.db.models.deletion.SET_NULL, related_name='answer_updated',
                to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterUniqueTogether(
            name='submission',
            unique_together={('survey', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('survey', 'relative_index')},
        ),
    ]
