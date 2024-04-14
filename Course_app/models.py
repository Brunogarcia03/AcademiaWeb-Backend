from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    PRINCIPIANTE = 'Principiante'
    INTERMEDIO = 'Intermedio'
    AVANZADO = 'Avanzado'
    
    DIFICULTY_CHOICES = [
        (PRINCIPIANTE, 'Principiante'),
        (INTERMEDIO, 'Intermedio'),
        (AVANZADO, 'Avanzado'),
    ]

    def save(self, *args, **kwargs):
        # Generar el slug a partir del título
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    difficulty = models.CharField(max_length=20, choices=DIFICULTY_CHOICES, default=PRINCIPIANTE)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image_file = models.FileField(upload_to='video_images/', null=True)
    video_file = models.FileField(upload_to='video_files/')
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title