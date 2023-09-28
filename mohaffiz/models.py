from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta,date
from django.utils import timezone

class Circle(models.Model):
    name = models.CharField('اسم الحلقة',max_length=100)
    masjed_name = models.CharField('اسم المسجد',max_length=100)
    address = models.TextField('عنوان المسجد',)
    work_schedule = models.CharField('وقت تفعيل الحلقة',max_length=255)
    
    def __str__(self):
        return self.name

class Teacher(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField('الإسم رباعي',max_length=100)
    image = models.ImageField('صورة المحفظ',upload_to='teachers/')
    id_number  = models.CharField('رقم الهوية',max_length=14, unique=True)
    date_of_birth = models.DateField('تاريخ الميلاد',)
    address = models.TextField('عنوان السكن',)
    personal_mobile = models.CharField('رقم الجوال',max_length=15)
    Monthly_absence = models.PositiveIntegerField('عدد أيام الغياب',default=0)
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE, related_name='teachers', verbose_name="اختر الحلقة")
    
    
    def __str__(self):
        return self.full_name

class Student(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField('صورة الطالب',upload_to='students/')
    full_name = models.CharField('الإسم رباعي',max_length=100)
    id_number  = models.CharField('رقم الهوية',max_length=14, unique=True)
    birth_date = models.DateField('تاريخ الميلاد',)
    address = models.TextField('عنوان السكن',)
    personal_mobile = models.CharField('رقم الجوال الشخصي (اختياري)', max_length=15, blank=True, null=True)
    guardian_mobile = models.CharField('رقم جوال ولي الأمر', max_length=15)
    current_hifz = models.CharField('الحفظ الحالي',max_length=100)
    education_stage = models.CharField('المستوى الدراسي',max_length=100)
    Monthly_absence = models.PositiveIntegerField('عدد أيام الغياب',default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students', verbose_name="اختر المحفظ")
    
    
    def __str__(self):
        return self.full_name


part_counts = [(str(i), str(i)) for i in range(1, 31)]
# initial_part_number_counts = [(str(i), str(i)) for i in range(1, 31)]
# final_part_number_counts = [(str(i), str(i)) for i in range(1, 31)]
parts_name = [
    ('الأول', 'الأول'),
    ('الثاني', 'الثاني'),
    ('الثالث', 'الثالث'),
    ('الرابع', 'الرابع'),
    ('الخامس', 'الخامس'),
    ('السادس', 'السادس'),
    ('السابع', 'السابع'),
    ('الثامن', 'الثامن'),
    ('التاسع', 'التاسع'),
    ('العاشر', 'العاشر'),
    ('الحادي عشر', 'الحادي عشر'),
    ('الثاني عشر', 'الثاني عشر'),
    ('الثالث عشر', 'الثالث عشر'),
    ('الرابع عشر', 'الرابع عشر'),
    ('الخامس عشر', 'الخامس عشر'),
    ('السادس عشر', 'السادس عشر'),
    ('السابع عشر', 'السابع عشر'),
    ('الثامن عشر', 'الثامن عشر'),
    ('التاسع عشر', 'التاسع عشر'),
    ('العشرون', 'العشرون'),
    ('الواحد والعشرون', 'الواحد والعشرون'),
    ('الثاني والعشرون', 'الثاني والعشرون'),
    ('الثالث والعشرون', 'الثالث والعشرون'),
    ('الرابع والعشرون', 'الرابع والعشرون'),
    ('الخامس والعشرون', 'الخامس والعشرون'),
    ('السادس والعشرون', 'السادس والعشرون'),
    ('السابع والعشرون', 'السابع والعشرون'),
    ('الثامن والعشرون', 'الثامن والعشرون'),
    ('التاسع والعشرون', 'التاسع والعشرون'),
    ('الثلاثون', 'الثلاثون')
]


class Test(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="اختر الطالب")
    parts_count = models.CharField('عدد الأجزاء',choices=part_counts,max_length=10)
    initial_part_number = models.CharField('من بداية الجزء',choices=parts_name,max_length=30)
    final_part_number = models.CharField('إلى نهاية الجزء',choices=parts_name,max_length=30)
    test_date = models.DateTimeField('تاريخ الإختبار',default=timezone.now)
    result = models.IntegerField('معدل الإختبار')

    def __str__(self):
        return f"اختبار للطالب {self.student.full_name} من جزء {self.initial_part_number} إلى جزء {self.final_part_number}"
    


class DailySaving(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="اختر الطالب")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="اختر المحفظ"), 
    name = models.CharField('اختر السورة',max_length=100)
    ayat_number = models.PositiveIntegerField('رقم آية البداية')
    ayat_number2 = models.PositiveIntegerField('رقم آية النهاية')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class DailyReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="اختر الطالب")
    name = models.CharField('اختر السورة',max_length=100)
    ayat_number = models.PositiveIntegerField('رقم آية البداية')
    ayat_number2 = models.PositiveIntegerField('رقم آية النهاية')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# class Recitation(models.Model):
#     surah = models.CharField(max_length=255)
#     start_verse = models.PositiveIntegerField()
#     end_verse = models.PositiveIntegerField()
#     recitation_date = models.DateField()
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"{self.student.full_name}'s Recitation of {self.surah}"

# class HonorRoll(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     circle = models.ForeignKey(Circle, on_delete=models.CASCADE)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     achievement_type = models.CharField(max_length=255)  # You may want to create a separate model for this



# Certificate_type = [
#     ('شرعية','شرعية'),
#     ('علمية' ,'علمية')
# ]

# class Achievement(models.Model):
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='certificates')
#     certificate_type = models.CharField(max_length=255, choices=Certificate_type)
#     certificate_name = models.CharField(max_length=255)
#     certificate_image = models.ImageField(upload_to='certificates/')
    
#     def __str__(self):
#         return f"شهادة {self.teacher.full_name}"





# from django.db import models
# from django.contrib.auth.models import User



# departments=[('Cardiologist','Cardiologist'),
# ('Dermatologists','Dermatologists'),
# ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
# ('Allergists/Immunologists','Allergists/Immunologists'),
# ('Anesthesiologists','Anesthesiologists'),
# ('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
# ]
# class Doctor(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=True)
#     department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
#     status=models.BooleanField(default=False)
#     @property
#     def get_name(self):
#         return self.user.first_name+" "+self.user.last_name
#     @property
#     def get_id(self):
#         return self.user.id
#     def __str__(self):
#         return "{} ({})".format(self.user.first_name,self.department)



# class Patient(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=False)
#     symptoms = models.CharField(max_length=100,null=False)
#     assignedDoctorId = models.PositiveIntegerField(null=True)
#     admitDate=models.DateField(auto_now=True)
#     status=models.BooleanField(default=False)
#     @property
#     def get_name(self):
#         return self.user.first_name+" "+self.user.last_name
#     @property
#     def get_id(self):
#         return self.user.id
#     def __str__(self):
#         return self.user.first_name+" ("+self.symptoms+")"


# class Appointment(models.Model):
#     patientId=models.PositiveIntegerField(null=True)
#     doctorId=models.PositiveIntegerField(null=True)
#     patientName=models.CharField(max_length=40,null=True)
#     doctorName=models.CharField(max_length=40,null=True)
#     appointmentDate=models.DateField(auto_now=True)
#     description=models.TextField(max_length=500)
#     status=models.BooleanField(default=False)



# class PatientDischargeDetails(models.Model):
#     patientId=models.PositiveIntegerField(null=True)
#     patientName=models.CharField(max_length=40)
#     assignedDoctorName=models.CharField(max_length=40)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=True)
#     symptoms = models.CharField(max_length=100,null=True)

#     admitDate=models.DateField(null=False)
#     releaseDate=models.DateField(null=False)
#     daySpent=models.PositiveIntegerField(null=False)

#     roomCharge=models.PositiveIntegerField(null=False)
#     medicineCost=models.PositiveIntegerField(null=False)
#     doctorFee=models.PositiveIntegerField(null=False)
#     OtherCharge=models.PositiveIntegerField(null=False)
#     total=models.PositiveIntegerField(null=False)















































# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# departments = [
#     ("خالد بن الوليد", "خالد بن الوليد"),
#     ("زيد بن حارثة", "زيد بن حارثة"),
#     ("معاذ بن جبل", "معاذ بن جبل"),
# ]


# class Mohaffiz(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField(
#         "الصورة الشخصية",
#         upload_to="profile_pic/MohaffizProfilePic/",
#         null=True,
#         blank=True,
#     )
#     address = models.CharField("العنوان", max_length=40)
#     mobile = models.CharField("رقم الجوال", max_length=20, null=True)
#     department = models.CharField(
#         "اسم الحلقة",max_length=50, choices=departments, default="خالد بن الوليد"
#     )
#     status = models.BooleanField("الحالة",default=False)

#     @property
#     def get_name(self):
#         return self.user.first_name + " " + self.user.last_name

#     @property
#     def get_id(self):
#         return self.user.id

#     def __str__(self):
#         return "{} ({})".format(self.user.first_name, self.department)
