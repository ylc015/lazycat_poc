from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    OPEN = 1
    CLOSED = 2

    OPENING_STATUS = (
        (OPEN, 'open'),
        (CLOSED, 'closed'),
        )

    BREAKFAST = 1
    LAUNCH = 2
    DINNER = 3
    DELIVERY = 4
    CAFE = 5
    LUXURY = 6
    NIGHT = 7

    FEATURE_CHOICES = (
        (BREAKFAST, 'breakfast'),
        (LAUNCH, 'launch'),
        (DINNER, 'dinner'),
        (DELIVERY, 'delivery'),
        (CAFE, 'cafe'),
        (LUXURY, 'luxury dining'),
        (NIGHT, 'night life'),
        )

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


    TIMING_CHOICES = (
        (MONDAY, 'monday'),
        (TUESDAY, 'tuesday'),
        (WEDNESDAY, 'wednesday'),
        (THURSDAY, 'thursday'),
        (FRIDAY, 'friday'),
        (SATURDAY, 'saturday'),
        (SUNDAY, 'sunday'),
        )
    user = models.ForeignKey(User)
    restaurant_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    restaurant_phone_number = models.PositiveIntegerField()
    restaurant_email = models.EmailField(blank=True, null=True)
    owner_email = models.EmailField(blank=True, null=True)
    opening_status = models.IntegerField(choices=OPENING_STATUS, default=OPEN)
    email = models.EmailField()
    restaurant_website = models.TextField(validators=[URLValidator()])
    features = models.IntegerField(choices=FEATURE_CHOICES, default=DINNER)
    timings = models.IntegerField(choices=TIMING_CHOICES, default=MONDAY)
    opening_from = models.TimeField()
    opening_to = models.TimeField()
    facebook_page = models.TextField(validators=[URLValidator()])
    twitter_handle = models.CharField(max_length=80, blank=True, null=True)
    other_details = models.TextField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'
        ordering = ('restaurant_name',)
        index_together = (('id','slug'),)


    def __str__(self):
        return self.restaurant_name

    # def get_absolute_url(self):
    #   return reverse('restaurant:restaurant_detail', args=[self.id, self.slug])



class Category(models.Model):
    name = models.CharField(max_length=120,db_index=True) #veg, non-veg
    slug = models.SlugField(max_length=120,db_index=True)

    class Meta:
        ordering=('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Menu(models.Model):
    category = models.ForeignKey(Category, related_name="menu")
    restaurant = models.ForeignKey(Restaurant, related_name="restaurant_menu")
    name = models.CharField(max_length=120,db_index=True)
    slug = models.SlugField(max_length=120,db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering=('name', )
        index_together = (('id', 'slug'), )
        verbose_name = 'menu'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #   return reverse('restaurant:menu_detail', args=[self.id, self.slug])


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
