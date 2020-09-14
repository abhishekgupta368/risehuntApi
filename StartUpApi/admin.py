from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StartUpOwner)
admin.site.register(StartUpTeam)
admin.site.register(StartUpDetails)
admin.site.register(StartUpLegal)
admin.site.register(StartUpCatorgery)

admin.site.register(InvestorInformation)
admin.site.register(InvestorProfessionalExperience)
admin.site.register(InvestorSkillsExperience)
admin.site.register(InvestorPosition)
admin.site.register(InvestmentDetail)
admin.site.register(IndustrialInvestment)