import datetime
from statistics import mode
from django.db import models
DEP_CHOICES={
    ('Civil Engineering','Civil Engineering'),
    ('Computer Engineering','Computer Engineering'),
    ('Electronics & Telecommunication Engineering','Electronics & Telecommunication Engineering'),
    ('Mechanical Engineering','Mechanical Engineering'),

}
RELIGION_CHOICES={('Hindu','Hindu'),
 ('Jain','Jain'),
 ('Buddhisth','Buddhisth'),
 ('Muslim','Muslim'),}
CATEGORE_CHOICES={
    ('Open','Open'),	
    ('OBC','OBC'),
    ('NT','NT'),
    ('SC','SC'),
    ('ST','ST'),

}	
YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]	

GENDER_CHOICES={('Male','Male'),('Female','Female')}
# Create your models here.
class formmodel(models.Model):
    en_roll= models.IntegerField()
    f_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100) 
    l_name = models.CharField(max_length=100)
    Class = models.CharField(
        max_length = 50,
        choices = DEP_CHOICES,
        default = '1'
        )
    pe_phone= models.IntegerField()
    pe_wphone= models.IntegerField()
    pr_phone= models.IntegerField()
    pr_wphone = models.IntegerField()
    DOB = models.DateField()
    Gender=models.CharField(
        max_length = 10,
        choices = GENDER_CHOICES,
        default = '1'
        )
    Email_id=models.EmailField()
    pdis=models.BooleanField(help_text="Are You Physicalliy Disabled?")
    address =models.CharField(max_length=100)
    AT_post= models.CharField(max_length=100)
    Tal=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    pin_code=models.IntegerField()
    is_sameadd=models.BooleanField(default = True)
    address2 =models.CharField(max_length=100)
    AT_post2= models.CharField(max_length=100)
    Tal2=models.CharField(max_length=100)
    district2=models.CharField(max_length=100)
    pin_code2=models.IntegerField()
    Religion=models.CharField(
        max_length = 10,
        choices = RELIGION_CHOICES,
        default = 'Hindu'
        )
    Categore= models.CharField(
        max_length = 10,
        choices = CATEGORE_CHOICES,
        default = 'Open'
        )
    is_fatheralive=models.BooleanField(help_text="Is Father is Alive?",default=True)
    is_motheralive=models.BooleanField(help_text="Is Mother is Alive?",default=True)
    father_occ=models.CharField(max_length=100,blank=True)
    mother_occ=models.CharField(max_length=100,blank=True,default = 'Housewife')
    Family_inc=models.IntegerField(default= 5000)
    par_res=models.CharField(max_length=100)
    SSC_res=models.IntegerField()
    SSC_year=models.IntegerField(choices=YEAR_CHOICES,default=datetime.datetime.now().year)
    HSC_res=models.IntegerField()
    HSC_year=models.IntegerField()
    NOther_cor=models.CharField(max_length=100)
    FY_addYear=models.IntegerField()
    SY_addYear=models.IntegerField()
    TY_addYear=models.IntegerField()
    Sem1_res=models.IntegerField()
    sem1_back=models.CharField(max_length=100)
    sem1pass_ex=models.CharField(max_length=100)
    Sem2_res=models.IntegerField()
    sem2_back=models.CharField(max_length=100)
    sem2pass_ex=models.CharField(max_length=100)
    Sem3_res=models.IntegerField()
    sem3_back=models.CharField(max_length=100)
    sem3pass_ex=models.CharField(max_length=100)
    Sem4_res=models.IntegerField()
    sem4_back=models.CharField(max_length=100)
    sem4pass_ex=models.CharField(max_length=100)
    Sem5_res=models.IntegerField()
    sem5_back=models.CharField(max_length=100)
    sem5pass_ex=models.CharField(max_length=100)
    Sem6_res=models.IntegerField()
    sem6_back=models.CharField(max_length=100)
    sem6pass_ex=models.CharField(max_length=100)
    photo=models.IntegerField()
# asas
class tem1(models.Model):
    en_roll=models.IntegerField()
    Gendar=models.BooleanField()
    BOD=models.DateField()
    
    # BOD = models.DateTimeField((""), auto_now=False, auto_now_add=False)