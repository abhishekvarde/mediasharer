from django.db import models


# Create your models here.

class uploads(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='my_images')

    def __str__(self):
        return self.name


'''
echo "# mediasharer" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/abhishekvarde/mediasharer.git
git push -u origin main
                
'''