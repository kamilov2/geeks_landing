# Generated by Django 4.2.16 on 2024-10-15 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_course_description_alter_course_is_modern_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursedescription',
            options={},
        ),
        migrations.AddField(
            model_name='lead',
            name='course',
            field=models.ForeignKey(default=0, help_text='Курсни танланг', on_delete=django.db.models.deletion.CASCADE, to='main.course', verbose_name='Курс'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursedescription',
            name='course',
            field=models.ForeignKey(help_text='Курсни танланг', on_delete=django.db.models.deletion.CASCADE, related_name='coursedescription', to='main.course', verbose_name='Курс'),
        ),
    ]
