from django.db import models
# Import the GateWay Model


# Create your models here.
class JobSeekerModel(models.Model):
    # Foreignkey from the GateWay Model, Limit to Seekers only
    """ 
    seeker = models.ForeignKey(User, on_delete=models.CASCADE,
        limit_choices_to= {'user__user_type': job_seeker},
        related_name='loginregister_user',
        blank=False, null=False
    )"""
    # cv
    name = models.CharField(max_length=100, null=False, blank=False)
    surname = models.CharField(max_length=100, null=False, blank=False)
    bio = models.CharField(max_length=1000, default='add bio')
    interview = models.IntegerField(null=True, blank=True)
    cv = models.FileField(upload_to='media/seeker/')

    def __str__(self) -> str:
        return self.name 
    
    class Meta:
        verbose_name_plural = 'Job Seeker Model'

    