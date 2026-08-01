from django.db import models
from django.urls import reverse
from decimal import Decimal

class Professional(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='professionals/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField(max_length=160, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    duration_minutes = models.PositiveIntegerField(default=30, help_text="Duration in minutes")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    professionals = models.ManyToManyField(Professional, blank=True, related_name='services')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', args=[self.slug])


class Booking(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    PAYMENT_PERSON = 'person'
    PAYMENT_CARD = 'card'
    PAYMENT_CHOICES = [
        (PAYMENT_PERSON, 'Pay in Person'),
        (PAYMENT_CARD, 'Card Payment'),
    ]

    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='bookings')
    professional = models.ForeignKey(Professional, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    customer_name = models.CharField(max_length=140)
    customer_phone = models.CharField(max_length=30)
    customer_email = models.EmailField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default=PAYMENT_PERSON)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-appointment_date', '-appointment_time']

    def __str__(self):
        return f'Booking #{self.id} - {self.service.name} for {self.customer_name}'

    def save(self, *args, **kwargs):
        # ensure total_price is set (default to service.price if not provided)
        if not self.total_price:
            self.total_price = self.service.price
        super().save(*args, **kwargs)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name