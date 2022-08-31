from statistics import mode
from django.db import models

# Create your models here.
class formmodel(models.Model):
    en_roll= models.IntegerField()
    f_name = models.CharField()
    m_name = models.CharField() 
    l_name = models.CharField()
    Class = models.CharField()
    pe_phone= models.IntegerField()
    pe_wphone= models.IntegerField()
    pr_phone= models.IntegerField()
    pr_wphone = models.IntegerField()
    DOB = models.DateField();
    Gender=models.BooleanField();
    Email_id=models.EmailField()
    pdis=models.BooleanField()
    address =models.CharField();
    AT_post= models.CharField();
    Tal=models.CharField();
    district=models.CharField();
    pin_code=models.IntegerField();
    is_sameadd=models.BooleanField();
    address2 =models.CharField();
    AT_post2= models.CharField();
    Tal2=models.CharField();
    district2=models.CharField();
    pin_code2=models.IntegerField();
    Religion=models.CharField();
    Categore= models.CharField();
    is_fatheralive=models.BooleanField();
    is_motheralive=models.BooleanField();
    father_occ=models.CharField();
    mother_occ=models.CharField();
    Family_inc=models.IntegerField();
    par_res=models.CharField();
    SSC_res=models.IntegerField();
    SSC_year=models.IntegerField();
    HSC_res=models.IntegerField();
    HSC_year=models.IntegerField();
    NOther_cor=models.CharField();
    FY_addYear=models.IntegerField();
    SY_addYear=models.IntegerField();
    TY_addYear=models.IntegerField();
    Sem1_res=models.ImageField();
    sem1_back=models.CharField();
    sem1pass_ex=models.CharField();
    Sem2_res=models.ImageField();
    sem2_back=models.CharField();
    sem2pass_ex=models.CharField();
    Sem3_res=models.ImageField();
    sem3_back=models.CharField();
    sem3pass_ex=models.CharField();
    Sem4_res=models.ImageField();
    sem4_back=models.CharField();
    sem4pass_ex=models.CharField();
    Sem5_res=models.ImageField();
    sem5_back=models.CharField();
    sem5pass_ex=models.CharField();
    Sem6_res=models.ImageField();
    sem6_back=models.CharField();
    sem6pass_ex=models.CharField();
    photo=models.IntegerField();






