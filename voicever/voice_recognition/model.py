from django.db.models import Model,FileField,ForeignKey,CASCADE,UniqueConstraint
from django.contrib.auth.models import User
class AuthenticUserVoice(Model):
    sample = FileField(upload_to="voice")
    user = ForeignKey(User,related_name="voice",on_delete=CASCADE)
    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['sample','user'],
                name='one-sample-one-user-unique'
            )
        ]
    