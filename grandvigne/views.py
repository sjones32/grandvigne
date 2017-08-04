from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import View
from django.utils import timezone 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

#  Tutorial Forms 
#from formtools.wizard.views import SessionWizardView
#from formtools.wizard.views import NamedUrlSessionWizardView
from .formsets import FormSetView

from django.forms import formset_factory

from .forms import createVigne
from .forms import registerForm
from .forms import vignetteForm, descriptionForm, variableForm, levelForm

from .models import defaultModel, Vignette 
from .models import descriptionStatement, Variable, levelModel 
 
import urllib
# Create your views here.

class IndexView(generic.ListView):
	model = Vignette
	template_name = 'grandvigne/index.html'
	form_class = vignetteForm
			

#training pages	
class t1(generic.ListView):
	model = createVigne
	template_name = 'grandvigne/tf/train1.html'
	
	def get_queryset(self):
		"""excludes any questions not published yet"""
		return HttpResponse("Hello, world. You're at the Vigne Index.")	
class t2(generic.ListView):
	model = createVigne
	template_name = 'grandvigne/tf/train2.html'
	
	def get_queryset(self):
		"""excludes any questions not published yet"""
		return HttpResponse("Hello, world. You're at the Vigne Index.")

class t3(generic.ListView):
	model = Vignette
	template_name = 'grandvigne/tf/train3.html'
	form_class = vignetteForm
	
	def get(self, request): 
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})
		
	def post(self, request): 
		form = self.form_class(request.POST)
	
		if form.is_valid():
			vign = form.save(commit = False)
			domainField = form.cleaned_data['domainField']

			vign.save()		
			request.session['interactionText'] = vign.interaction_text
			request.session['domainField'] = domainField

		return redirect('grandvigne:training4')
		
class t4(generic.ListView):
	model = Vignette
	template_name = 'grandvigne/tf/train4.html'
	form_class = descriptionForm
	
	def get_context_data(self, **kwargs):
		context = super(t4, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
		
	def get(self,request):

		interactionText =	request.session['interactionText'] 
		domainField = request.session['domainField'] 

		if (1==1):
			#A Form Set
			dForma = descriptionForm(prefix = str(0), instance = descriptionStatement())
			varForma = variableForm( prefix = str(0), instance = Variable())
			levFormsa = [levelForm(prefix = str(x), instance = levelModel()) for x in range(0,3)]

			#B Form Set
			dFormb = descriptionForm(prefix = str(1), instance = descriptionStatement())
			varFormb = variableForm( prefix = str(1), instance = Variable())
			levFormsb = [levelForm(prefix = str(x+4), instance = levelModel()) for x in range(0,3)]


			#C Form Set
			dFormc = descriptionForm(prefix = str(2), instance = descriptionStatement())
			varFormc = variableForm( prefix = str(2), instance = Variable())
			levFormsc = [levelForm(prefix = str(x+8), instance = levelModel()) for x in range(0,3)]

			#D Form Set
			dFormd = descriptionForm(prefix = str(3), instance = descriptionStatement())
			varFormd = variableForm( prefix = str(3), instance = Variable())
			levFormsd = [levelForm(prefix = str(x+12), instance = levelModel()) for x in range(0,3)]
		
		get_dict = {'desc_form_0':dForma,'desc_form_1':dFormb, 'desc_form_2':dFormc, 'desc_form_3':dFormd,
					'var_form_0':varForma,'var_form_1':varFormb, 'var_form_2':varFormc, 'var_form_3':varFormd,
					'lev_form_0':levFormsa,'lev_form_1':levFormsb, 'lev_form_2':levFormsc, 'lev_form_3':levFormsd}
		
		return render(request, 'grandvigne/tf/train4.html', get_dict)

	def post(self, request, *args, **kwargs):

		if (1 == 1):
			#A Form Set
			dForma = descriptionForm(request.POST,prefix = str(0), instance = descriptionStatement())
			varForma = variableForm( request.POST,prefix = str(0), instance = Variable())
			levFormsa = [levelForm(request.POST,prefix = str(x), instance = levelModel()) for x in range(0,3)]

			#B Form Set
			dFormb = descriptionForm(request.POST,prefix = str(1), instance = descriptionStatement())
			varFormb = variableForm(request.POST, prefix = str(1), instance = Variable())
			levFormsb = [levelForm(request.POST,prefix = str(x+4), instance = levelModel()) for x in range(0,3)]


			#C Form Set
			dFormc = descriptionForm(request.POST,prefix = str(2), instance = descriptionStatement())
			varFormc = variableForm( request.POST,prefix = str(2), instance = Variable())
			levFormsc = [levelForm(request.POST,prefix = str(x+8), instance = levelModel()) for x in range(0,3)]

			#D Form Set
			dFormd = descriptionForm(request.POST,prefix = str(3), instance = descriptionStatement())
			varFormd = variableForm(request.POST, prefix = str(3), instance = Variable())
			levFormsd = [levelForm(request.POST,prefix = str(x+12), instance = levelModel()) for x in range(0,3)]
			
		if request.POST.get("countVals") == 'count':
			print('One Description Set)')
			if (dForma.is_valid() and varForma.is_valid() and (all([lf.is_valid() for lf in levFormsa]))):
				new_descript = dForma.save()
				new_var = varForma.save(commit = False)
				i = 1
				for lf in levFormsa:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					new_level.save()
					request.session['levelsa'+str(i)] = new_var.levels.level_option
					i = i + 1
				new_var.save()	
				request.session['descTexta'] = new_descript.description_text
				request.session['VarTexta'] = new_var.variable_text

		elif request.POST.get("countVals") == 'count2':
			print('Two Description Sets')

			if (dForma.is_valid() and varForma.is_valid() and (all([lf.is_valid() for lf in levFormsa]))):
				new_descript = dForma.save()
				i = 1
				for lf in levFormsa:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					new_level.save()
					request.session['levelsa'+str(i)] = new_var.levels.level_option
					i = i + 1
				new_var.save()	
				request.session['descTexta'] = new_descript.description_text
				request.session['VarTexta'] = new_var.variable_text
					
			if (dFormb.is_valid() and varFormb.is_valid() and (all([lf.is_valid() for lf in levFormsb]))):
				new_descript = dFormb.save()
				new_var = varFormb.save(commit = False)
				i =1
				for lf in levFormsb:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					request.session['levelsb'+str(i)] = new_var.levels.level_option
					new_level.save()
					i = i + 1
				new_var.save()	
				request.session['descTextb'] = new_descript.description_text
				request.session['VarTextb'] = new_var.variable_text
		
		elif request.POST.get("countVals") == 'count3':
			print('Three Description Sets)')

			if (dForma.is_valid() and varForma.is_valid() and (all([lf.is_valid() for lf in levFormsa]))):
				new_descript = dForma.save()
				new_var = varForma.save(commit = False)
				for lf in levFormsa:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					new_level.save()
				new_var.save()
					
			if (dFormb.is_valid() and varFormb.is_valid() and (all([lf.is_valid() for lf in levFormsb]))):
				new_descript = dFormb.save()
				new_var = varFormb.save(commit = False)
				for lf in levFormsb:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					new_level.save()
				new_var.save()
			if (dFormc.is_valid() and varFormc.is_valid() and (all([lf.is_valid() for lf in levFormsc]))):
				new_descript = dFormc.save()
				new_var = varFormc.save(commit = False)
				for lf in levFormsc:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					new_level.save()
				new_var.save()
		elif request.POST.get("countVals") == 'count4':
			print('Four Description Sets)')

			if (dForma.is_valid() and varForma.is_valid() and (all([lf.is_valid() for lf in levFormsa]))):
				new_descript = dForma.save()
				i = 1
				for lf in levFormsa:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					new_level.save()
					request.session['levelsa'+str(i)] = new_var.levels.level_option
					i = i + 1
				new_var.save()	
				request.session['descTexta'] = new_descript.description_text
				request.session['VarTexta'] = new_var.variable_text
					
			if (dFormb.is_valid() and varFormb.is_valid() and (all([lf.is_valid() for lf in levFormsb]))):
				new_descript = dFormb.save()
				new_var = varFormb.save(commit = False)
				i =1
				for lf in levFormsb:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					request.session['levelsb'+str(i)] = new_var.levels.level_option
					i = i + 1
					new_level.save()
				new_var.save()	
				request.session['descTextb'] = new_descript.description_text
				request.session['VarTextb'] = new_var.variable_text
		
			if (dFormc.is_valid() and varFormc.is_valid() and (all([lf.is_valid() for lf in levFormsc]))):
				new_descript = dFormc.save()
				new_var = varFormc.save(commit = False)
				i =1
				for lf in levFormsc:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					request.session['levelsc'+str(i)] = new_var.levels.level_option
					i = i + 1
					new_level.save()
				new_var.save()	
				request.session['descTextc'] = new_descript.description_text
				request.session['VarTextc'] = new_var.variable_text
		
			if (dFormd.is_valid() and varFormd.is_valid() and (all([lf.is_valid() for lf in levFormsd]))):
				new_descript = dFormd.save()
				new_var = varFormd.save(commit = False)

				for lf in levFormsd:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					request.session['levelsd'+str(i)] = new_var.levels.level_option
					i = i + 1
					new_level.save()
				new_var.save()	
				request.session['descTextd'] = new_descript.description_text
				request.session['VarTextd'] = new_var.variable_text
		

		return redirect('grandvigne:training5')
		#description counts, know there is always 1 check if more if not save there
		#return HttpResponseRedirect(reverse('grandvigne:training5'))
			
class t5(generic.ListView):
	model = createVigne
	template_name = 'grandvigne/tf/train5.html'
	
	def get(self, request):
		interactionText =	request.session['interactionText'] 
		domainField = request.session['domainField']
			
		if request.get("countVals") == 'count':
			print(' um its count')
		descTexta=		request.session['descTexta']
		VarTexta =		request.session['VarTexta'] 
		levelsa1 =		request.session['levels1a'] 
		levelsa2 =		request.session['levels2a'] 
		levelsa3 =		request.session['levels3a'] 
		renderDict = {"interactionText": interactionText, "domainField": domainFielda, "descText":descTexta,
						"VarText": VarTexta, "levels1":levelsa1,"levels2":levelsa2,"levels3":levelsa3}
	
		return render(request, self.template_name, renderDict)

		
class UserRegistrationView(generic.ListView):
	form_class = registerForm
	template_name = 'grandvigne/registration-form.html'
	
	#display blank form 
	def get(self, request): 
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})
		
	# process form data
	def post(self, request): 
		form = self.form_class(request.POST)
		
		if form.is_valid():
			user = form.save(commit = False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			
			user.set_password(password)
			user.save()
			
			user = authenticate(username=username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('grandvigne:index')
					#redirect success page
			#else: 
				#cry and return invalid login
		
		return render(request, self.template_name, {'form': form})

		
	
def	addDesc(request, vignette_id):
	vignette = get_object_or_404(Vignette, pk=vignette_id)
	
	try:
		print(request.POST)
		description = vignette.descriptionStatement_set.get(pk=request.POST['descriptionStatement'])
	except (KeyError, descriptionStatement.DoesNotExist):
		return render(request, 'grandvigne/index.html', {'vignette': vignette,'error_message': "You didn't ente a descStatement.",})
	else:
		description.description_text = vignette.cleaned_data['domainField']
		description.save()
		
		return HttpResponseRedirect(reverse('grandvigne:training5', args=(vignette.id,)))
		
		
# Multiple Form Handling References
# https://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/#more-84

"""
			dForm = descriptionForm(request.POST, instance = descriptionStatement())
			varForm = [variableForm(request.POST, instance = Variable())]
			levForms = [levelForm(request.POST, prefix = str(x), instance = levelModel()) for x in range(0,3)]
		
		form_list = [dForm, varForm, levForms]
			
		if (dForm.is_valid() and all([vf.is_valid() for vf in varForm]) and all([lf.is_valid() for lf in levForms])):
			print('validForm')
			new_descript = dForm.save()

			for vf in varForm:
				new_var = vf.save(commit = False)
				for lf in levForms:
					new_level = lf.save(commit = False)
					new_var.levels = new_level
					new_level.save()
				new_var.save()
				
"""

"""	
	def formHandle(self, request):
		prefix_list = ['a','b','c','d']
		for a in prefix_list:
			dForm[a] = descriptionForm(request.POST, a)
			varForm[a] = variableForm(request.POST, a)
			levForms[a] = levelForm(request.POST, a)
		
			if (dForm[a].is_valid() and all([vf.is_valid() for vf in varForm[a]]) and all([lf.is_valid() for lf in levForms[a]])):
				print('validForm')
				new_descript = dForm[a].save()

				for vf in varForm[a]:
					new_var = vf.save(commit = False)
					for lf in levForms[a]:
						new_level = lf.save(commit = False)
						new_var.levels = new_level
						new_level.save()
					new_var.save()
"""	