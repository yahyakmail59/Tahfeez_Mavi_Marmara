from django import forms
from .models import Circle, Teacher, Student, Test

class CircleForm(forms.ModelForm):
    class Meta:
        model = Circle
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'masjed_name': forms.TextInput(attrs={'class': 'form-control'}),
            'work_schedule': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

            


        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'id_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'personal_mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'Monthly_absence': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'circle': forms.Select(attrs={'class': 'form-control'}),

        }
        

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
        
# class AchievementForm(forms.ModelForm):
#     class Meta:
#         model = Achievement
#         fields = '__all__'



# class RecitationForm(forms.ModelForm):
#     class Meta:
#         model = Recitation
#         fields = '__all__'
