from django.db import models
from django.core.files import File
from taggit.managers import TaggableManager
from accounts.models import Account    

from io import BytesIO
from PIL import Image

# Create your models here.

#Category for each listings
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


#real estate listing class
class Listing(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')

    )
    category = models.ForeignKey(Category, related_name='listings', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) 
    price = models.FloatField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    num_sittingrooms = models.IntegerField()
    num_kitchens = models.IntegerField()
    square_feet = models.FloatField(null= True, blank=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    description = models.TextField(null= True, blank=True)
    created_by = models.ForeignKey(Account, related_name='listings', default= 1, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to= 'uploads/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    tags = TaggableManager(blank=True)
    

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):                  #str here is used to rrepresent string of an object in python, self is an instance of the class listing, we want our  class to be represneted in our database where its stored as the title attribute 
        return self.title
    
    #resize image
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url 
            else:
                return 'https://via.placeholder.com/240x240x.jpg'
            
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        
        return thumbnail
       
    
   
