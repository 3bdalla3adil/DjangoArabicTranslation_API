from django.db   import models
# from .arabic_keyword_api  import stringutils


class keyword(models.Model):

    keyword_text = models.CharField("KeyWord",max_length=150)

    def __str__(self):
        return self.keyword_text

    
# Create your models here.