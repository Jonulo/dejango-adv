"""Circle model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModel

class Circle(CRideModel):
    """Circle model.

    A circle is a private group where rides are offered and taken
    by irs members. To join a circle a user must receive an unique
    invitation code from an existing circle member.
    """

    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle Description', max_length=255)
    picture = models.ImageField(upload_to='circle/picture', blank=True, null=True)

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles are also known as official communities.'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Public circles are listed in the main page so everyone know about their existence.'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to fixed numbers of members'
    )
    members_limit = models.PositiveIntegerField(
        default=True,
        help_text='If circle is limited, this will be the limit on the numbers of members'
    )

    def __str__(self):
        """Return circle name."""
        return self.name

    # We need to use the same Meta like ./utils/models.py so we can INHERIT the class:
    class Meta(CRideModel.Meta):
        """Meta class."""

        # We just need to modify this value to get the RESPONSE in this way:
        ordering = ['-rides_taken', '-rides_offered']
