from django.urls import path, re_path
from .import views

# added for sitemap
from django.contrib.sitemaps.views import sitemap
from .sitemap import PaperSitemap, StaticSitemap

sitemaps = {
    'abstract': PaperSitemap,
    'static': StaticSitemap
}



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('policy/', views.policy, name='policy'),
    path('add_abstract/', views.add_abstract, name = 'add_abstract'),
    path('abstract_list/', views.abstract_list, name = 'abstract_list'),
    path('abstract_detail/<slug:slug>/', views.abstract_detail, name = 'abstract_detail'),
    path('register_profile/', views.register_profile, name = 'register_profile'),
    re_path(r'profile/(?P<username>[\w\-]+)/', views.profile, name='profile'),
    path('add_review/<slug:slug>/review/', views.add_review, name = 'add_review'),
    path('tag_department/', views.tag_department, name = 'tag_department'),
    path('tag_department/<int:pk>/remove/', views.remove_tag, name = 'remove_tag'),
    path('send_msg/<int:pk>/', views.send_msg, name = 'send_msg'),
    path('remove_msg/<int:pk>/remove/', views.remove_msg, name = 'remove_msg'),
    path('liked_review/<int:pk>', views.liked_review, name = 'liked_review'),
    path('search/', views.search, name = 'search'),
    path('remove_review/<int:pk>/remove/', views.remove_review, name = 'remove_review'),
    path('update_profile/', views.update_profile, name = 'update_profile'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'), # for sitemap

    


    # Agriculture
    path('agriculture_all/', views.agriculture_all, name = 'agriculture_all'),
    path('agricultural_administration/', views.agricultural_administration, name = 'agricultural_administration'),
    path('agricultural_administration/', views.agricultural_administration, name = 'agricultural_administration'),
    path('agricultural_business_finance/', views.agricultural_business_finance, name = 'agricultural_business_finance'),
    path('agricultural_economics/', views.agricultural_economics, name = 'agricultural_economics'),
    path('agricultural_extension/', views.agricultural_extension, name = 'agricultural_extension'),
    path('agronomy/', views.agronomy, name = 'agronomy'),
    path('animal_science/', views.animal_science, name = 'animal_science'),
    path('crop_science/', views.crop_science, name = 'crop_science'),
    path('fisheries/', views.fisheries, name = 'fisheries'),
    path('forestry/', views.forestry, name = 'forestry'),
    path('soil_science/', views.soil_science, name = 'soil_science'),
    path('agriculture_topics/', views.agriculture_topics, name = 'agriculture_topics'),

    # Arts/Humanities
    path('arts_all/', views.arts_all, name = 'arts_all'),
    path('anthropology/', views.anthropology, name = 'anthropology'),
    path('arabic_islamic_studies/', views.arabic_islamic_studies, name = 'arabic_islamic_studies'),
    path('christian_studies/', views.christian_studies, name = 'christian_studies'),
    path('communication_arts/', views.communication_arts, name = 'communication_arts'),
    path('creative_arts/', views.creative_arts, name = 'creative_arts'),
    path('english_literature/', views.english_literature, name = 'english_literature'),
    path('french/', views.french, name = 'french'),
    path('geography/', views.geography, name = 'geography'),
    path('hausa/', views.hausa, name = 'hausa'),
    path('history_international_studies_diplomacy/', views.history_international_studies_diplomacy, name = 'history_international_studies_diplomacy'),
    path('igbo/', views.igbo, name = 'igbo'),
    path('language_linguistics/', views.language_linguistics, name = 'language_linguistics'),
    path('philosophy/', views.philosophy, name = 'philosophy'),
    path('political_science/', views.political_science, name = 'political_science'),
    path('psychology/', views.psychology, name = 'psychology'),
    path('religious_studies/', views.religious_studies, name = 'religious_studies'),
    path('sociology/', views.sociology, name = 'sociology'),
    path('yoruba/', views.yoruba, name = 'yoruba'),
    path('arts_humanities/', views.arts_humanities, name = 'arts_humanities'),


    # Education
    path('education_all/', views.education_all, name = 'education_all'),
    path('adult_nonformal_education/', views.adult_nonformal_education, name = 'adult_nonformal_education'),
    path('curriculum_studies/', views.curriculum_studies, name = 'curriculum_studies'),
    path('educational_administration_management/', views.educational_administration_management, name = 'educational_administration_management'),
    path('guidance_counselling/', views.guidance_counselling, name = 'guidance_counselling'),
    path('library_studies/', views.library_studies, name = 'library_studies'),
    path('nursery_primary_education/', views.nursery_primary_education, name = 'nursery_primary_education'),
    path('physical_health_education/', views.physical_health_education, name = 'physical_health_education'),
    path('special_education/', views.special_education, name = 'special_education'),
    path('teacher_education/', views.teacher_education, name = 'teacher_education'),
    path('education_other/', views.education_other, name = 'education_other'),

    # Engineering/Environmental/Technology
    path('engineering_all/', views.engineering_all, name = 'engineering_all'),
    path('agricultural_engineering/', views.agricultural_engineering, name = 'agricultural_engineering'),
    path('architecture/', views.architecture, name = 'architecture'),
    path('biomedical/', views.biomedical, name = 'biomedical'),
    path('chemical_petroleum_gas/', views.chemical_petroleum_gas, name = 'chemical_petroleum_gas'),
    path('civil/', views.civil, name = 'civil'),
    path('computer/', views.computer, name = 'computer'),
    path('electrical_electronics/', views.electrical_electronics, name = 'electrical_electronics'),
    path('estate_management/', views.estate_management, name = 'estate_management'),
    path('food_engineering_technology/', views.food_engineering_technology, name = 'food_engineering_technology'),
    path('land_quantity_surveying/', views.land_quantity_surveying, name = 'land_quantity_surveying'),
    path('marine/', views.marine, name = 'marine'),
    path('mechanical_production/', views.mechanical_production, name = 'mechanical_production'),
    path('metallurgical_materials/', views.metallurgical_materials, name = 'metallurgical_materials'),
    path('polymer_textile/', views.polymer_textile, name = 'polymer_textile'),
    path('software/', views.software, name = 'software'),
    path('urban_regional_planning/', views.urban_regional_planning, name = 'urban_regional_planning'),
    path('water_resources_environmental/', views.water_resources_environmental, name = 'water_resources_environmental'),
    path('engineering_environmental_technology/', views.engineering_environmental_technology, name = 'engineering_environmental_technology'),
    

    # Law
    path('law_all/', views.law_all, name = 'law_all'),
    path('civil_law/', views.civil_law, name = 'civil_law'),
    path('common_law/', views.common_law, name = 'common_law'),
    path('international_law_jurisprudence/', views.international_law_jurisprudence, name = 'international_law_jurisprudence'),
    path('islamic_sharia_law/', views.islamic_sharia_law, name = 'islamic_sharia_law'),
    path('public_law/', views.public_law, name = 'public_law'),
    path('law_others/', views.law_others, name = 'law_others'),


    #  Medical
    path('medical_all/', views.medical_all, name = 'medical_all'),
    path('basic_medical/', views.basic_medical, name = 'basic_medical'),
    path('dentistry_dental_technology/', views.dentistry_dental_technology, name = 'dentistry_dental_technology'),
    path('human_medicine/', views.human_medicine, name = 'human_medicine'),
    path('human_nutrition_dietetics/', views.human_nutrition_dietetics, name = 'human_nutrition_dietetics'),
    path('medical_laboratory_science_technology/', views.medical_laboratory_science_technology, name = 'medical_laboratory_science_technology'),
    path('nursing/', views.nursing, name = 'nursing'),
    path('optometry/', views.optometry, name = 'optometry'),
    path('pharmacy_pharmacology/', views.pharmacy_pharmacology, name = 'pharmacy_pharmacology'),
    path('physiotherapy/', views.physiotherapy, name = 'physiotherapy'),
    path('public_health/', views.public_health, name = 'public_health'),
    path('radiography/', views.radiography, name = 'radiography'),
    path('veterinary_medicine/', views.veterinary_medicine, name = 'veterinary_medicine'),
    path('medical_others/', views.medical_others, name = 'medical_others'),


    # Science 
    path('science_all/', views.science_all, name = 'science_all'),   
    path('animal_environmental_biology_zoology/', views.animal_environmental_biology_zoology, name = 'animal_environmental_biology_zoology'),
    path('biochemistry/', views.biochemistry, name = 'biochemistry'),
    path('biotechnology_genetics/', views.biotechnology_genetics, name = 'biotechnology_genetics'),
    path('botany/', views.botany, name = 'botany'),
    path('chemistry/', views.chemistry, name = 'chemistry'),
    path('computer_science/', views.computer_science, name = 'computer_science'),
    path('geology/', views.geology, name = 'geology'),
    path('mathematics_statistics/', views.mathematics_statistics, name = 'mathematics_statistics'),
    path('microbiology/', views.microbiology, name = 'microbiology'),
    path('physics/', views.physics, name = 'physics'),
    path('science_others/', views.science_others, name = 'science_others'),


    # Social/Management
    path('management_all/', views.management_all, name = 'management_all'),
    path('accounting/', views.accounting, name = 'accounting'),
    path('banking_finance/', views.banking_finance, name = 'banking_finance'),
    path('business_administration/', views.business_administration, name = 'business_administration'),
    path('economics/', views.economics, name = 'economics'),
    path('entrepreneurship/', views.entrepreneurship, name = 'entrepreneurship'),
    path('insurance_actuarial_science/', views.insurance_actuarial_science, name = 'insurance_actuarial_science'),
    path('marketing/', views.marketing, name = 'marketing'),
    path('project_personnel_management/', views.project_personnel_management, name = 'project_personnel_management'),
    path('public_administration_relation/', views.public_administration_relation, name = 'public_administration_relation'),
    path('taxation/', views.taxation, name = 'taxation'),
    path('social_management_others/', views.social_management_others, name = 'social_management_others'),

   
]


