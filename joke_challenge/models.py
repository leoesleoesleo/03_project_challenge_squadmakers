from django.db import models


class Joke(models.Model):
	id = models.AutoField(primary_key=True)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	joke = models.CharField(max_length=100)
	is_active = models.BooleanField(default=True)
