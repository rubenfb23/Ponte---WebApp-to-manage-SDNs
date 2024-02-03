from django.db import models

TYPE_CHOICES = [
    ('Educational', 'Educational'),
    ('Personal', 'Personal'),
    ('Business', 'Business'),
]


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    status = models.BooleanField(blank=True)
    port = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    status = models.BooleanField(blank=True)
    operating_system = models.CharField(max_length=20)
    services = models.ManyToManyField(Service, blank=True)
    private_ip = models.CharField(max_length=20)
    mac_address = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Network(models.Model):
    network_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.BooleanField()
    ip = models.CharField(max_length=20)
    subnet_mask = models.CharField(max_length=20)
    gateway = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    devices = models.ManyToManyField(Device)

    def __str__(self):
        return self.name


class Anchor(models.Model):
    anchor_id = models.AutoField(primary_key=True)
    public_ip = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.BooleanField()
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    state = models.BooleanField(blank=True)
    networks = models.ManyToManyField(Network)

    def __str__(self):
        return self.name
