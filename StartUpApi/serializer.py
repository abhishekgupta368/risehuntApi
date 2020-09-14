from rest_framework import serializers
from .models import *

class StartUpOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartUpOwner
        fields = "__all__"

class StartUpTeamSerializer(serializers.ModelSerializer):
    owner_team_size = StartUpOwnerSerializer(many=True, read_only=True)
    class Meta:
        model = StartUpTeam
        fields = "__all__"

class StartUpDetailsSerializer(serializers.ModelSerializer):
    owner_details = StartUpOwnerSerializer(many=True, read_only=True)
    class Meta:
        model = StartUpDetails
        fields = "__all__"

class StartUpCatorgerySerializer(serializers.ModelSerializer):
    owner_catorgery = StartUpOwnerSerializer(many=True, read_only=True)
    class Meta:
        model = StartUpCatorgery
        fields = "__all__"

class StartUpLegalSerializer(serializers.ModelSerializer):
    owner_legal = StartUpOwnerSerializer(many=True, read_only=True)
    class Meta:
        model = StartUpLegal
        fields = "__all__"

#######################################################################

class InvestorInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorInformation
        fields = "__all__"

class InvestorProfessionalExperienceSerializer(serializers.ModelSerializer):
    investor_profressional_experience = InvestorInformationSerializer(many=True, read_only=True)    
    class Meta:
        model = InvestorProfessionalExperience
        fields = "__all__"  

class InvestorSkillsExperienceSerializer(serializers.ModelSerializer):
    investor_skill_experience = InvestorInformationSerializer(many=True, read_only=True)    
    class Meta:
        model = InvestorSkillsExperience
        fields = "__all__"  

class InvestorPositionSerializer(serializers.ModelSerializer):
    investor_position = InvestorInformationSerializer(many=True, read_only=True)    
    class Meta:
        model = InvestorPosition
        fields = "__all__"  

class InvestmentDetailSerializer(serializers.ModelSerializer):
    investor_detail = InvestorInformationSerializer(many=True, read_only=True)    
    class Meta:
        model = InvestmentDetail
        fields = "__all__"  

class IndustrialInvestmentSerializer(serializers.ModelSerializer):
    industrial_investment_details = InvestorInformationSerializer(many=True, read_only=True)
    class Meta:
        model = IndustrialInvestment
        fields = "__all__" 
