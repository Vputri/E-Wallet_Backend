# Generated by Django 3.2.12 on 2022-03-17 09:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wallet.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_id', models.CharField(default=wallet.models.generate_wallet_id, max_length=17, unique=True, validators=[django.core.validators.MinLengthValidator(17), django.core.validators.MaxLengthValidator(17)])),
                ('is_disabled', models.BooleanField(default=False)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
