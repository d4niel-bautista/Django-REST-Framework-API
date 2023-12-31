# Generated by Django 4.2.3 on 2023-07-07 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificationsinfo',
            name='person_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='app.generalinfo'),
        ),
        migrations.AlterField(
            model_name='charreferencesinfo',
            name='person_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char_references', to='app.generalinfo'),
        ),
        migrations.AlterField(
            model_name='educationinfo',
            name='person_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educ', to='app.generalinfo'),
        ),
        migrations.AlterField(
            model_name='seminarsinfo',
            name='person_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seminars', to='app.generalinfo'),
        ),
        migrations.AlterField(
            model_name='skillsinfo',
            name='person_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='app.generalinfo'),
        ),
        migrations.AlterField(
            model_name='strengthsinfo',
            name='person_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strengths', to='app.generalinfo'),
        ),
    ]
