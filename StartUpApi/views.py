from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status 
from .models import *
from .serializer import *
from rest_framework.exceptions import NotFound

# Create your views here.
#http://127.0.0.1:8000/api/start-up-owner/?email_id=?
class StartUpOwnerApi(viewsets.ModelViewSet):
    # queryset = StartUpOwner.objects.all()
    serializer_class =  StartUpOwnerSerializer
    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        if(email!=None):
            try:
                Start_Up_Owner  = StartUpOwner.objects.filter(email_id = email)
                return Start_Up_Owner
            except Exception as e:
                raise NotFound({"message":"not_found"})
        else:
            Start_Up_Owner  = StartUpOwner.objects.all()
            return Start_Up_Owner

    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        request.data['id']= StartUpTeam.objects.count()+1
        request.data['name'] = request.query_params.get('name')
        request.data['email_id'] = request.query_params.get('email_id')
        request.data['password'] = request.query_params.get('password')
        request.data['mobile_number'] = request.query_params.get('mobile_number')
        request.data['background'] = request.query_params.get('background')

        try:
            if(request.data['id']!=None and request.data['name']!=None and request.data['email_id']!=None and request.data['password']!=None and request.data['mobile_number']!=None):
                Start_Up_Owner_Serializer = StartUpOwnerSerializer(data=request.data)
                if(Start_Up_Owner_Serializer.is_valid()):
                    Start_Up_Owner_Serializer.save()
                    return Response(Start_Up_Owner_Serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(Start_Up_Owner_Serializer.data,status=status.HTTP_400_BAD_REQUEST) 
            else:
                raise NotFound({"message":"Not found"})
        except:
            raise NotFound({"message":"Not found","block":"outer_block"})

class StartUpTeamApi(viewsets.ModelViewSet):
    # queryset = StartUpTeam.objects.all()
    serializer_class = StartUpTeamSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        if(email!=None):
            try:
                Start_Up_Owner  = StartUpOwner.objects.get(email_id = email)
                Start_Up_Team = StartUpTeam.objects.filter(owner = Start_Up_Owner.id)
                return Start_Up_Team
            except Exception as e:
                raise NotFound({"message":"not_found"})
            
        else:
            Start_Up_Team  = StartUpTeam.objects.all()
            return Start_Up_Team

    def retrieve(self,request,*args,**kwargs):
        pass
    
    def create(self,request,*args,**kwargs):
        email= request.query_params.get('email_id')
        Start_Up_Owner  = StartUpOwner.objects.get(email_id = email)
        ########################################################
        request.data['id']= StartUpTeam.objects.count()+1
        request.data['team_size'] = request.query_params.get('team_size')
        request.data['owner']=Start_Up_Owner.id
        ########################################################
        try:
            if(request.data['team_size']!=None and request.data['team_size']!=""):
                Start_Up_Team_Serializer = StartUpTeamSerializer(data=request.data)
                if(Start_Up_Team_Serializer.is_valid()):
                    Start_Up_Team_Serializer.save()
                    return Response(Start_Up_Team_Serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(Start_Up_Team_Serializer.data,status=status.HTTP_400_BAD_REQUEST) 
            else:
                raise NotFound({"message":"rejected"})
        except:
            raise NotFound({"message":"Not found","block":"outer_block"})

class StartUpDetailsApi(viewsets.ModelViewSet):
    # queryset = StartUpDetails.objects.all()
    serializer_class = StartUpDetailsSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        if(email!=None):
            try:
                Start_Up_Owner  = StartUpOwner.objects.get(email_id = email)
                Start_Up_Details = StartUpDetails.objects.filter(owner=Start_Up_Owner.id)
                return Start_Up_Details
            except Exception as e:
                raise NotFound({"message":"not_found"})
        else:
            Start_Up_Details  = StartUpDetails.objects.all()
            return Start_Up_Details

    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        email= request.query_params.get('email_id')
        Start_Up_Owner  = StartUpOwner.objects.get(email_id = email)
        ########################################################
        request.data['id']= StartUpDetails.objects.count()+1
        request.data['start_up_name'] = request.query_params.get('start_up_name')
        request.data['start_up_url'] = request.query_params.get('start_up_url')
        request.data['start_up_description'] = request.query_params.get('start_up_description')
        request.data['start_up_product_detail'] = request.query_params.get('start_up_product_detail')
        request.data['start_up_handler'] = request.query_params.get('start_up_handler')
        request.data['owner']=Start_Up_Owner.id

        try:
            if(request.data['start_up_name']!=None and request.data['start_up_url']!=None and request.data['start_up_description']!=None and request.data['start_up_product_detail']!=None and request.data['start_up_handler']!=None):
                Start_Up_Details_Serializer = StartUpDetailsSerializer(data=request.data)
                if(Start_Up_Details_Serializer.is_valid()):
                    Start_Up_Details_Serializer.save()
                    return Response(Start_Up_Details_Serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(Start_Up_Details_Serializer.data,status=status.HTTP_400_BAD_REQUEST) 
            else:
                raise NotFound({"message":"rejected"})
        except:
            raise NotFound({"message":"Not found","block":"outer_block"})


class StartUpCatorgeryApi(viewsets.ModelViewSet):
    # queryset = StartUpCatorgery.objects.all()
    serializer_class = StartUpCatorgerySerializer

    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        if(email!=None):
            try:
                Start_Up_Owner  = StartUpOwner.objects.get(email_id = email)
                Start_Up_Catorgery = StartUpCatorgery.objects.filter(owner=Start_Up_Owner.id)
                return Start_Up_Catorgery
            except Exception as e:
                raise NotFound({"message":"not_found"})
        else:
            Start_Up_Catorgery  = StartUpCatorgery.objects.all()
            return Start_Up_Catorgery

    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        email= request.query_params.get('email_id')
        Start_Up_Owner  = StartUpOwner.objects.get(email_id = email)
        ########################################################
        request.data['id']= StartUpCatorgery.objects.count()+1
        request.data['customer_targeted'] = request.query_params.get('customer_targeted')
        request.data['start_up_technology_catergory'] = request.query_params.get('start_up_technology_catergory')
        request.data['start_up_stage'] = request.query_params.get('start_up_stage')
        request.data['start_up_usecase'] = request.query_params.get('start_up_usecase')
        request.data['owner']=Start_Up_Owner.id
        try:
            Start_Up_Catorgerys_Serializer = StartUpCatorgerySerializer(data=request.data)
            if(Start_Up_Catorgerys_Serializer.is_valid()):
                Start_Up_Catorgerys_Serializer.save()
                return Response(Start_Up_Catorgerys_Serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(Start_Up_Catorgerys_Serializer.data,status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return NotFound({"message":"rejected"})

class StartUpLegalApi(viewsets.ModelViewSet):
    # queryset = StartUpLegal.objects.all()
    serializer_class = StartUpLegalSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        if(email!=None):
            try:
                Start_Up_Owner  = StartUpOwner.objects.get(email_id = email)
                Start_Up_Legal = StartUpLegal.objects.filter(owner=Start_Up_Owner.id)
                return Start_Up_Legal
            except Exception as e:
                raise NotFound({"message":"not_found"})
        else:
            Start_Up_Legal  = StartUpLegal.objects.all()
            return Start_Up_Legal

    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        email= request.query_params.get('email_id')
        Start_Up_Owner  = StartUpOwner.objects.get(email_id = email)
        ########################################################
        request.data['id']= StartUpLegal.objects.count()+1
        request.data['legal_entity_information'] = request.query_params.get('legal_entity_information')
        request.data['incorporated_company_name'] = request.query_params.get('incorporated_company_name')
        request.data['patents_filed'] = request.query_params.get('patents_filed')
        request.data['owner']=Start_Up_Owner.id

        try:
            if(request.data['legal_entity_information']!=None and request.data['incorporated_company_name']!=None and request.data['patents_filed']!=None):
                Start_Up_Legal_Serializer = StartUpLegalSerializer(data=request.data)
                if(Start_Up_Legal_Serializer.is_valid()):
                    Start_Up_Legal_Serializer.save()
                    return Response(Start_Up_Legal_Serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(Start_Up_Legal_Serializer.data,status=status.HTTP_400_BAD_REQUEST) 
            else:
                raise NotFound({"message":"rejected"})
        except:
            raise NotFound({"message":"rejected","block":"outter_block"})


#############################################################################

class InvestorInformationApi(viewsets.ModelViewSet):
    # queryset = InvestorInformation.objects.all()
    serializer_class = InvestorInformationSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        if(email!=None):
            try:
                Investor_Information  = InvestorInformation.objects.get(email_id = email)
                return Investor_Information
            except Exception as e:
                raise NotFound({"message":"not_found"})
        else:
            Investor_Information  = InvestorInformation.objects.all()
            return Investor_Information

    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        ########################################################
        request.data['id']= InvestorInformation.objects.count()+1
        request.data['name'] = request.query_params.get('name')
        request.data['email_id'] = request.query_params.get('email_id')
        request.data['password'] = request.query_params.get('password')
        request.data['mobile_number'] = request.query_params.get('mobile_number')
        request.data['year_of_experience'] = request.query_params.get('year_of_experience')
        request.data['company_invested'] = request.query_params.get('company_invested')

        try:
            if(request.data['name']!=None and request.data['email_id']!=None and request.data['password']!=None and request.data['mobile_number']!=None and request.data['year_of_experience']!=None and request.data['company_invested']!=None):
                Investor_Information_Serializer = InvestorInformationSerializer(data=request.data)
                if(Investor_Information_Serializer.is_valid()):
                    Investor_Information_Serializer.save()
                    return Response(Investor_Information_Serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(Investor_Information_Serializer.data,status=status.HTTP_400_BAD_REQUEST) 
            else:
                raise NotFound({"message":"rejected"})
        except:
            raise NotFound({"message":"rejected","block":"outter_block"})



class InvestorProfessionalExperienceApi(viewsets.ModelViewSet):
    # queryset = InvestorProfessionalExperience.objects.all()
    serializer_class = InvestorProfessionalExperienceSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        print(email)
        if(email!=None):
            try:
                Investor_Information  = InvestorInformation.objects.get(email_id = email)
                Investor_Professional_Experience = InvestorProfessionalExperience.objects.filter( investor = Investor_Information.id)
                return Investor_Professional_Experience
            except Exception as e:
                raise NotFound({"message":"not_found"})
        else:
            Investor_Professional_Experience  = InvestorProfessionalExperience.objects.all()
            return Investor_Professional_Experience

    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        ########################################################
        email= request.query_params.get('email_id')
        Investor_Information  = InvestorInformation.objects.get(email_id = email)
        request.data['id']= InvestorProfessionalExperience.objects.count()+1
        request.data['investor_catorgery'] = request.query_params.get('investor_catorgery')
        request.data['investor'] = Investor_Information.id

        try:
            if(request.data['investor_catorgery']!=None and request.data['investor']!=None):
                Investor_Professional_Experience_Serializer = InvestorProfessionalExperienceSerializer(data=request.data)
                if(Investor_Professional_Experience_Serializer.is_valid()):
                    Investor_Professional_Experience_Serializer.save()
                    return Response(Investor_Professional_Experience_Serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(Investor_Professional_Experience_Serializer.data,status=status.HTTP_400_BAD_REQUEST) 
            else:
                raise NotFound({"message":"rejected"})
        except:
            raise NotFound({"message":"rejected","block":"outter_block"})



class InvestorSkillsExperienceApi(viewsets.ModelViewSet):
    # queryset = InvestorSkillsExperience.objects.all()
    serializer_class = InvestorSkillsExperienceSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        if(email!=None):
            try:
                Investor_Information  = InvestorInformation.objects.get(email_id = email)
                Investor_Skills_Experience = InvestorSkillsExperience.objects.filter( investor = Investor_Information.id)
                return Investor_Skills_Experience
            except Exception as e:
                raise NotFound({"message":"not_found"})
        else:
            Investor_Skills_Experience  = InvestorSkillsExperience.objects.all()
            return Investor_Skills_Experience

    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        ########################################################
        email= request.query_params.get('email_id')
        Investor_Information  = InvestorInformation.objects.get(email_id = email)
        request.data['id']= InvestorSkillsExperience.objects.count()+1
        request.data['investor_skills'] = request.query_params.get('investor_skills')
        request.data['investor'] = Investor_Information.id

        try:
            if(request.data['investor_skills']!=None):
                Investor_Skills_Experience_Serializer = InvestorSkillsExperienceSerializer(data=request.data)
                if(Investor_Skills_Experience_Serializer.is_valid()):
                    Investor_Skills_Experience_Serializer.save()
                    return Response(Investor_Skills_Experience_Serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(Investor_Skills_Experience_Serializer.data,status=status.HTTP_400_BAD_REQUEST) 
            else:
                raise NotFound({"message":"rejected"})
        except:
            raise NotFound({"message":"rejected","block":"outter_block"})



class InvestorPositionApi(viewsets.ModelViewSet):
    # queryset = InvestorPosition.objects.all()
    serializer_class = InvestorPositionSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        if(email!=None):
            try:
                Investor_Information  = InvestorInformation.objects.get(email_id = email)
                Investor_Position = InvestorPosition.objects.filter( investor = Investor_Information.id)
                return Investor_Position
            except Exception as e:
                raise NotFound({"message":"not_found"})
        else:
            Investor_Position  = InvestorPosition.objects.all()
            return Investor_Position

    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        ########################################################
        email= request.query_params.get('email_id')
        Investor_Information  = InvestorInformation.objects.get(email_id = email)
        request.data['id']= InvestorPosition.objects.count()+1
        request.data['position'] = request.query_params.get('position')
        request.data['investor'] = Investor_Information.id
        try:
            if(request.data['position']!=None and request.data['investor']!=None):
                Investor_Position_Serializer = InvestorPositionSerializer(data=request.data)
                if(Investor_Position_Serializer.is_valid()):
                    Investor_Position_Serializer.save()
                    return Response(Investor_Position_Serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(Investor_Position_Serializer.data,status=status.HTTP_400_BAD_REQUEST) 
            else:
                raise NotFound({"message":"rejected"})
        except:
            raise NotFound({"message":"rejected","block":"outter_block"})


class InvestmentDetailApi(viewsets.ModelViewSet):
    # queryset = InvestmentDetail.objects.all()
    serializer_class = InvestmentDetailSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        if(email!=None):
            try:
                Investor_Information  = InvestorInformation.objects.get(email_id = email)
                Investment_Detail = InvestmentDetail.objects.filter( investor = Investor_Information.id)
                return Investment_Detail
            except Exception as e:
                raise NotFound({"message":"not_found"})
        else:
            Investment_Detail  = InvestmentDetail.objects.all()
            return Investment_Detail

    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        ########################################################
        email= request.query_params.get('email_id')
        Investor_Information  = InvestorInformation.objects.get(email_id = email)
        request.data['id']= InvestmentDetail.objects.count()+1
        request.data['investor_company_stage'] = request.query_params.get('investor_company_stage')
        request.data['investor_company_relation'] = request.query_params.get('investor_company_relation')
        request.data['investment_range'] = request.query_params.get('investment_range')
        request.data['form_of_investment'] = request.query_params.get('form_of_investment')
        request.data['general_expectation'] = request.query_params.get('general_expectation')
        request.data['historical_rate_returns'] = request.query_params.get('historical_rate_returns')
        request.data['investor'] = Investor_Information.id

        try:
            if(request.data['investor_company_stage']!=None and request.data['investor_company_relation']!=None and request.data['investment_range']!=None 
                and request.data['form_of_investment']!=None and request.data['general_expectation']!=None and request.data['historical_rate_returns']!=None):
                Investment_Detail_Serializer = InvestmentDetailSerializer(data=request.data)
                if(Investment_Detail_Serializer.is_valid()):
                    Investment_Detail_Serializer.save()
                    return Response(Investment_Detail_Serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(Investment_Detail_Serializer.data,status=status.HTTP_400_BAD_REQUEST) 
            else:
                raise NotFound({"message":"rejected"})
        except:
            raise NotFound({"message":"rejected","block":"outter_block"})


class IndustrialInvestmentApi(viewsets.ModelViewSet):
    # queryset = IndustrialInvestment.objects.all()
    serializer_class = IndustrialInvestmentSerializer
    
    def get_queryset(self):
        email = self.request.query_params.get('email_id')
        if(email!=None):
            try:
                Investor_Information  = InvestorInformation.objects.get(email_id = email)
                Investment_Detail = IndustrialInvestment.objects.filter( investor = Investor_Information.id)
                return Investment_Detail
            except Exception as e:
                raise NotFound({"message":"not_found"})
        else:
            Investment_Detail  = IndustrialInvestment.objects.all()
            return Investment_Detail

    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        ########################################################
        email= request.query_params.get('email_id')
        Investor_Information  = InvestorInformation.objects.get(email_id = email)
        request.data['id']= IndustrialInvestment.objects.count()+1
        request.data['investment_domain'] = request.query_params.get('investment_domain')
        request.data['investor'] = Investor_Information.id
        try:
            if(request.data['investment_domain']!=None ):
                Industrial_Investment_Serializer = IndustrialInvestmentSerializer(data=request.data)
                if(Industrial_Investment_Serializer.is_valid()):
                    Industrial_Investment_Serializer.save()
                    return Response(Industrial_Investment_Serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(Industrial_Investment_Serializer.data,status=status.HTTP_400_BAD_REQUEST) 
            else:
                raise NotFound({"message":"rejected"})
        except:
            raise NotFound({"message":"rejected","block":"outter_block"})


