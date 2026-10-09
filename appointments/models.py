from django.db import models


class Practitioner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Dr {self.first_name} {self.last_name}"


class Patient(models.Model):
    class Gender(models.TextChoices):
        FEMALE = "F", "Femme"
        MALE = "M", "Homme"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=Gender.choices)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Appointment(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Prévu"
        COMPLETED = "completed", "Honoré"
        NO_SHOW = "no_show", "Absent"
        CANCELLED = "cancelled", "Annulé"

    patient = models.ForeignKey(
        Patient, on_delete=models.PROTECT, related_name="appointments"
    )
    practitioner = models.ForeignKey(
        Practitioner, on_delete=models.PROTECT, related_name="appointments"
    )
    start_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=30)
    reason = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.SCHEDULED
    )
    sms_reminder_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["start_at"]

    def __str__(self):
        return f"{self.patient} - {self.start_at:%d/%m/%Y %H:%M}"
