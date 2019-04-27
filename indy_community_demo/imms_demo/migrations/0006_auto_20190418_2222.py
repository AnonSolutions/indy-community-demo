# Generated by Django 2.2 on 2019-04-18 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indy_community', '0007_auto_20190413_0125'),
        ('imms_demo', '0005_auto_20190418_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repoimmunizationconversation',
            name='imms_consent_request',
        ),
        migrations.RemoveField(
            model_name='schoolimmunizationconversation',
            name='consent_enablement',
        ),
        migrations.RemoveField(
            model_name='schoolimmunizationconversation',
            name='health_id_proof',
        ),
        migrations.AddField(
            model_name='repoimmunizationconversation',
            name='imms_consent_proof',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imms_consent_proof', to='indy_community.AgentConversation'),
        ),
        migrations.AddField(
            model_name='schoolimmunizationconversation',
            name='consent_enablement_offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consent_enablement_offer', to='indy_community.AgentConversation'),
        ),
        migrations.AddField(
            model_name='schoolimmunizationconversation',
            name='health_id_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='health_id_request', to='indy_community.AgentConversation'),
        ),
        migrations.CreateModel(
            name='UserImmunizationConversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_id', models.CharField(max_length=60)),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=80, null=True)),
                ('first_name_parent', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name_parent', models.CharField(blank=True, max_length=80, null=True)),
                ('status', models.CharField(max_length=20)),
                ('msg', models.CharField(blank=True, max_length=200, null=True)),
                ('initiation_date', models.DateField()),
                ('consent_enablement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consent_enablement', to='indy_community.AgentConversation')),
                ('health_id_proof', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='health_id_proof', to='indy_community.AgentConversation')),
                ('imms_consent_request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imms_consent_request', to='indy_community.AgentConversation')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indy_community.IndyWallet', to_field='wallet_name')),
            ],
        ),
    ]