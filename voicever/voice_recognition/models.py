from django.db.models import Model,FileField,OneToOneField,CASCADE
from django.contrib.auth.models import User
class AuthenticUserVoice(Model):
    sample = FileField(upload_to="voice")
    user = OneToOneField(User,related_name="voice",on_delete=CASCADE)
    def __str__(self):
        return self.user.username