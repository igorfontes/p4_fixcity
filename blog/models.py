from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # CHANGE
    image = models.ImageField(default='post_default.jpg', upload_to='post_pics')

    UNSOLVED = 1
    ONGOING = 2
    SOLVED = 3
    STATUS = (
        (UNSOLVED, ('Unsolved problem')),
        (ONGOING, ('Solution is ongoing')),
        (SOLVED, ('Solved problem')),
    )
    
    # CHANGE
    # remember that you have to execute the following commands to add a new attribute at the database:
    # python manage.py makemigrations
    # python manage.py migrate

    status = models.PositiveSmallIntegerField(
        choices=STATUS,
        default=UNSOLVED,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    
