from django.test import TestCase
from .models import Image,Category,Location


# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.new_category = Category(name='Nature')
        self.new_category.save_category()
        self.new_location = Location(name ='Motherland')
        self.new_location.save_location()
        self.new_image = Image(image_name='Sunsets in the forest', description='View of a sunset in the forest',category=self.new_category,image_location=self.new_location)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()


    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(image_name='Sunsets in the forest')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_display_all_objects_method(self):
        self.new_image.save_image()
        all_objects = Image.retrieve_all()
        self.assertEqual(all_objects.get(id=1).image_name,'Sunsets in the forest')
        
    def test_update_single_object_property(self):
        self.new_image.save_image()

    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)
   

    def test_filter_by_location(self):
        self.new_image.save_image()
        fetch_specific = Image.filter_location('Motherland')
        self.assertEqual(fetch_specific.get(id=1),self.new_image)