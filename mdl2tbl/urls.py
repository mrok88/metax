# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views
############################## bootstrap 3 ##############################
#from .views import HomePageView,DefaultFormView,Djbs01FormView,Djbs02FormView,Djbs03FormView,Djbs04FormView,Djbs05FormView,Djbs06FormView,Djbs07FormView
######################################################################################

app_name='mdl2tbl'
urlpatterns = [
    url(r'^$',  views.Djbs02FormView.as_view(), name='djbs02'),
    url(r'form_by_field', views.form_by_field , name='form_by_field'),
    url(r'djbs01', views.Djbs01FormView.as_view(), name='djbs01'),
    url(r'djbs02', views.Djbs02FormView.as_view(), name='djbs02'),
    url(r'djbs03', views.Djbs03FormView.as_view(), name='djbs03'),
    url(r'djbs04', views.Djbs04FormView.as_view(), name='djbs04'),
    url(r'djbs05', views.Djbs05FormView.as_view(), name='djbs05'),
    url(r'djbs06', views.Djbs06FormView.as_view(), name='djbs06'),
    url(r'djbs07', views.Djbs07FormView.as_view(), name='djbs07'),
    url(r'djbs08', views.Djbs08FormView.as_view(), name='djbs08'),
    url(r'djbs09', views.Djbs09FormView.as_view(), name='djbs09'),
    url(r'djbs10', views.Djbs10FormView.as_view(), name='djbs10'),
    url(r'djbs11', views.Djbs11FormView.as_view(), name='djbs11'),
    url(r'djbs12p', views.Djbs12pFormView.as_view(), name='djbs12p'),    
    url(r'djbs12', views.Djbs12FormView.as_view(), name='djbs12'),
    url(r'djbs13p', views.Djbs13pFormView.as_view(), name='djbs13p'),    
    url(r'djbs13', views.Djbs13FormView.as_view(), name='djbs13'),
    url(r'djbs14', views.Djbs14FormView.as_view(), name='djbs14'),
    url(r'form', views.DefaultFormView.as_view(), name='form'),
    url(r'test/', views.tbl_list, name='tbl_list'),
    url(r'cds/', views.cd_list, name='cd_list'),    
    url(r'comp/(?P<pk>\w*)', views.comp_list, name='comp_list'),
    url(r'erd/(?P<pk>\w*)', views.erd_pview, name='erd_pview'),
]