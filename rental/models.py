from django.db import models


# Create your models here.

class BikeCategory(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='images/categories', blank=True)
    price = models.PositiveSmallIntegerField(default=20)

    STATUS_CHOICES = [
        ('D', 'Draft'),
        ('P', 'Published'),
    ]
    published = models.CharField(max_length=1, choices=STATUS_CHOICES, default='D',)

    def __str__(self):
        return self.title

    def get_image(self):
        return self.image.url


class RandomManager(models.Manager):
    def get_queryset(self, rows=None):
        if rows is None:
            return super().get_queryset().all().order_by('?')
        else:
            return super().get_queryset().all().order_by('?')[:rows]


class Bike(models.Model):
    class Meta:
        verbose_name = 'Bike'
        verbose_name_plural = 'Bikes'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='images/bikes', blank=True, unique=True)
    image_rotated = models.ImageField(upload_to='images/rotated', blank=True, unique=True)

    category = models.ForeignKey(to=BikeCategory, on_delete=models.CASCADE)

    objects = models.Manager()
    randomized = RandomManager()

    def __str__(self):
        return self.title

    def get_image(self):
        return self.image.url

    def get_rotated_image(self):
        return self.image_rotated.url


class BikeOptions(models.Model):
    class Meta:
        verbose_name = 'BikeOption'
        verbose_name_plural = 'BikeOptions'

    BRAKE_CHOICES = [
        ('DM', 'Disc Mechanical'),
        ('DH', 'Disc Hydraulic'),
        ('DP', 'Dual-Pivot'),
        ('VB', 'MTB V-Brake'),
        ('CN', 'Cantilever'),
    ]

    color = models.CharField(max_length=50)
    groupset = models.CharField(max_length=80)
    size = models.PositiveSmallIntegerField(default=50)
    brakes = models.CharField(
        max_length=2,
        choices=BRAKE_CHOICES,
        default='DH',
    )
    bike = models.ForeignKey(to=Bike, on_delete=models.CASCADE)


class LatestManager(models.Manager):
    def get_queryset(self, rows=None):
        if rows is None:
            return super().get_queryset().all()
        else:
            return super().get_queryset().all()[:rows]


class News(models.Model):
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Newses'
        ordering = ['-created']

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/news', blank=True, unique=True)
    created = models.DateField(auto_now=True)

    objects = models.Manager()
    latest = LatestManager()

    published = models.CharField(
        max_length=1,
        choices=[('D', 'Draft'), ('P', 'Published'), ],
        default='D',
    )

    def __str__(self):
        return str(self.created) + ' ' + self.slug

    def get_image(self):
        return self.image.url

