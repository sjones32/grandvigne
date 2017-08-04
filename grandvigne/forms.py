import pickle

from django.contrib.auth.models import User
from django import forms
from django.forms import inlineformset_factory, BaseModelFormSet

from .models import defaultModel, Variable, Vignette, levelModel
from .models import descriptionStatement

class registerForm(forms.ModelForm):
	#makes *** in password form
	password = forms.CharField(widget = forms.PasswordInput)
	
	class Meta: 
		
		model = User 
		fields = ['username', 'email', 'password', 'first_name', 'last_name']
		
class createVigne(forms.ModelForm):
	#makes *** in password form
	password = forms.CharField(widget = forms.PasswordInput)
	
	class Meta: 
		
		model = defaultModel 
		fields = ['title', 'text']

			  
# Vignette Form classes
class vignetteForm(forms.ModelForm):
#	domainField = forms.CharField()
	class Meta: 
		
		model = Vignette 
		fields = ['domainField','interaction_text']
#https://gist.github.com/elena/3915748#file-basic-multivaluefield-multiwidget-L40

class variableWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput(),
                   forms.TextInput(), 
				   forms.TextInput()]
        super(variableWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return pickle.loads(value)
        else:
            return ['', '']
			
class levelsWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput(),
                   forms.TextInput(), 
				   forms.TextInput(),
				   forms.TextInput()]
        super(levelsWidget, self).__init__(widgets, attrs)
		
    def decompress(self, value):
        if value:
            return pickle.loads(value)
        else:
            return ['', '']
			
class descriptionForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		
		super(descriptionForm, self).__init__(*args, **kwargs)
		descriptionForm.variable_text = forms.CharField(max_length = 200)

	def save(self, commit = True):
		s = descriptionStatement()
		s.save()
		s.description_text = self.cleaned_data['description_text']
		# loop over various forms to save
		if commit:
			s.save()
		return s
	
	class Meta: 
		
		model = descriptionStatement 
		exclude = ('variable_text',)
		
			
class variableForm(forms.ModelForm):
	
	class Meta: 
		model = Variable
		exclude = ('levels',)
		
class levelForm(forms.ModelForm):

	class Meta: 
		model = levelModel
		fields = ['level_option']

class BaseDescriptionFormSet(BaseModelFormSet):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
