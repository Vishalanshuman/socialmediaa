from django.db import models

# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='post')
    post_image = models.ImageField(upload_to='post_image', blank=True, null=True,)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-post_date']
    
    def __str__(self):
        return self.content[0:40]


