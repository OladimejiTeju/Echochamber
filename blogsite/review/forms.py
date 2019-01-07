from django import forms

CHOICES = (('1','title'),('2','author'),('3','pubdate'))

class ListForm(forms.Form):
	listselect = forms.ChoiceField(label='Select Sort', choices=CHOICES , initial = '1')
	#your_name = forms.CharField(label='Your name', max_length=100, widget=forms.Textarea)
	
