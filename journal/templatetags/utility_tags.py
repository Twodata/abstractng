# -*- coding: utf-8 -*-

from django import template
from journal.models import Paper, AuthorProfile
from django.db.models import Q, Count



from django.utils.safestring import mark_safe

register = template.Library()





@register.inclusion_tag('journal/utility_tags.html')
def get_most_viewed():
     most_viewed = Paper.objects.all().filter(views__gte = 5).order_by('-views')[:10]
     return {'abstract_viewed': most_viewed}


@register.inclusion_tag('journal/utility_tags.html')
def get_most_recent():
     most_recent = Paper.objects.all().order_by('-pk')[:10]
     return {'abstract_recent': most_recent}



@register.inclusion_tag('journal/utility_tags.html')
def get_most_reviewed():
     most_reviewed = Paper.objects.annotate(num_review = Count('review')).filter(num_review__gte = 2).order_by('-num_review')[:10]
     return {'abstract_reviewed': most_reviewed}


@register.inclusion_tag('journal/utility_tags.html')
def get_most_viewed_author():
     most_viewed = AuthorProfile.objects.all().order_by('-views')[:10]
     return {'author_viewed': most_viewed}


@register.inclusion_tag('journal/utility_tags.html')
def get_search_form():
	return {'search_form': 'search_form'}



# Agriculture
@register.inclusion_tag('journal/utility_tags.html')
def related_agriculture():
	abstracts = Paper.objects.annotate(num_review = Count('review')).filter(Q(department = 'Agricultural Administration'
		)|Q(department = 'Agricultural Business/Finance'
		)|Q(department = 'Agricultural Economics'
		)|Q(department = 'Agricultural Extension'
		)|Q(department = 'Agronomy'
		)|Q(department = 'Animal Science'
		)|Q(department = 'Crop Science'
		)|Q(department = 'Fisheries'
		)|Q(department = 'Forestry'
		)|Q(department = 'Soil Science'
		)|Q(department = 'Agriculture(Other topics)')).order_by('-pk')[:20]
	return {'related_agriculture': abstracts}


# Arts/Humanities
@register.inclusion_tag('journal/utility_tags.html')
def related_arts():
	abstracts = Paper.objects.annotate(num_review = Count('review')).filter(Q(department = 'Anthropology'
		)|Q(department = 'Arabic/Islamic Studies'
		)|Q(department = 'Christian Studies'
		)|Q(department = 'Communication Arts(Mass Communication etc)'
		)|Q(department = 'Creative Arts(Fine Arts/Dramatic Arts/Music etc)'
		)|Q(department = 'English Language and Literature'
		)|Q(department = 'French'
		)|Q(department = 'Geography'
		)|Q(department = 'Hausa'
		)|Q(department = 'History/International Studies/Diplomacy'
		)|Q(department = 'Igbo'
		)|Q(department = 'Language/Linguistics'
		)|Q(department = 'Philosophy'
		)|Q(department = 'Political Science'
		)|Q(department = 'Psychology'
		)|Q(department = 'Religious Studies'
		)|Q(department = 'Sociology'
		)|Q(department = 'Yoruba'
		)|Q(department = 'Arts/Humanities(Other topics)')).order_by('-pk')[:20]
	return {'related_arts': abstracts}


# Education
@register.inclusion_tag('journal/utility_tags.html')
def related_education():
	abstracts = Paper.objects.annotate(num_review = Count('review')).filter(Q(department = 'Adult/Non-Formal Education'
		)|Q(department = 'Curriculum Studies'
		)|Q(department = 'Educational Administration/Management'
		)|Q(department = 'Guidance and Counselling'
		)|Q(department = 'Library Studies'
		)|Q(department = 'Nursery/Primary Education'
		)|Q(department = 'Physical and Health Education'
		)|Q(department = 'Special Education'
		)|Q(department = 'Teacher Education'
		)|Q(department = 'Education(Other topics)'
		)).order_by('-pk')[:20]
	return {'related_education': abstracts}


# Engineering
@register.inclusion_tag('journal/utility_tags.html')
def related_engineering():
	abstracts = Paper.objects.annotate(num_review = Count('review')).filter(Q(department = 'Agricultural Engineering'
		)|Q(department = 'Architecture'
		)|Q(department = 'Biomedical'
		)|Q(department = 'Chemical/Petroleum/Gas'
		)|Q(department = 'Civil'
		)|Q(department = 'Computer'
		)|Q(department = 'Electrical/Electronics'
		)|Q(department = 'Estate Management'
		)|Q(department = 'Food Engineering/Technology'
		)|Q(department = 'Land/Quantity Surveying'
		)|Q(department = 'Marine'
		)|Q(department = 'Mechanical/Production'
		)|Q(department = 'Metallurgical and Materials'
		)|Q(department = 'Polymer and Textile'
		)|Q(department = 'Software'
		)|Q(department = 'Urban and Regional Planning'
		)|Q(department = 'Water Resources/Environmental'
		)|Q(department = 'Engineering/Environmental/Technology(Other topics)')).order_by('-pk')[:20]
	return {'related_engineering': abstracts}





# Law
@register.inclusion_tag('journal/utility_tags.html')
def related_law():
	abstracts = Paper.objects.annotate(num_review = Count('review')).filter(Q(department = 'Civil Law'
		)|Q(department = 'Common Law'
		)|Q(department = 'International Law and Jurisprudence'
		)|Q(department = 'Islamic/Sharia Law'
		)|Q(department = 'Public Law'
		)|Q(department = 'Law(Other topics)')).order_by('-pk')[:20]
	return {'related_law': abstracts}




# Medical
@register.inclusion_tag('journal/utility_tags.html')
def related_medical():
	abstracts = Paper.objects.annotate(num_review = Count('review')).filter(Q(department = 'Basic Medical Sciences'
		)|Q(department = 'Dentistry/Dental Technology'
		)|Q(department = 'Human Medicine'
		)|Q(department = 'Human Nutrition/Dietetics'
		)|Q(department = 'Medical Laboratory Science/Technology'
		)|Q(department = 'Nursing'
		)|Q(department = 'Optometry'
		)|Q(department = 'Pharmacy/Pharmacology'
		)|Q(department = 'Physiotherapy'
		)|Q(department = 'Public Health'
		)|Q(department = 'Radiography'
		)|Q(department = 'Veterinary Medicine'
		)|Q(department = 'Medical(Other topics)')).order_by('-pk')[:20]
	return {'related_medical': abstracts}




# Science
@register.inclusion_tag('journal/utility_tags.html')
def related_science():
	abstracts = Paper.objects.annotate(num_review = Count('review')).filter(Q(department = 'Animal and Environmental Biology/Zoology'
		)|Q(department = 'Biochemistry'
		)|Q(department = 'Biotechnology/Genetics'
		)|Q(department = 'Botany'
		)|Q(department = 'Chemistry'
		)|Q(department = 'Computer Science'
		)|Q(department = 'Geology'
		)|Q(department = 'Mathematics/Statistics'
		)|Q(department = 'Microbiology'
		)|Q(department = 'Physics'
		)|Q(department = 'Science(Other topics)')).order_by('-pk')[:20]
	return {'related_science': abstracts}




# Management
@register.inclusion_tag('journal/utility_tags.html')
def related_management():
	abstracts = Paper.objects.annotate(num_review = Count('review')).filter(Q(department = 'Accounting'
		)|Q(department = 'Banking and Finance'
		)|Q(department = 'Business Administration'
		)|Q(department = 'Economics'
		)|Q(department = 'Entrepreneurship'
		)|Q(department = 'Insurance/Actuarial Science'
		)|Q(department = 'Marketing'
		)|Q(department = 'Project/Personnel Management'
		)|Q(department = 'Public Administration/Relation'
		)|Q(department = 'Taxation'
		)|Q(department = 'Social/Management(Other topics)')).order_by('-pk')[:20]
	return {'related_management': abstracts}