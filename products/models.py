from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
import time
from django.utils.text import slugify
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField(validators = [MinValueValidator(0)])
    stock = models.IntegerField(validators = [MinValueValidator(0)], default = 0)
    description = models.TextField(max_length = 250)
    pub_date = models.DateTimeField(auto_now_add = True)
    last_date = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank=True)
    def get_image_path(instance, filename):
        current_time = time.strftime("%Y/%m/%d")
        return f"products/{current_time}/{filename}"
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    slug = models.SlugField(max_length = 50, blank = True, null = True)
    

    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', args = [self.slug])