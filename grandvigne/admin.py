from django.contrib import admin

# Register your models here.
from .models import defaultModel, Vignette
from .models import descriptionStatement, Variable, levelModel 



class DescriptionInline(admin.TabularInline):
		model = descriptionStatement
		extra = 1
class LevelsInline(admin.TabularInline):
		model = levelModel
		extra = 1
	
class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['domainField', 'interaction_text','description_text']}), 
		('Date information', {'fields': ['created_date'], 'classes': ['collapse']}),
	]
	#inlines = [DescriptionInline,LevelsInline]
	list_display = ('domainField','created_date')
	list_filter = ['created_date']
	search_fields = ['domainField']



#admin.site.register(defaultModel)
admin.site.register(Vignette,TutorialAdmin)
admin.site.register(descriptionStatement)
admin.site.register(Variable)
admin.site.register(levelModel)

