from django.db.models import Model,UUIDField,CharField,OneToOneField,CASCADE
from django.contrib.auth.models import User
from random import randint,choice
from uuid import uuid4
class ChallengeResponse(Model):
    id = UUIDField(
        default=uuid4,
        primary_key=True,
        null=False,
        editable=False
    )
    challenge_message = CharField(
        null=False
    )
    response_message = CharField(
        null=False
    )
    user = OneToOneField(
        User,
        related_name="challenge",
        on_delete=CASCADE
    )
    