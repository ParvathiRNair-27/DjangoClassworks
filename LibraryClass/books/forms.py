from django import forms

# class addbookForm(forms.Form):
#     Title=forms.CharField()
#     Author=forms.CharField()
#     Price=forms.IntegerField()
#     Pages=forms.IntegerField()
#     Language_choices=[('english','English'),('french','French'),('malayalam','Malayalam'),('hindi','Hindi')]
#     Language = forms.ChoiceField(choices=Language_choices)
#     Image=forms.ImageField()

# using ModelForm

from books.models import books
class addbookForm(forms.ModelForm):
    class Meta:
        model=books
        # fields="__all__"
            # or
        fields=['Title','Author','Price','Pages','Language','Image']