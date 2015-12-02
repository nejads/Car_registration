
user = User(name='Sou', email='sou@gmail.com', credential=cred, plate='121', bank='0543', tel='00765')

from carreg_app import models
from carreg_app.models import User, Credential, Refuel

user = User.objects.get(email="ali@gmail.com")
cred = Credential.objects.get(pk=user.id)
user


DROP SCHEMA public CASCADE;CREATE SCHEMA public;