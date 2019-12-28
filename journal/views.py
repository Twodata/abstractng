from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.core.mail import EmailMessage
from django.template.loader import get_template

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db.models import Count, Q

from .models import AuthorProfile, Paper, Department, Review, MyMessage, Liked
from journal.forms import AuthorProfileForm, PaperForm, DepartmentForm, ReviewForm, MyMessageForm, ContactForm


def index(request):
	abstracts = Paper.objects.all()
	index_abstract = Paper.objects.filter(index_paper = True).order_by('-pk')[:20]
	return render(request, 'journal/index.html', {'abstracts':abstracts, 'index_abstract': index_abstract})


def about(request):
	return render(request, 'journal/about.html')


def policy(request):
	return render(request, 'journal/policy.html')


def contact(request):
	form_class = ContactForm
	if request.method == 'POST':
		form = form_class(data = request.POST)
		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

			# email the profile with contact information
			template = get_template('journal/contact_template.txt')
			context = {'contact_name':contact_name, 'contact_email': contact_email, 'form_content':form_content}
			content = template.render(context)

			email = EmailMessage(
				'New contact form submission',
				content,
				'abstract.ng' + '',
				['osabohienchukwuma@gmail.com'],
				headers = {'Reply-To': contact_email})
			email.send()
			messages.success(request, 'Message to Abstractng delivered successfully!')
	return render(request, 'journal/contact.html', {'form':form_class})


@login_required            
def add_abstract(request):
	author_user = User.objects.get(username = request.user)
	author_profile = AuthorProfile.objects.get(user = author_user)
	if request.method == 'POST' and author_profile.title and author_profile.firstname and author_profile.lastname:
		form = PaperForm(request.POST, request.FILES)
		if form.is_valid():
			abstract = form.save(commit = False)
			abstract.author = author_profile.get_author()
			abstract.added_by = request.user
			abstract.save()
			return redirect('abstract_list')
	else:
		form = PaperForm()
	return render(request, 'journal/add_abstract.html', {'form' : form})



@login_required          
def register_profile(request):
	form = AuthorProfileForm()

	if request.method == 'POST':
		form = AuthorProfileForm(request.POST, request.FILES)
		if form.is_valid():
			author_profile = form.save(commit=False)
			author_profile.user = request.user
			author_profile.save()
			return redirect('index')
		else:
			print(form.errors)

	context_dict = {'form' : form}

	return render(request, 'journal/profile_registration.html', context_dict)

@login_required   
def profile(request, username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		return redirect('index')

	authorprofile = AuthorProfile.objects.get_or_create(user=user)[0]
	form = AuthorProfileForm()

	if request.method == 'POST':
		form = AuthorProfileForm(request.POST, request.FILES, instance=authorprofile)
		if form.is_valid():
			form.save(commit=True)
			return redirect('profile', user.username)
		else:
			print(form.errors)

	public_abstract = Paper.objects.filter(added_by = username).order_by('-pk')
	public_review = Review.objects.filter(added_by = username).order_by('-pk')

	tag_form = DepartmentForm()
	tag_department = Department.objects.filter(added_by = username)

	msg_form = MyMessageForm()
	msg = MyMessage.objects.filter(to = authorprofile).order_by('-pk')

	tag_abstract_list = []
	tag_depart = Department.objects.filter(added_by = username)
	if tag_depart:
		for item in tag_depart:
			tag_abstract = Paper.objects.filter(department = item.department)
			tag_abstract_list.extend(tag_abstract)


	if request.user != authorprofile.user:
		authorprofile.views += 1
		authorprofile.save()
	

	return render(request, 'journal/profile.html', 
    	{'authorprofile': authorprofile, 'selecteduser': user, 'form': form, 
    	'public_abstract':public_abstract, 'tag_form': tag_form, 'tag_department': tag_department,
    	'msg_form':msg_form, 'msg':msg, 'public_review':public_review, 'tag_abstract_list':tag_abstract_list})
    

def update_profile(request):
	userprofile = AuthorProfile.objects.get(user = request.user)
	form = AuthorProfileForm(instance = userprofile)
	if request.method == 'POST':
		form = AuthorProfileForm(request.POST, request.FILES, instance = userprofile)
		if form.is_valid():
			form.save(commit = True)
			return redirect('profile', request.user.username)
		else:
			print(form.errors)
	else:
		return render(request, 'journal/profile_registration.html', {'form': form, 'update': 'update'})
    
def abstract_list(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).order_by('-pk')
	return render(request, 'journal/abstract_list.html', {'abstract':abstract})



def abstract_detail(request, slug):
	form = ReviewForm()
	abstract = get_object_or_404(Paper, slug=slug)
	reviews = Review.objects.all().filter(paper_reviewed = abstract).order_by('-pk')

	user = User.objects.get(username = abstract.added_by)
	authorprofile = AuthorProfile.objects.get(user = user)

	num_abstract = Paper.objects.filter(added_by = user.username)
	num_review = Review.objects.filter(added_by = user.username)

	related_abstracts = Paper.objects.all().exclude(topic = abstract.topic).filter(department = 
        abstract.department)[:10]
	abstract.views += 1
	abstract.save()
	context_dict = {'abstract' : abstract, 'reviews':reviews, 'form':form, 
	'related_abstracts':related_abstracts, 'authorprofile':authorprofile, 'num_abstract': num_abstract,
	'num_review':num_review}

	return render (request, 'journal/abstract_detail.html', context_dict)


@login_required    
def add_review(request, slug):
    paper = get_object_or_404(Paper, slug=slug)
    author = AuthorProfile.objects.get(user = request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit = False)
            review.paper_reviewed = paper
            review.added_by = request.user
            review.review_author = author            
            review.save()
            reviews = Review.objects.all() # added for ajax

            return redirect('abstract_detail', slug=slug)
    else:
        return redirect('abstract_detail', slug=paper.slug)


def tag_department(request):
	if request.method == 'POST':
		form = DepartmentForm(request.POST)
		if form.is_valid:
			department = request.POST.get('department')
			try:
				Department.objects.get(added_by = request.user, department = department)
			except:
				tagged_department = form.save(commit = False)
				tagged_department.added_by = request.user
				tagged_department.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_tag(request, pk):
	tag_department = get_object_or_404(Department, pk=pk)
	tag_department.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def send_msg(request, pk):
	sender = AuthorProfile.objects.get(user = request.user)
	to = AuthorProfile.objects.get(pk=pk)
	if request.method == 'POST':
		form = MyMessageForm(request.POST)
		if form.is_valid:
			msg = form.save(commit = False)
			msg.sender = sender.get_author()
			msg.to = to
			msg.added_by = request.user
			msg.save()
			messages.success(request, 'Your message has been delivered successfully!')
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_msg(request, pk):
	msg = MyMessage.objects.get(pk=pk)
	msg.delete()
	msg = MyMessage.objects.all()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def liked_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    try:
        Liked.objects.get(added_by = request.user, review = review)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Liked.DoesNotExist:
         pref = Liked()
         pref.added_by = request.user
         pref.review = review
         review.likes +=1
         review.save()         
         pref.save()
         reviews = Review.objects.all() # added for ajax
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        topic_list = Paper.objects.annotate(num_review = Count('review')).filter(topic__icontains=query).order_by('-pk')
        return render(request, 'journal/result.html', {'result' : topic_list, 'query':query})


def remove_review(request, pk):
	review = Review.objects.get(pk=pk)
	review.delete()
	reviews = Review.objects.all() # added for ajax
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





# Agriculture
def agriculture_all(request):
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
		)|Q(department = 'Agriculture(Other topics)')).order_by('-pk')
	return render(request, 'journal/abstract_list.html', {'agriculture':abstracts})

def agricultural_administration(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Agricultural Administration').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})


def agricultural_business_finance(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Agricultural Business/Finance').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})

def agricultural_economics(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Agricultural Economics').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})


def agricultural_extension(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Agricultural Extension').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})

def agronomy(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Agronomy').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})

def animal_science(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Animal Science').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})

def crop_science(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Crop Science').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})

def fisheries(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Fisheries').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})

def forestry(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Forestry').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})

def soil_science(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Soil Science').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})

def agriculture_topics(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Agriculture(Others)').order_by('-pk')
	return render(request, 'journal/agriculture.html', {'abstract':abstract})




# Arts/Humanities
def arts_all(request):
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
		)|Q(department = 'Arts/Humanities(Other topics)')).order_by('-pk')
	return render(request, 'journal/abstract_list.html', {'arts': abstracts})

def anthropology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Anthropology').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def arabic_islamic_studies(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Arabic/Islamic Studies').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def christian_studies(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Christian Studies').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def communication_arts(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Communication Arts(Mass Communication etc)').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def creative_arts(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Creative Arts(Fine Arts/Dramatic Arts/Music etc)').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def english_literature(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'English Language and Literature').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def french(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'French').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def geography(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Geography').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def hausa(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Hausa').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def history_international_studies_diplomacy(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'History/International Studies/Diplomacy').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def igbo(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Igbo').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def language_linguistics(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Language/Linguistics').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def philosophy(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Philosophy').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def political_science(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Political Science').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def psychology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Psychology').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def religious_studies(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Religious Studies').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def sociology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Sociology').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def yoruba(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Yoruba').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})

def arts_humanities(request):
	abstract = Paper.objects.filter(department = 'Arts/Humanities(Others)').order_by('-pk')
	return render(request, 'journal/arts_humanities.html', {'abstract':abstract})


# Education
def education_all(request):
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
		)).order_by('-pk')
	return render(request, 'journal/abstract_list.html', {'education': abstracts})

def adult_nonformal_education(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Adult/Non-Formal Education').order_by('-pk')
	return render(request, 'journal/education.html', {'abstract':abstract})

def curriculum_studies(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Curriculum Studies').order_by('-pk')
	return render(request, 'journal/education.html', {'abstract':abstract})

def educational_administration_management(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Educational Administration/Management').order_by('-pk')
	return render(request, 'journal/education.html', {'abstract':abstract})

def guidance_counselling(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Guidance and Counselling').order_by('-pk')
	return render(request, 'journal/education.html', {'abstract':abstract})

def library_studies(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Library Studies').order_by('-pk')
	return render(request, 'journal/education.html', {'abstract':abstract})

def nursery_primary_education(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Nursery/Primary Education').order_by('-pk')
	return render(request, 'journal/education.html', {'abstract':abstract})

def physical_health_education(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Physical and Health Education').order_by('-pk')
	return render(request, 'journal/education.html', {'abstract':abstract})

def special_education(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Special Education').order_by('-pk')
	return render(request, 'journal/education.html', {'abstract':abstract})

def teacher_education(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Teacher Education').order_by('-pk')
	return render(request, 'journal/education.html', {'abstract':abstract})

def education_other(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Education(Others)').order_by('-pk')
	return render(request, 'journal/education.html', {'abstract':abstract})


# Engineering/Environmental/Technology
def engineering_all(request):
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
		)|Q(department = 'Engineering/Environmental/Technology(Other topics)')).order_by('-pk')
	return render(request, 'journal/abstract_list.html', {'engineering':abstracts})

def agricultural_engineering(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Agricultural Engineering').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def architecture(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Architecture').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def biomedical(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Biomedical').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def chemical_petroleum_gas(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Chemical/Petroleum/Gas').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def civil(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Civil').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def computer(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Computer').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def electrical_electronics(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Electrical/Electronics').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def estate_management(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Estate Management').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def food_engineering_technology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Food Engineering/Technology').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def land_quantity_surveying(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Land/Quantity Surveying').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def marine(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Marine').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def mechanical_production(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Mechanical/Production').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def metallurgical_materials(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Metallurgical and Materials').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def polymer_textile(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Polymer and Textile').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def software(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Software').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def urban_regional_planning(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Urban and Regional Planning').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def water_resources_environmental(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Water Resources/Environmental').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})

def engineering_environmental_technology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Engineering/Environmental/Technology(Others)').order_by('-pk')
	return render(request, 'journal/engineering.html', {'abstract':abstract})



# Law
def law_all(request):
	abstracts = Paper.objects.annotate(num_review = Count('review')).filter(Q(department = 'Civil Law'
		)|Q(department = 'Common Law'
		)|Q(department = 'International Law and Jurisprudence'
		)|Q(department = 'Islamic/Sharia Law'
		)|Q(department = 'Public Law'
		)|Q(department = 'Law(Other topics)')).order_by('-pk')
	return render(request, 'journal/abstract_list.html', {'law':abstracts})

def civil_law(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Civil Law').order_by('-pk')
	return render(request, 'journal/law.html', {'abstract':abstract})

def common_law(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Common Law').order_by('-pk')
	return render(request, 'journal/law.html', {'abstract':abstract})

def international_law_jurisprudence(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'International Law and Jurisprudence').order_by('-pk')
	return render(request, 'journal/law.html', {'abstract':abstract})

def islamic_sharia_law(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Islamic/Sharia Law').order_by('-pk')
	return render(request, 'journal/law.html', {'abstract':abstract})

def public_law(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Public Law').order_by('-pk')
	return render(request, 'journal/law.html', {'abstract':abstract})

def law_others(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Law(Others)').order_by('-pk')
	return render(request, 'journal/law.html', {'abstract':abstract})



# Medical
def medical_all(request):
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
		)|Q(department = 'Medical(Other topics)')).order_by('-pk')
	return render(request, 'journal/abstract_list.html', {'medical':abstracts})


def basic_medical(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Basic Medical Sciences').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})

def dentistry_dental_technology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Dentistry/Dental Technology').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})

def human_medicine(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Human Medicine').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})

def human_nutrition_dietetics(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Human Nutrition/Dietetics').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})

def medical_laboratory_science_technology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Medical Laboratory Science/Technology').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})

def nursing(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Nursing').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})

def optometry(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Optometry').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})

def pharmacy_pharmacology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Pharmacy/Pharmacology').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})

def physiotherapy(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Physiotherapy').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})

def public_health(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Public Health').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})

def radiography(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Radiography').order_by('-pk')
	return render(request, 'journal/medical.html.html', {'abstract':abstract})

def veterinary_medicine(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Veterinary Medicine').order_by('-pk')
	return render(request, 'journal/abstract_list.html', {'abstract':abstract})

def medical_others(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Medical(Others)').order_by('-pk')
	return render(request, 'journal/medical.html', {'abstract':abstract})




# Science
def science_all(request):
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
		)|Q(department = 'Science(Other topics)')).order_by('-pk')
	return render(request, 'journal/abstract_list.html', {'science':abstracts})

def animal_environmental_biology_zoology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Animal and Environmental Biology/Zoology').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})

def biochemistry(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Biochemistry').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})

def biotechnology_genetics(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Biotechnology/Genetics').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})

def botany(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Botany').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})

def chemistry(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Chemistry').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})

def computer_science(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Computer Science').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})

def geology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Geology').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})

def mathematics_statistics(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Mathematics/Statistics').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})

def microbiology(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Microbiology').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})

def physics(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Physics').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})

def science_others(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Science(Others)').order_by('-pk')
	return render(request, 'journal/science.html', {'abstract':abstract})




# Social/Management
def management_all(request):
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
		)|Q(department = 'Social/Management(Other topics)')).order_by('-pk')
	return render(request, 'journal/abstract_list.html', {'management':abstracts})


def accounting(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Accounting').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})


def banking_finance(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Banking and Finance').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})


def business_administration(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Business Administration').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})


def economics(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Economics').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})


def entrepreneurship(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Entrepreneurship').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})


def insurance_actuarial_science(request):
	abstract = Paper.objects.filter(department = 'Insurance/Actuarial Science').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})


def marketing(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Marketing').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})


def project_personnel_management(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Project/Personnel Management').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})


def public_administration_relation(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Public Administration/Relation').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})


def taxation(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Taxation').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})


def social_management_others(request):
	abstract = Paper.objects.annotate(num_review = Count('review')).filter(department = 'Social/Management(Others)').order_by('-pk')
	return render(request, 'journal/management.html', {'abstract':abstract})



