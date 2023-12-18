from django.db import models

# Create your models here.
class Airplane(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    plane_id: models.IntegerField = models.IntegerField()
    passenger_assumptions: models.IntegerField = models.IntegerField()

    def fuel_consumption_per_minute(self) -> float:
        return 0.80 * self.plane_id + 0.002 * self.passenger_assumptions

    def fuel_tank_capacity(self) -> float:
        return 200 * self.plane_id

    def max_minutes_fly(self) -> float:
        return self.fuel_tank_capacity() / self.fuel_consumption_per_minute()