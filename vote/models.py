from django.db import models


class InitiativeVote(models.Model):

    initiative = models.ForeignKey('initiative.Initiative',
                                   related_name='initiative_vote',
                                   on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='initiative_vote_user',
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = ['initiative', 'user']


class LeaderVote(models.Model):

    leader = models.ForeignKey('users.User', related_name='leader_vote',
                               on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='leader_vote_user',
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = ['leader', 'user']
