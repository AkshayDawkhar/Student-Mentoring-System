from email.policy import default
from operator import imod
# from tkinter import Widget
from  django import forms
from formModel.models import formmodel
from formModel.models import tem1
from django.contrib.admin.widgets import AdminDateWidget

class studentForm(forms.ModelForm):
    class Meta:
        model = formmodel
        fields = '__all__'
        labels = {
            "BOD":'date',
            "f_name":"Name",
            "pe_phone":"Contact No","pr_phone":"Contact No",
            "pr_wphone":"whatsapp Number","pe_wphone":"whatsapp Number",
            "pdis":"",
            "is_fatheralive":"",
            "is_motheralive":""
        }
        widgets={
            'en_roll':forms.NumberInput(attrs={'class':'form-control'}),
            "DOB": forms.DateInput(attrs={'class':'form-control'}),
            "f_name":forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder': 'Last - First - Middle',}),
            # "m_name":forms.NumberInput(attrs={'class':'form-control'}),
            # "l_name":forms.NumberInput(attrs={'class':'form-control'}),
            "Class":forms.Select(attrs={'class':'form-control'}),
            # "Class":forms.RadioSelect(),
            "pe_phone":forms.NumberInput(attrs={'class':'form-control','placeholder': 'Personal',}),
            "pe_wphone":forms.NumberInput(attrs={'class':'form-control','placeholder': 'Personal'}),
            "pr_phone":forms.NumberInput(attrs={'class':'form-control','placeholder': 'Parent'}),
            "pr_wphone":forms.NumberInput(attrs={'class':'form-control','placeholder': 'Parent'}),
            "DOB":forms.NumberInput(attrs={'class':'form-control'}),
            "Gender":forms.RadioSelect(),
            # "Email_id":forms.NumberInput(attrs={'class':'form-control'}),
            "Email_id":forms.EmailInput(attrs={'class':'form-control'}),
            "pdis":forms.CheckboxInput(attrs={"class":"form-check-label "}),
            "address":forms.TextInput(attrs={'class':'form-control'}),
            "AT_post":forms.TextInput(attrs={'class':'form-control'}),
            "Tal":forms.TextInput(attrs={'class':'form-control'}),
            "district":forms.TextInput(attrs={'class':'form-control'}),
            "pin_code":forms.NumberInput(attrs={'class':'form-control'}),
            "is_sameadd":forms.CheckboxInput(attrs={'class':'form-check-label'}),
            "address2":forms.TextInput(attrs={'class':'form-control','placeholder': 'Same as Permanent Address',}),                      
            "AT_post2":forms.TextInput(attrs={'class':'form-control','placeholder': 'Same as Permanent Address',}),
            "Tal2":forms.TextInput(attrs={'class':'form-control','placeholder': 'Same as Permanent Address',}),
            "district2":forms.TextInput(attrs={'class':'form-control','placeholder': 'Same as Permanent Address',}),
            "pin_code2":forms.NumberInput(attrs={'class':'form-control','placeholder': 'Same as Permanent Address',}),
            "Religion":forms.Select(attrs={'class':'form-control'}),
            "Categore":forms.Select(attrs={'class':'form-control'}),
            "is_fatheralive":forms.CheckboxInput(attrs={'class':'form-check-label'}),
            "is_motheralive":forms.CheckboxInput(attrs={'class':'form-check-label'}),
            "father_occ":forms.TextInput(attrs={'class':'form-control'}),
            "mother_occ":forms.TextInput(attrs={'class':'form-control'}),
            "Family_inc":forms.NumberInput(attrs={'class':'form-control'}),
            "par_res":forms.NumberInput(attrs={'class':'form-control'}),
            "SSC_res":forms.NumberInput(attrs={'class':'form-control'}),
            "SSC_year":forms.Select(attrs={'class':'form-control'}),
            "HSC_res":forms.NumberInput(attrs={'class':'form-control'}),
            "HSC_year":forms.NumberInput(attrs={'class':'form-control'}),
            "NOther_cor":forms.NumberInput(attrs={'class':'form-control'}),
            "FY_addYear":forms.NumberInput(attrs={'class':'form-control'}),
            "SY_addYear":forms.NumberInput(attrs={'class':'form-control'}),
            "TY_addYear":forms.NumberInput(attrs={'class':'form-control'}),
            "Sem1_res":forms.NumberInput(attrs={'class':'form-control'}),
            "sem1_back":forms.NumberInput(attrs={'class':'form-control'}),
            "sem1pass_ex":forms.NumberInput(attrs={'class':'form-control'}),
            "Sem2_res":forms.NumberInput(attrs={'class':'form-control'}),
            "sem2_back":forms.NumberInput(attrs={'class':'form-control'}),
            "sem2pass_ex":forms.NumberInput(attrs={'class':'form-control'}),
            "Sem3_res":forms.NumberInput(attrs={'class':'form-control'}),
            "sem3_back":forms.NumberInput(attrs={'class':'form-control'}),
            "sem3pass_ex":forms.NumberInput(attrs={'class':'form-control'}),
            "Sem4_res":forms.NumberInput(attrs={'class':'form-control'}),
            "sem4_back":forms.NumberInput(attrs={'class':'form-control'}),
            "sem4pass_ex":forms.NumberInput(attrs={'class':'form-control'}),
            "Sem5_res":forms.NumberInput(attrs={'class':'form-control'}),
            "sem5_back":forms.NumberInput(attrs={'class':'form-control'}),
            "sem5pass_ex":forms.NumberInput(attrs={'class':'form-control'}),
            "Sem6_res":forms.NumberInput(attrs={'class':'form-control'}),
            "sem6_back":forms.NumberInput(attrs={'class':'form-control'}),
            "sem6pass_ex":forms.NumberInput(attrs={'class':'form-control'}),
            "photo":forms.NumberInput(attrs={'class':'form-control'}),
        }
class temForm(forms.ModelForm):
    class Meta:
        model = tem1
        fields = '__all__'
        widgets = {
        "BOD": forms.DateInput(attrs={'class': 'form-control'})
        }
        labels= {
        "BOD":"date"
        }