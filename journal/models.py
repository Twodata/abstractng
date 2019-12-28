from django.db import models
from ckeditor.fields import RichTextField


from django.utils.text import slugify

from django.contrib.auth.models import User



department_list = (
			('', 'Choose department'),
			('Agriculture', (
				('Agricultural Administration', 'Agricultural Administration'),
				('Agricultural Business/Finance', 'Agricultural Business/Finance'),
				('Agricultural Economics', 'Agricultural Economics'),
				('Agricultural Extension', 'Agricultural Extension'),
				('Agronomy', 'Agronomy'),
				('Animal Science', 'Animal Science'),
				('Crop Science', 'Crop Science'),
				('Fisheries', 'Fisheries'),
				('Forestry', 'Forestry'),
				('Soil Science', 'Soil Science'),
				('Agriculture(Other topics)', 'Agriculture(Other topics)'),
			) ),

			('Arts/Humanities', (
				('Anthropology', 'Anthropology'),
				('Arabic/Islamic Studies', 'Arabic/Islamic Studies'),
				('Christian Studies', 'Christian Studies'),
				('Communication Arts(Mass Communication etc)', 'Communication Arts(Mass Communication etc)'),
				('Creative Arts(Fine Arts/Dramatic Arts/Music etc)', 'Creative Arts(Fine Arts/Dramatic Arts/Music etc)'),
				('English Language and Literature', 'English Language and Literature'),
				('French', 'French'),
				('Geography', 'Geography'),
				('Hausa', 'Hausa'),
				('History/International Studies/Diplomacy', 'History/International Studies/Diplomacy'),
				('Igbo', 'Igbo'),
				('Language/Linguistics', 'Language/Linguistics'),
				('Philosophy', 'Philosophy'),
				('Political Science', 'Political Science'),
				('Psychology', 'Psychology'),
				('Religious Studies', 'Religious Studies'),
				('Sociology', 'Sociology'),
				('Yoruba', 'Yoruba'),
				('Arts/Humanities(Other topics)', 'Arts/Humanities(Other topics)'),
			) ),

		('Education', (
				('Adult/Non-Formal Education', 'Adult/Non-Formal Education'),
				('Curriculum Studies', 'Curriculum Studies'),
				('Educational Administration/Management', 'Educational Administration/Management'),
				('Guidance and Counselling', 'Guidance and Counselling'),
				('Library Studies', 'Library Studies'),
				('Nursery/Primary Education', 'Nursery/Primary Education'),
				('Physical and Health Education', 'Physical and Health Education'),
				('Special Education', 'Special Education'),
				('Teacher Education', 'Teacher Education'),
				('Education(Other topics)', 'Education(Other topics)'),
			) ),

		('Engineering/Environmental/Technology', (
				('Agricultural Engineering', 'Agricultural Engineering'),
				('Architecture', 'Architecture'),
				('Biomedical', 'Biomedical'),
				('Chemical/Petroleum/Gas', 'Chemical/Petroleum/Gas'),
				('Civil', 'Civil'),
				('Computer', 'Computer'),
				('Electrical/Electronics', 'Electrical/Electronics'),
				('Estate Management', 'Estate Management'),
				('Food Engineering/Technology', 'Food Engineering/Technology'),
				('Land/Quantity Surveying', 'Land/Quantity Surveying'),
				('Marine', 'Marine'),
				('Mechanical/Production', 'Mechanical/Production'),
				('Metallurgical and Materials', 'Metallurgical and Materials'),
				('Polymer and Textile', 'Polymer and Textile'),
				('Software', 'Software'),
				('Urban and Regional Planning', 'Urban and Regional Planning'),
				('Water Resources/Environmental', 'Water Resources/Environmental'),
				('Engineering/Environmental/Technology(Other topics)', 'Engineering/Environmental/Technology(Other topics)'),
			) ),

		('Law', (
				('Civil Law', 'Civil Law'),
				('Common Law', 'Common Law'),
				('International Law and Jurisprudence', 'International Law and Jurisprudence'),
				('Islamic/Sharia Law', 'Islamic/Sharia Law'),
				('Public Law', 'Public Law'),
				('Law(Other topics)', 'Law(Other topics)'),
			) ),

		('Medical', (
				('Basic Medical Sciences', 'Basic Medical Sciences'),
				('Dentistry/Dental Technology', 'Dentistry/Dental Technology'),
				('Human Medicine', 'Human Medicine'),
				('Human Nutrition/Dietetics', 'Human Nutrition/Dietetics'),
				('Medical Laboratory Science/Technology', 'Medical Laboratory Science/Technology'),
				('Nursing', 'Nursing'),
				('Optometry', 'Optometry'),
				('Pharmacy/Pharmacology', 'Pharmacy/Pharmacology'),
				('Physiotherapy', 'Physiotherapy'),
				('Public Health', 'Public Health'),
				('Radiography', 'Radiography'),
				('Veterinary Medicine', 'Veterinary Medicine'),
				('Medical(Other topics)', 'Medical(Other topics)'),
			) ),

		('Science', (
				('Animal and Environmental Biology/Zoology', 'Animal and Environmental Biology/Zoology'),
				('Biochemistry', 'Biochemistry'),
				('Biotechnology/Genetics', 'Biotechnology/Genetics'),
				('Botany', 'Botany'),
				('Chemistry', 'Chemistry'),
				('Computer Science', 'Computer Science'),
				('Geology', 'Geology'),
				('Mathematics/Statistics', 'Mathematics/Statistics'),
				('Microbiology', 'Microbiology'),
				('Physics', 'Physics'),
				('Science(Other topics)', 'Science(Other topics)'),
			) ),

		('Social/Management', (
				('Accounting', 'Accounting'),
				('Banking and Finance', 'Banking and Finance'),
				('Business Administration', 'Business Administration'),
				('Economics', 'Economics'),
				('Entrepreneurship', 'Entrepreneurship'),
				('Insurance/Actuarial Science', 'Insurance/Actuarial Science'),
				('Marketing', 'Marketing'),
				('Project/Personnel Management', 'Project/Personnel Management'),
				('Public Administration/Relation', 'Public Administration/Relation'),
				('Taxation', 'Taxation'),
				('Social/Management(Other topics)', 'Social/Management(Other topics)'),
			) ),
)



title_list = (

            ('Prof', 'Prof'),
            ('Dr', 'Dr'),
            ('Mr', 'Mr'),
            ('Mrs', 'Mrs'),
            ('Ms', 'Ms'),

            )


''' Code snippet for generating unique slugfield. This code is can be placed in utils.py file
of Marketplace app and imported into models.py for use.'''

def generate_unique_slug(klass, field):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`

    :param `klass` is Class model.
    :param `field` is specific field for title.
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug




class AuthorProfile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	title = models.CharField(max_length = 20, choices = title_list)
	firstname = models.CharField(max_length = 50)
	lastname = models.CharField(max_length = 50)
	organisation = models.CharField(max_length = 100, null = True, blank = True)
	email = models.EmailField(max_length = 200, null = True, blank = True)
	website = models.URLField(null = True, blank = True)
	location = models.CharField(max_length = 100, null = True, blank = True)
	research_interest = models.CharField(max_length = 500, null = True, blank = True)
	awards = models.CharField(max_length = 500, null = True, blank = True)
	hobbies = models.CharField(max_length = 200, null = True, blank = True)
	photo = models.ImageField(upload_to = 'photo', default = 'photo', null = True, blank = True)
	views = models.IntegerField(default = 0)
	
	 

	def get_author(self):
		return self.title + ' ' + self.lastname + ' ' + self.firstname


	
	def __str__(self):
		return self.title + ' ' + self.lastname + ' ' + self.firstname 




class Paper(models.Model):
	author = models.CharField(max_length = 150)
	co_authors = models.CharField(max_length = 500, null = True, blank = True)
	department = models.CharField(max_length = 60, choices = department_list)
	topic =  models.CharField(max_length = 300, unique = True)
	publication = models.CharField(max_length = 250, null = True, blank = True)
	content = RichTextField()
	image1 = models.ImageField(upload_to = 'image', default = 'image', null = True, blank = True)
	image2 = models.ImageField(upload_to = 'image', default = 'image', null = True, blank = True)
	image3 = models.ImageField(upload_to = 'image', default = 'image', null = True, blank = True)
	date_added = models.DateField(auto_now_add = True)
	views = models.IntegerField(default = 0)
	added_by = models.CharField(max_length = 50)
	slug = models.SlugField(max_length=300, unique=True)
	index_paper = models.BooleanField(default = False)


	def save(self, *args, **kwargs):
		if self.slug:
			if slugify(self.topic) != self.slug:
				self.slug = generate_unique_slug(Paper, self.topic)
		else:
			self.slug = generate_unique_slug(Paper, self.topic)
		super(Paper, self).save(*args, **kwargs)     




	def __str__(self):

		return self.topic + ' by ' + self.added_by



class Review(models.Model):
	paper_reviewed = models.ForeignKey(Paper, on_delete = models.CASCADE)
	text = RichTextField(config_name='review_toolbar')
	likes = models.IntegerField(default = 0)
	date_added = models.DateField(auto_now_add = True)
	added_by = models.CharField(max_length = 50)
	review_author = models.CharField(max_length = 150, default = 'review_author')



class Department(models.Model):
	department = models.CharField(max_length = 60, choices = department_list)
	added_by = models.CharField(max_length = 50)

	def __str__(self):
		return self.department + ' tagged by ' + self.added_by


class MyMessage(models.Model):
	to = models.ForeignKey(AuthorProfile, on_delete = models.CASCADE)
	body = models.TextField()
	sender = models.CharField(max_length = 150)
	date_added = models.DateTimeField(auto_now_add = True)
	added_by = added_by = models.CharField(max_length = 50, default = 'name')
		
	def __str__(self):

		return 'From ' + self.sender

class Liked(models.Model):
    added_by = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    class Meta:
        unique_together = ('added_by', 'review')

    def __str__(self):
        return str(self.added_by)

		

