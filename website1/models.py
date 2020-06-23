from django.db import models




class Team(models.Model):
    name = models.CharField(max_length=250)
    ids = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Members(models.Model):
    team= models.ForeignKey(Team,on_delete=models.CASCADE)
    members_name=models.CharField(max_length=250)

    def __str__(self):
        return self.members_name

