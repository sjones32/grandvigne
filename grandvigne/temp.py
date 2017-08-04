Model 

class SurveyResult(models.Model):
    stay = models.OneToOneField(Stay, related_name='survey')
    created = models.DateTimeField(default=datetime.now)
    vote = models.BooleanField(default=False)
    vote_service = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)

    def getThreads(self):
        return SurveyThread.objects.filter(parent_survey = self)

    threads = property(getThreads)

    def __unicode__(self):
        return self.vote and 'Good' or 'Bad'

    class Meta:
        get_latest_by = '-created'

class SurveyThread(models.Model):
    survey = models.ManyToManyField(SurveyResult, related_name='parent_survey')
    email = models.EmailField(max_length=200)
    comment = models.TextField(blank=True, null=True)