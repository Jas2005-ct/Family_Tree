from django.db import models


class Person(models.Model):
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("O", "Other")]

    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100, blank=True)
    gender     = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    photo      = models.ImageField(upload_to="persons/", null=True, blank=True)
    bio        = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def full_name(self):
        return str(self)


class Relationship(models.Model):
    REL_TYPES = [
        ("spouse",  "Spouse"),
        ("parent",  "Parent -> Child"),
        ("sibling", "Sibling"),
    ]

    from_person   = models.ForeignKey(
        Person, related_name="relationships_from", on_delete=models.CASCADE
    )
    to_person     = models.ForeignKey(
        Person, related_name="relationships_to", on_delete=models.CASCADE
    )
    rel_type      = models.CharField(max_length=20, choices=REL_TYPES)
    marriage_date = models.DateField(null=True, blank=True)
    notes         = models.TextField(blank=True)

    class Meta:
        unique_together = ("from_person", "to_person", "rel_type")

    def __str__(self):
        return f"{self.from_person} --{self.rel_type}--> {self.to_person}"
