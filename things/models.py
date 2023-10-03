from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# class Thing(models.Model):
#     name = models.CharField(default = "", max_length=30, unique=True, blank=False)
#     description = models.TextField(blank=True, max_length=120)
#     quantity = models.IntegerField(
#         validators=[
#             MaxValueValidator(100),
#             MinValueValidator(0)
#         ]
#     )



class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        verbose_name="Name"
    )
    description = models.TextField(
        max_length=120,
        blank=True,
        verbose_name="Description"
    )
    quantity = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        verbose_name="Quantity"
    )

    def __str__(self):
        return self.name