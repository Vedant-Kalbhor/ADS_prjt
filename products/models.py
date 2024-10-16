from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver



class Laptop(models.Model):
    brand = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    processor = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    graphics_card = models.CharField(max_length=255)
    laptop_type = models.CharField(max_length=255, choices=[('Professional', 'Professional'), ('Gaming', 'Gaming'), ('Daily Use', 'Daily Use')])
    image_url = models.URLField(max_length=500)
    rating = models.IntegerField(default=4)

    def __str__(self):
        return f"{self.brand} {self.model_name}"

    # For the graph structure: fetch related laptops by brand or type
    def get_related_laptops(self):
        return Laptop.objects.filter(brand=self.brand, laptop_type=self.laptop_type).exclude(id=self.id)



@receiver(post_save, sender=Laptop)
@receiver(post_delete, sender=Laptop)
def rebuild_avl_tree(sender, instance, **kwargs):

    from .views import update_tree_cache
    update_tree_cache()