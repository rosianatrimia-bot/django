from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosmed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AkunSosmed',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('nama_depan', models.CharField(max_length=100)),
                ('nama_belakang', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                (
                    'platform',
                    models.CharField(
                        max_length=20,
                        choices=[
                            ('instagram', 'Instagram'),
                            ('tiktok', 'TikTok'),
                            ('facebook', 'Facebook'),
                            ('twitter', 'X / Twitter'),
                        ]
                    )
                ),
            ],
        ),
    ]
