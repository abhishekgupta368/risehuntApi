from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views


route = routers.DefaultRouter()
route.register("start-up-owner",views.StartUpOwnerApi,basename="start-up-owner")
route.register("start-up-team",views.StartUpTeamApi,basename="start-up-team")
route.register("start-up-details",views.StartUpDetailsApi,basename="start-up-details")
route.register("start-up-catorgery",views.StartUpCatorgeryApi,basename="start-up-catorgery")
route.register("start-up-legal",views.StartUpLegalApi,basename="start-up-legal")

route.register("investment-info",views.InvestorInformationApi,basename="investment-info")
route.register("investment-profressional-exp",views.InvestorProfessionalExperienceApi,basename="investment-profressional-exp")
route.register("investment-skills-exp",views.InvestorSkillsExperienceApi,basename="investment-skills-exp")
route.register("investment-position",views.InvestorPositionApi,basename="investment-position")
route.register("investment-details",views.InvestmentDetailApi,basename="investment-details")
route.register("industorial-investment",views.IndustrialInvestmentApi,basename="industorial-investment")


urlpatterns = [
    path('',include(route.urls)),
]
