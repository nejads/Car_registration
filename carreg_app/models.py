from django.db import models
import uuid
from . import utils
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
)


class UserManager(BaseUserManager):
    def create_user(self, name=None, email=None, password=None, plate=None,
                    tag_id=None, bank=None, tel=None):
        if (not email) or (not name) or (not plate) or (not bank) or (
                not tel) or (not password):
            raise ValueError('Some information missing')

        tag_id = uuid.uuid4()
        user = self.model(
            name=name,
            email=self.normalize_email(email),
            plate=plate,
            bank=bank,
            tel=tel,
            tag_id=tag_id,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, email, password):
        user = self.create_user(
            name,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User (AbstractBaseUser):
    tag_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    plate = models.CharField(max_length=30)
    bank = models.CharField(max_length=30)
    tel = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'plate', 'bank', 'tel']

    def __str__(self):
        return ('id: {} tag_id: {} name: {} email: {}'
                'plate: {} bank: {} tel: {}'.
                format(self.id, self.tag_id, self.name, self.email,
                       self.plate, self.bank, self.tel))


class Refuel (models.Model):
    user = models.ForeignKey('User', related_name='refuels')
    line = models.CharField(max_length=23)
    consumption = models.PositiveIntegerField()
    refuel_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ('id: {} user: {} line: {} consumption: {} refuel_time: {}'.
                format(self.id, self.user, self.line, self.consumption,
                       self.refuel_time))
