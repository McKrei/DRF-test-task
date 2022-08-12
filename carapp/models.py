from django.utils.timezone import now
from django.db import models


class Color(models.Model):
    title = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.title


class Model(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.ForeignKey('Model', on_delete=models.PROTECT)
    color = models.ForeignKey('Color', on_delete=models.PROTECT)
    count = models.PositiveIntegerField()
    date  = models.DateTimeField(default=now, blank=True, null=True)

    def __str__(self):
        return f'Order №{self.id}: {self.model.brand} {self.model}, {self.color}, {self.count} cars'
