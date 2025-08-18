from django.db.models import Model,FileField,OneToOneField,CASCADE
from django.contrib.auth.models import User
def register(instance,filename):
    return f"register/{instance.user.username}_registration.wav"
def verify(instance,filename):
    return f"verify/{instance.user.username}_verification.wav"
class RegistrationUserVoice(Model):
    sample = FileField(upload_to=register)
    user = OneToOneField(User,related_name="register",on_delete=CASCADE)
    def __str__(self):
        return self.user.username
class VerificationUserVoice(Model):
    sample = FileField(upload_to=verify)
    user = OneToOneField(User,related_name="verify",on_delete=CASCADE)
    def __str__(self):
        return self.user.username