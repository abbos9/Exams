from django.db import models

# Create your models here.


class FoodGalleryCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class FoodGalleryModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ManyToManyField(FoodGalleryCategoryModel, null = True)
    image = models.ImageField(upload_to='gallery')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'foodgallery'
        verbose_name_plural = 'foodgalleries'


class ReservationModel(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=100)
    num_of_people = models.IntegerField(default=1)
    date = models.CharField(max_length=100)
    contact_message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_name
    
    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"


class SubscribeModel(models.Model):
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"

class MenuModelCategory(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Menucategory"
        verbose_name_plural = "Menucategories"


class MenuModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Menu")
    icons = models.ImageField(upload_to="Menu_icons",)
    category = models.ForeignKey(MenuModelCategory, on_delete = models.CASCADE)
    about = models.TextField()
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'


class Comment(models.Model):
    icon = models.ImageField(upload_to="comments")
    first_name = models.CharField(max_length=100)
    description = models.TextField()
    job = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.first_name
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Events(models.Model):
    place = models.CharField(max_length=150)
    time = models.CharField(max_length=150)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="events")
    date = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

class ChefModel(models.Model):
    title= models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    about = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="chef_image")
    icon = models.ImageField(upload_to="chef_icon", null = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title
    
    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'
