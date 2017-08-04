from django.conf.urls import url

from . import views 
from . import forms

from grandvigne.forms import descriptionForm, vignetteForm

app_name = 'grandvigne'


#tutWiz = tutorialViewWizard.as_view(TRANSF_FORMS, url_name = 'interactionstep', done_step_name = 'training5')
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	url(r'^register/$', views.UserRegistrationView.as_view(), name='register'),
	url(r'^training$', views.t1.as_view(), name = 'training'),
	url(r'^training/2$', views.t2.as_view(), name = 'training2'),
	url(r'^training/3$', views.t3.as_view(), name = 'training3'),
	url(r'^training/4$', views.t4.as_view(), name = 'training4'),
	url(r'^training/5$', views.t5.as_view(), name = 'training5'),
#	url(r'^addDesc/$', views.addDesc, name='addDesc'),
]