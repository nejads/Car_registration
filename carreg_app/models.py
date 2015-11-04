from django.db import models
from . import utils


class User (models.Model):
    tag_id = models.CharField(unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    credential = models.OneToOneField('Credential')
    plate = models.CharField(max_length=30)
    bank = models.CharField(max_length=30)
    tel = models.CharField(max_length=23)
    registration_time = models.DateTimeField(auto_now_add=True)
    latest_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('id: {} tag_id: {} name: {} email: {}'
                'credential_id: {} plate: {} bank: {} tel: {}'
                'registration_time: {} latest_modification: {}'.
                format(self.id, self.tag_id, self.name, self.email,
                       self.credential.id, self.plate, self.bank, self.tel,
                       self.registration_time, self.latest_modification))


class Credential (models.Model):
    encrypted_pass = models.CharField(max_length=128)
    salt = models.CharField(max_length=50)

    def __str__(self):
        return ('id: {} salt: {}'.format(self.id, self.salt))


class Refuel (models.Model):
    user = models.ForeignKey('User', related_name='refuels')
    line = models.CharField(max_length=23)
    consumption = models.PositiveIntegerField()
    refuel_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ('id: {} user: {} line: {} consumption: {} refuel_time: {}'.
                format(self.id, self.user, self.line, self.consumption,
                       self.refuel_time))
