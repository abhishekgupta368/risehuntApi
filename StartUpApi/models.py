from django.db import models

# Create your models here.
class StartUpOwner(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    background = models.CharField(max_length=100)

    def __str__(self):
        return self.email_id

class StartUpTeam(models.Model):
    owner = models.ForeignKey(StartUpOwner,related_name="owner_team_size", on_delete=models.CASCADE)
    team_size = models.CharField(max_length=100)

    def __str__(self):
        return self.owner.email_id

class StartUpDetails(models.Model):
    owner = models.ForeignKey(StartUpOwner,related_name="owner_details", on_delete=models.CASCADE)
    start_up_name = models.CharField(max_length=100)
    start_up_url = models.URLField(max_length=200)
    start_up_description = models.TextField(max_length=60)
    start_up_product_detail = models.TextField(max_length=300)
    start_up_handler = models.CharField(max_length=100)

    def __str__(self):
        return self.owner.email_id 

class StartUpCatorgery(models.Model):
    owner = models.ForeignKey(StartUpOwner, related_name="owner_catorgery", on_delete=models.CASCADE)
    customer_targeted = models.CharField(max_length=100)
    start_up_technology_catergory = models.CharField(max_length=100)
    start_up_stage = models.CharField(max_length=100)
    start_up_usecase = models.CharField(max_length=100)

    def __str__(self):
        return self.owner.email_id

class StartUpLegal(models.Model):
    owner = models.ForeignKey(StartUpOwner,related_name="owner_legal", on_delete=models.CASCADE)
    legal_entity_information = models.BooleanField()
    incorporated_company_name = models.BooleanField()
    patents_filed = models.BooleanField()

    def __str__(self):
        return self.owner.email_id

############################### Investor Database ####################################

class InvestorInformation(models.Model):
    name = models.CharField(max_length=100,null=True)
    email_id = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    mobile_number = models.CharField(max_length=100,null=True)
    year_of_experience = models.CharField(max_length=100,null=True)
    company_invested = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.email_id

class InvestorProfessionalExperience(models.Model):
    investor = models.ForeignKey(InvestorInformation,related_name="investor_profressional_experience",on_delete=models.CASCADE)
    investor_catorgery = models.CharField(max_length=100)

    def __str__(self):
        return "Investor "+str(self.investor.email_id)

class InvestorSkillsExperience(models.Model):
    investor = models.ForeignKey(InvestorInformation,related_name="investor_skill_experience", on_delete=models.CASCADE)
    investor_skills = models.CharField(max_length=100)

    def __str__(self):
        return "Investor "+str(self.investor.email_id)

class InvestorPosition(models.Model):
    investor = models.ForeignKey(InvestorInformation,related_name="investor_position", on_delete=models.CASCADE)
    position = models.CharField(max_length=100,null=False)

    def __str__(self):
        return "Investor "+str(self.investor.email_id)

class InvestmentDetail(models.Model):
    investor = models.ForeignKey(InvestorInformation,related_name="investor_detail", on_delete=models.CASCADE)
    investor_company_stage = models.CharField(max_length=100)
    investor_company_relation = models.CharField(max_length=100)
    investment_range = models.CharField(max_length=100)
    form_of_investment = models.CharField(max_length=100)

    general_expectation = models.CharField(max_length=100)
    historical_rate_returns = models.CharField(max_length=100)

    def __str__(self):
        return "Investor "+str(self.investor.email_id)

class IndustrialInvestment(models.Model):
    investor = models.ForeignKey(InvestorInformation,related_name="industrial_investment_details", on_delete=models.CASCADE)
    investment_domain = models.CharField(max_length=100)

    def __str__(self):
        return "Investor "+str(self.investor.email_id)
