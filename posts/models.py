from django.db import models
from users.models import User
# Create your models here.




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='image/',null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Tag(models.Model):
    tag_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tag_name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='image/',null=True, blank=True)
    def __str__(self):
        return self.title
