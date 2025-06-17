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
from Books.models import Books
class addbookForm(forms.ModelForm):
    class Meta:  #inner class used to give description about form structure
        model=Books
        #fields="_all_"
        #or
        fields=['Title','Author','Price','Language','Pages','Image']