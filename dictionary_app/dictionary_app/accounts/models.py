from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_model

from dictionary_app.core.validators import validate_only_letters


# Create your models here.


class AppUser(auth_model.AbstractUser):
    MAX_FIRST_NAME_LEN = 20
    MIN_FIRST_NAME_LEN = 5
    MAX_LAST_NAME_LEN = 20
    MIN_LAST_NAME_LEN = 5
    MAX_USER_NAME_LEN = 20
    MIN_USER_NAME_LEN = 5

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME_LEN),
            validate_only_letters,
        ),
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        validators=(
            MinLengthValidator(MIN_LAST_NAME_LEN),
            validate_only_letters,
        ),
        blank=False,
        null=False,
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )
    picture = models.ImageField(upload_to='user_photos/')
