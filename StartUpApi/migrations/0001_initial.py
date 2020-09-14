# Generated by Django 3.0.8 on 2020-09-09 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvestorInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_experience', models.IntegerField()),
                ('company_invested', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StartUpOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('background', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StartUpTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_size', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_team_size', to='StartUpApi.StartUpOwner')),
            ],
        ),
        migrations.CreateModel(
            name='StartUpLegal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_entity_information', models.BooleanField()),
                ('incorporated_company_name', models.BooleanField()),
                ('patents_filed', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_legal', to='StartUpApi.StartUpOwner')),
            ],
        ),
        migrations.CreateModel(
            name='StartUpDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_up_name', models.CharField(max_length=100)),
                ('start_up_url', models.URLField()),
                ('start_up_description', models.TextField(max_length=60)),
                ('start_up_product_detail', models.TextField(max_length=300)),
                ('start_up_handler', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_details', to='StartUpApi.StartUpOwner')),
            ],
        ),
        migrations.CreateModel(
            name='StartUpCatorgery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_targeted', models.CharField(max_length=100)),
                ('start_up_technology_catergory', models.CharField(max_length=100)),
                ('start_up_stage', models.CharField(max_length=100)),
                ('start_up_usecase', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_catorgery', to='StartUpApi.StartUpOwner')),
            ],
        ),
        migrations.CreateModel(
            name='InvestorSkillsExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor_skills', models.CharField(max_length=100)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investor_skill_experience', to='StartUpApi.InvestorInformation')),
            ],
        ),
        migrations.CreateModel(
            name='InvestorProfessionalExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor_catorgery', models.CharField(max_length=100)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investor_profressional_experience', to='StartUpApi.InvestorInformation')),
            ],
        ),
        migrations.CreateModel(
            name='InvestorPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor_position', models.CharField(max_length=100)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investor_position', to='StartUpApi.InvestorInformation')),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor_company_stage', models.CharField(max_length=100)),
                ('investor_company_relaion', models.CharField(max_length=100)),
                ('investment_range', models.CharField(max_length=100)),
                ('form_of_investment', models.CharField(max_length=100)),
                ('general_expectation', models.CharField(max_length=100)),
                ('historical_rate_returns', models.CharField(max_length=100)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investor_detail', to='StartUpApi.InvestorInformation')),
            ],
        ),
        migrations.CreateModel(
            name='IndustrialInvestment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_domain', models.CharField(max_length=100)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='industrial_investment_details', to='StartUpApi.InvestmentDetail')),
            ],
        ),
    ]