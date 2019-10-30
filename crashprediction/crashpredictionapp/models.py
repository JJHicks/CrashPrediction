from django.db import models

# Create your models here.
class Crashdata(models.Model):
    crash_id = models.TextField(db_column='Crash ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adjusted_average_daily_traffic_amount = models.TextField(db_column='Adjusted Average Daily Traffic Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    commercial_motor_vehicle_flag = models.TextField(db_column='Commercial Motor Vehicle Flag', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    crash_death_count = models.TextField(db_column='Crash Death Count', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    crash_time = models.TextField(db_column='Crash Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    crash_total_injury_count = models.TextField(db_column='Crash Total Injury Count', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    curve_degrees = models.TextField(db_column='Curve Degrees', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    curve_type = models.TextField(db_column='Curve Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    day_of_week = models.TextField(db_column='Day of Week', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inside_shoulder_width_on_divided_highway = models.TextField(db_column='Inside Shoulder Width on Divided Highway', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    latitude = models.TextField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    light_condition = models.TextField(db_column='Light Condition', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    longitude = models.TextField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    manner_of_collision = models.TextField(db_column='Manner of Collision', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_lanes = models.TextField(db_column='Number of Lanes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_struck = models.TextField(db_column='Object Struck', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    outside_shoulder_width_on_divided_highway = models.TextField(db_column='Outside Shoulder Width on Divided Highway', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    property_damages = models.TextField(db_column='Property Damages', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    road_class = models.TextField(db_column='Road Class', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    street_name = models.TextField(db_column='Street Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    street_number = models.TextField(db_column='Street Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    surface_condition = models.TextField(db_column='Surface Condition', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    weather_condition = models.TextField(db_column='Weather Condition', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    driver_alcohol_result = models.TextField(db_column='Driver Alcohol Result', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.crash_id

    class Meta:
        managed = False
        db_table = 'CrashData'
