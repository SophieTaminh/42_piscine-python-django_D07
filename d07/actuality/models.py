from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# modele article
class Article(models.Model):
	title = models.CharField(max_length=64,null=False)
	#reference un enrg du model user
	author = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
	created = models.DateTimeField(default=timezone.now(),null=False)
	synopsis = models.CharField(max_length=312,null=False)
	content = models.TextField()

# Ce modèle doit également redéfinir la methode __str__ 
# afin que celle-ci renvoie l’attribut title
	def __str__(self):
		return(self.title)

# modele UserFavoriteArticle
class UserFavoriteArticle(models.Model):
	#reference un enrg du model user
	user = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
	#reference au title du modele Article
	article = models.ForeignKey(Article,null=False,on_delete=models.CASCADE)
	
# Ce modèle doit également redéfinir la methode __str__ 
# afin que celle-ci renvoie l’attribut title
	def __str__(self):
		return(self.article)

