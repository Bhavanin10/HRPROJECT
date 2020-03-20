from django.db import models
from django.core.validators import RegexValidator,FileExtensionValidator,MinValueValidator,MaxValueValidator
from django import forms
# Create your models here.
GENDER_CHOICES = (
    ('Male','Male'),
    ('Female', 'Female'),
    ('Other','Other'),
)

MARITALSTATUS_CHOICES=(
    ('Single','Single'),
    ('Married','Married'),
)

phone_regex = RegexValidator(regex="[6-9]\d{9}", message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class EmployeeDetails(models.Model):
    EmployeeId=models.CharField(max_length=10,unique=True,blank=False)
    EmployeeName=models.CharField(blank=False,default=None,max_length=15)
    FathersName=models.CharField(blank=False,default=None,max_length=15)
    MothersName=models.CharField(blank=False,default=None,max_length=15)
    BloodGroup=models.CharField(blank=False,default=None,max_length=3)
    DateOfBirth=models.DateField()
    Gender=models.CharField(max_length=6, choices=GENDER_CHOICES, default='Other')
    MaritalStatus=models.CharField(max_length=10, choices=MARITALSTATUS_CHOICES, blank=False,default=None,)
    SpouseName=models.CharField(blank=False,default=None,max_length=15)
    Designation=models.CharField(blank=False,default=None,max_length=25)
    EmergencyContact=models.IntegerField(blank=False,default=None)
    PermanentAdress=models.CharField(max_length=200,blank=False,default=None)
    PresentAdress=models.CharField(max_length=200,blank=False,default=None)
    MobileNumber=models.CharField(validators=[phone_regex], max_length=10, blank=True)
    EmailId=models.EmailField(unique=True,blank=False,default=None,max_length=50)
    PostGraduation=models.CharField(blank=False,default=None,max_length=30)
    PostGraduation_university=models.CharField(max_length=20,default=None)
    PostGraduation_Yop=models.DateField()
    Graduation=models.CharField(blank=False,default=None,max_length=30)
    Graduation_university=models.CharField(max_length=20,default=None)
    Graduation_Yop=models.DateField()
    _12th=models.CharField(blank=False,default=None,max_length=30)
    _12th_Board=models.CharField(max_length=20,default=None)
    _12th_Yop=models.DateField()
    _10th=models.CharField(blank=False,default=None,max_length=30)
    _10th_Board=models.CharField(max_length=20,default=None)
    _10th_Yop=models.DateField()
    Employer1=models.CharField(max_length=20,default=None)
    Designation1=models.CharField(max_length=25,default=None)
    From1=models.DateField()
    To1=models.DateField()
    Employer2=models.CharField(max_length=20,default=None)
    Designation2=models.CharField(max_length=25,default=None)
    From2=models.DateField()
    To2=models.DateField()
    DOJ=models.DateField()
    PANNumber=models.CharField(max_length=10)
    AdharNumber=models.IntegerField(default=None)
    UANNumber=models.IntegerField(default=None)
    BankAccountNumber=models.CharField(max_length=15,default=None)
    IFSCCode=models.CharField(max_length=10,default=None)
    EmployeeSignature=models.CharField(blank=False,default=None,max_length=30)
    Date=models.DateField()


class Attachments(models.Model):
    EMPLOYEE_NAME=models.CharField(max_length=20,default=None,blank=False)
    PANCARD=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    ADHARCARD=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    ADDRESS_PROOF=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    PASSPORT_COPY=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    DEGREE_CERTIFICATE=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    SSLC_OR_10TH=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file',)])
    PUC_OR_12TH=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    PREVIOUS_COMPANY_OFFER_LETTER=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    EXPERIENCE_LETTER=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    RELIEVING_LETTER=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    INCREMENT_LETTER=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    PAYSLIP_MONTH1=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    PAYSLIP_MONTH2=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    PAYSLIP_MONTH3=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    FORM16_or_TAX_COMPUTATION_LETTER_or_FINAL_SETTLEMENT_LETTER=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='please choose the valid file')])
    PASSPORT_SIZE_PHOTO=models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg','img','png'],message='please choose the valid file')])