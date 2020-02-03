from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
import time
from django.utils.text import slugify
from PIL import Image
from django.urls import reverse
from unidecode import unidecode
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField(validators = [MinValueValidator(0)])
    stock = models.IntegerField(validators = [MinValueValidator(0)], default = 0)
    description = models.TextField(max_length = 250)
    pub_date = models.DateTimeField(auto_now_add = True, verbose_name='first published date')
    last_date = models.DateTimeField(auto_now = True, verbose_name='last modified date')
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank=True)
    def get_image_path(instance, filename):
        current_time = time.strftime("%Y/%m/%d")
        return f"products/{current_time}/{filename}"
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True, default='/default.jpg')
    slug = models.SlugField(max_length = 50, blank = True, unique=True, allow_unicode=True)


    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(unidecode(self.name))
        super(Product, self).save(*args, **kwargs)
        #將圖片大小調整為200x200像素
        try:
            initial_path = self.image.path
            img = Image.open(self.image.open())
            size = 300, 300
            img_resize = img.thumbnail(size)
            img_resize.save(initial_path, quality=95)
        except:
            pass  

    def get_absolute_url(self):
        return reverse('product_detail', args = [self.slug])