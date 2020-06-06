from django.db import models


class InitiativeVoite(models.Model):

    initiative = models.ForeignKey('initiative.Initiative', related_name='initiative_voite',
                                   on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='initiative_voite_user',
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = ['initiative', 'user']


class LeaderVoite(models.Model):

    leader = models.ForeignKey('users.User', related_name='leader_voite',
                               on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='leader_voite_user',
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = ['leader', 'user']
