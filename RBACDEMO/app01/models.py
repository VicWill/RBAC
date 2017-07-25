from django.db import models
from rbac import models as RbacModels


class UserInfo(models.Model):
    nickname = models.CharField(max_length=32)
    user = models.OneToOneField(RbacModels.User)

