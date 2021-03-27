from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

CATEGORY_CHOICES = (
    ('categorie1', 'categorie1'),
    ('categorie2', 'categorie2'),
    ('categorie3', 'categorie3'),
    ('categorie4', 'categorie4'),
)

DEPARTMENT_CHOICES = (
    ('IT', 'IT'),
    ('Finante', 'Finante'),
    ('Contabilitate', 'Contabilitate'),
    ('Support', 'Support'),
)

class Ticket(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=220, null=False, unique=True)
    author = models.CharField(max_length=300)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    departament = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ticket:ticket_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

