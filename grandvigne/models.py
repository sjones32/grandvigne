from django.db import models
from django.utils import timezone

#default model

class defaultModel(models.Model):
	title = models.CharField(max_length = 200, default='SOME STRING')

	text = models.CharField(max_length = 200, default='SOME STRING')

	def __str__(self):
		return self.title
		
#Vignette is the overall model 
#we want each vignette to consist of 1 description statement
#and between 2 and 4 interactionStatements
#the interaction statements should have variables with levels 


		
class levelModel(models.Model):
	level_option = models.CharField(max_length = 500, default='SOME STRING')	

	id = models.AutoField(primary_key=True)

	def __str__(self):
		return self.level_option
	
class Variable(models.Model):
	variable_text = models.CharField(max_length = 200, default='SOME STRING')	
	levels =  models.ForeignKey(levelModel, on_delete=models.CASCADE, null = True)
	
	id = models.AutoField(primary_key=True)

	def __str__(self):
		return self.variable_text
		
class descriptionStatement(models.Model):
	description_text = models.CharField(max_length = 500, blank =True)
	variable_text = models.ForeignKey(Variable,on_delete = models.CASCADE, null = True)	

	id = models.AutoField(primary_key=True)
	def get_queryset(self):
		return
	def __str__(self):
		return self.description_text

class Vignette(models.Model):
	domainField = models.CharField(max_length = 200, default='SOME STRING')
	interaction_text = models.CharField(max_length = 200, default='SOME Test')	
	description_text = models.ForeignKey(descriptionStatement, on_delete=models.CASCADE, null = True)	
	
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	id = models.AutoField(primary_key=True)

	def published(self): 
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.domainField
		
		
