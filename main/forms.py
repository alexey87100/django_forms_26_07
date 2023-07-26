from django import forms

from .models import Skill, Profile
from django.core.exceptions import ValidationError


class EditCreateProfileModelForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(EditCreateProfileModelForm, self).__init__(*args, **kwargs)
    #     self.fields['skill'].queryset = Skill.objects.all().order_by("-value")

    # def __init__(self, *args, **kwargs):
    #     if kwargs.get('show_two'):
    #         show_two = kwargs.get('show_two')
    #         del kwargs['show_two']
    #     super(EditCreateProfileModelForm, self).__init__(*args, **kwargs)
    #     if show_two:
    #         self.fields['skill'].queryset = Skill.objects.all()[:2]

    # def clean_age(self):
    #     age = self.cleaned_data['age']
    #     if int(age) < 18:
    #         raise ValidationError("Нельзя младше 18!")
    #     return age
        
    class Meta:
        model = Profile
        fields = ('name', 'skill', 'age')


class EditCreateProfileForm(forms.Form):

    name = forms.CharField(max_length=1200, help_text="Введи имя")
    skill = forms.ModelChoiceField(queryset=Skill.objects.all())
    age = forms.IntegerField(
        label="Возраст"
        )
