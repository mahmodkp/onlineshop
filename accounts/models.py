from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(_("mobile number"), max_length=50)
    address = models.CharField(_("adress"), max_length=400)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # def get_full_name(self) -> str:
    #     return f''
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     pass
#     # add additional fields in here

#     def __str__(self):
#         return self.usernamep