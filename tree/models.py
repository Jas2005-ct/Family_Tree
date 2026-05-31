from django.db import models


class Person(models.Model):
    GENERATION_CHOICES = [
        (1, 'Generation 1 - Grandparents'),
        (2, 'Generation 2 - Parents & Siblings'),
        (3, 'Generation 3 - Children'),
        (4, 'Generation 4 - Grandchildren'),
    ]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    ROLE_CHOICES = [
        ('grandfather', 'Grandfather'),
        ('grandmother', 'Grandmother'),
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('uncle', 'Uncle'),
        ('aunt', 'Aunt'),
        ('son', 'Son'),
        ('daughter', 'Daughter'),
        ('cousin', 'Cousin'),
        ('other', 'Other'),
    ]

    # Basic Info
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    generation = models.IntegerField(choices=GENERATION_CHOICES, default=2)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='other')
    birth_year = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    photo = models.ImageField(upload_to='persons/', null=True, blank=True)
    photo_url = models.URLField(blank=True, help_text='External photo URL if not uploading')

    # Relationships
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='children'
    )
    spouse = models.OneToOneField(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='spouse_of'
    )

    # Meta
    is_alive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['generation', 'name']
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return f"{self.name} ({self.get_role_display()}, Gen {self.generation})"

    def get_photo(self):
        """Return photo URL - uploaded or external"""
        if self.photo:
            return self.photo.url
        elif self.photo_url:
            return self.photo_url
        return None

    def get_children(self):
        return self.children.all()

    def get_siblings(self):
        if self.parent:
            return Person.objects.filter(parent=self.parent).exclude(pk=self.pk)
        return Person.objects.none()
