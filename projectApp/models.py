from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_age = models.IntegerField(blank=True,null=True)
    user_email = models.EmailField(max_length=100)
    user_picture = models.ImageField(upload_to='images/user_picture',blank=True,null=True,)
    user_address = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.user_name}'

    class Meta:
        db_table = 'User'


class Seat(models.Model):
    seat_id = models.AutoField(primary_key=True)
    total_seats = models.IntegerField()
    booked_seats = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f'{self.seat_id}'

    def available_seats(self):
        return self.total_seats - self.booked_seats

    class Meta:
        db_table = 'Seat'

# class Boarddroppoints(models.Model):
#     point_id=models.AutoField(primary_key=True)
#     stop_name = models.CharField(max_length=100)
#     def __str__(self):
#         return f'{self.stop_name}'

#     class Meta:
#         db_table = 'BoardDropPoints'



class Stop(models.Model):
    stop_id = models.AutoField(primary_key=True)
    stop_name = models.CharField(max_length=100)
    # points=models.ForeignKey(Boarddroppoints, on_delete=models.CASCADE,null=True,related_name='points')

    def __str__(self):
        return f'{self.stop_name}'
 
    class Meta:
        db_table = 'Stops'



class Fare(models.Model):
    fare_id = models.AutoField(primary_key=True)
    source_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='fare_source')
    destination_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='fare_destination')
    fare = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.source_stop} to {self.destination_stop} : ${self.fare}'

    class Meta:
        db_table = 'Fare'


class Bus(models.Model):
    bus_id = models.AutoField(primary_key=True)
    bus_name = models.CharField(max_length=100)
    bus_type = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    seats = models.ManyToManyField(Seat,blank=False)
    stops = models.ManyToManyField(Stop)
    source_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='bus_source_stop')
    destination_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='bus_destination_stop')

    def __str__(self):
        return f'{self.bus_name} - {self.source_stop} to {self.destination_stop}'

    def total_available_seat(self):
        return self.seats.available_seats()

    class Meta:
        db_table = 'Bus'


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    passenger_age = models.IntegerField()
    booking_time = models.DateTimeField()
    source_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='booking_source_stop')
    destination_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='booking_destination_stop')

    def __str__(self):
        return f'{self.passenger_name}'

    class Meta:
        db_table = 'Booking'
