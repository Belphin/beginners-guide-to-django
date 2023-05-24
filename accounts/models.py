from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	READER = 0
	BLOGGER = 1

	ROLE_TYPE = (
		(READER, "Reader"),
		(BLOGGER, "Blogger"),
	)

	role = models.PositiveSmallIntegerField(choices=ROLE_TYPE)