from django.db import models

# Create your models here.

class Character(models.Model):
    firstname = models.CharField("Character's first name", max_length=30)
    lastname = models.CharField("Character's last name", max_length=30)
    curr_time = models.IntegerField("Current time in story")
    ability = models.CharField("Character's adapted ability (if applicable)", max_length=30)
    role = models.CharField("Character's role", max_length=20)
    description = models.CharField("Current description of character", max_length=300)
    items = models.CharField("Current inventory of character", max_length=300)
    relations = models.CharField("Current relations relevant to character in this timeframe", max_length=300)
    
    class Meta:
        #primary keys cannot be composite in Django atm, so this forces the fields that would be in the composite key to be unique 
        constraints =[models.UniqueConstraint(fields=["firstname","lastname","curr_time"], name="mock_pk"),]


