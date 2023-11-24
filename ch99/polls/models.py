from django.db import models

"""
<form action="/url/" method="post">
    <label for ="your_name"?Your name: </label>
    <input id="your_name" type="text" name="your_name">
    <input type="submit" value="OK">
</form>
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text