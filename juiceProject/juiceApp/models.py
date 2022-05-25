from django.db import models

# Create your models here.
class home (models.Model):	
	album_img = models.ImageField(null=True, blank=True, upload_to ='images/')
	playing_song_image = models.ImageField(null=True, blank=True, upload_to="images/")
	main_hit = models.FileField(null=True, blank=True, upload_to='songs/')
	song_name = models.CharField(max_length=20, null=True)
	song_name2 = models.CharField(max_length=20, null=True)
	song_name3 = models.CharField(max_length=20, null=True)
	song_name4 = models.CharField(max_length=20, null=True)
	song_name5 = models.CharField(max_length=20, null=True)
	song_name6 = models.CharField(max_length=20, null=True)
	song_name7  = models.CharField(max_length=20, null=True)
	song_image = models.ImageField(null=True, blank=True, upload_to="images/")
	songs = models.FileField( default='DEFAULT VALUE', upload_to='songs/')
	songs2 = models.FileField( default='DEFAULT VALUE', upload_to='songs/')
	songs3 = models.FileField( default='DEFAULT VALUE',upload_to='songs/')
	songs4 = models.FileField( default='DEFAULT VALUE',upload_to='songs/')
	songs5 = models.FileField( default='DEFAULT VALUE',upload_to='songs/')
	songs6 = models.FileField( default='DEFAULT VALUE',upload_to='songs/')
	songs7 = models.FileField( default='DEFAULT VALUE',upload_to='songs/')

def __str__(self):
    return self.name 