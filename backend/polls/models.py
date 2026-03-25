from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    @property
    def total_votes(self):
        return sum(opt.votes for opt in self.options.all())


class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=255)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.text} ({self.votes} votos)"
