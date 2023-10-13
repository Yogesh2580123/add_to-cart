from django import forms
from .models import Student

ge = [('male', 'MALE'), ('female', 'FEMALE'), ('others', 'OTHERS')]
la = [('hindi', 'HINDI'), ('english', 'ENGLISH'), ('marathi', 'MARATHI')]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'fname': 'FIRST-NAME',
            'mname': 'MIDDEL-NAME',
            'lname': 'LAST-NAME',
            'address': 'ADDRESS',
            'dob': 'DATE-OF-BIRTH',
            'phone': 'CONTACT-NUMBER',
            'mail': 'EMAIL-ID',
            'gender': 'GENDER',
            'langauges': 'LANGAUGES',
        }

        widgets = {
            'address': forms.Textarea(attrs={'placeholder': 'E.g. kanhan 441401'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect(choices=ge),
            'langauges': forms.CheckboxSelectMultiple(choices=la)
        }
