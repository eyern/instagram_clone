from django.test import TestCase
import datetime as dt
from .models import Image, Profile
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.image = Image(image ='imageurl', image_name='culture', image_caption='designer', likes=150, comments='awesome')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_delete_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)


class ProfileTestClas(TestCase):

    def setUp(self):
        user = User(username='e.y.e.r.n')
        self.profile = Profile(profile_photo='bad things happen to good people', user_bio='Jah know His people', last_update='date', user=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)
