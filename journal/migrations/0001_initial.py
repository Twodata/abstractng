# Generated by Django 2.0.1 on 2019-02-11 12:58

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Prof', 'Prof'), ('Dr', 'Dr'), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], max_length=20)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('organisation', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('research_interest', models.CharField(blank=True, max_length=500, null=True)),
                ('awards', models.CharField(blank=True, max_length=500, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, default='photo', null=True, upload_to='photo')),
                ('views', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('', 'Choose department'), ('Agriculture', (('Agricultural Administration', 'Agricultural Administration'), ('Agricultural Business/Finance', 'Agricultural Business/Finance'), ('Agricultural Economics', 'Agricultural Economics'), ('Agricultural Extension', 'Agricultural Extension'), ('Agronomy', 'Agronomy'), ('Animal Science', 'Animal Science'), ('Crop Science', 'Crop Science'), ('Fisheries', 'Fisheries'), ('Forestry', 'Forestry'), ('Soil Science', 'Soil Science'), ('Agriculture(Other topics)', 'Agriculture(Other topics)'))), ('Arts/Humanities', (('Anthropology', 'Anthropology'), ('Arabic/Islamic Studies', 'Arabic/Islamic Studies'), ('Christian Studies', 'Christian Studies'), ('Communication Arts(Mass Communication etc)', 'Communication Arts(Mass Communication etc)'), ('Creative Arts(Fine Arts/Dramatic Arts/Music etc)', 'Creative Arts(Fine Arts/Dramatic Arts/Music etc)'), ('English Language and Literature', 'English Language and Literature'), ('French', 'French'), ('Geography', 'Geography'), ('Hausa', 'Hausa'), ('History/International Studies/Diplomacy', 'History/International Studies/Diplomacy'), ('Igbo', 'Igbo'), ('Language/Linguistics', 'Language/Linguistics'), ('Philosophy', 'Philosophy'), ('Political Science', 'Political Science'), ('Psychology', 'Psychology'), ('Religious Studies', 'Religious Studies'), ('Sociology', 'Sociology'), ('Yoruba', 'Yoruba'), ('Arts/Humanities(Other topics)', 'Arts/Humanities(Other topics)'))), ('Education', (('Adult/Non-Formal Education', 'Adult/Non-Formal Education'), ('Curriculum Studies', 'Curriculum Studies'), ('Educational Administration/Management', 'Educational Administration/Management'), ('Guidance and Counselling', 'Guidance and Counselling'), ('Library Studies', 'Library Studies'), ('Nursery/Primary Education', 'Nursery/Primary Education'), ('Physical and Health Education', 'Physical and Health Education'), ('Special Education', 'Special Education'), ('Teacher Education', 'Teacher Education'), ('Education(Other topics)', 'Education(Other topics)'))), ('Engineering/Environmental/Technology', (('Agricultural Engineering', 'Agricultural Engineering'), ('Architecture', 'Architecture'), ('Biomedical', 'Biomedical'), ('Chemical/Petroleum/Gas', 'Chemical/Petroleum/Gas'), ('Civil', 'Civil'), ('Computer', 'Computer'), ('Electrical/Electronics', 'Electrical/Electronics'), ('Estate Management', 'Estate Management'), ('Food Engineering/Technology', 'Food Engineering/Technology'), ('Land/Quantity Surveying', 'Land/Quantity Surveying'), ('Marine', 'Marine'), ('Mechanical/Production', 'Mechanical/Production'), ('Metallurgical and Materials', 'Metallurgical and Materials'), ('Polymer and Textile', 'Polymer and Textile'), ('Software', 'Software'), ('Urban and Regional Planning', 'Urban and Regional Planning'), ('Water Resources/Environmental', 'Water Resources/Environmental'), ('Engineering/Environmental/Technology(Other topics)', 'Engineering/Environmental/Technology(Other topics)'))), ('Law', (('Civil Law', 'Civil Law'), ('Common Law', 'Common Law'), ('International Law and Jurisprudence', 'International Law and Jurisprudence'), ('Islamic/Sharia Law', 'Islamic/Sharia Law'), ('Public Law', 'Public Law'), ('Law(Other topics)', 'Law(Other topics)'))), ('Medical', (('Basic Medical Sciences', 'Basic Medical Sciences'), ('Dentistry/Dental Technology', 'Dentistry/Dental Technology'), ('Human Medicine', 'Human Medicine'), ('Human Nutrition/Dietetics', 'Human Nutrition/Dietetics'), ('Medical Laboratory Science/Technology', 'Medical Laboratory Science/Technology'), ('Nursing', 'Nursing'), ('Optometry', 'Optometry'), ('Pharmacy/Pharmacology', 'Pharmacy/Pharmacology'), ('Physiotherapy', 'Physiotherapy'), ('Public Health', 'Public Health'), ('Radiography', 'Radiography'), ('Veterinary Medicine', 'Veterinary Medicine'), ('Medical(Other topics)', 'Medical(Other topics)'))), ('Science', (('Animal and Environmental Biology/Zoology', 'Animal and Environmental Biology/Zoology'), ('Biochemistry', 'Biochemistry'), ('Biotechnology/Genetics', 'Biotechnology/Genetics'), ('Botany', 'Botany'), ('Chemistry', 'Chemistry'), ('Computer Science', 'Computer Science'), ('Geology', 'Geology'), ('Mathematics/Statistics', 'Mathematics/Statistics'), ('Microbiology', 'Microbiology'), ('Physics', 'Physics'), ('Science(Other topics)', 'Science(Other topics)'))), ('Social/Management', (('Accounting', 'Accounting'), ('Banking and Finance', 'Banking and Finance'), ('Business Administration', 'Business Administration'), ('Economics', 'Economics'), ('Entrepreneurship', 'Entrepreneurship'), ('Insurance/Actuarial Science', 'Insurance/Actuarial Science'), ('Marketing', 'Marketing'), ('Project/Personnel Management', 'Project/Personnel Management'), ('Public Administration/Relation', 'Public Administration/Relation'), ('Taxation', 'Taxation'), ('Social/Management(Other topics)', 'Social/Management(Other topics)')))], max_length=60)),
                ('added_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Liked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('sender', models.CharField(max_length=150)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.CharField(default='name', max_length=50)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.AuthorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('co_authors', models.CharField(blank=True, max_length=500, null=True)),
                ('department', models.CharField(choices=[('', 'Choose department'), ('Agriculture', (('Agricultural Administration', 'Agricultural Administration'), ('Agricultural Business/Finance', 'Agricultural Business/Finance'), ('Agricultural Economics', 'Agricultural Economics'), ('Agricultural Extension', 'Agricultural Extension'), ('Agronomy', 'Agronomy'), ('Animal Science', 'Animal Science'), ('Crop Science', 'Crop Science'), ('Fisheries', 'Fisheries'), ('Forestry', 'Forestry'), ('Soil Science', 'Soil Science'), ('Agriculture(Other topics)', 'Agriculture(Other topics)'))), ('Arts/Humanities', (('Anthropology', 'Anthropology'), ('Arabic/Islamic Studies', 'Arabic/Islamic Studies'), ('Christian Studies', 'Christian Studies'), ('Communication Arts(Mass Communication etc)', 'Communication Arts(Mass Communication etc)'), ('Creative Arts(Fine Arts/Dramatic Arts/Music etc)', 'Creative Arts(Fine Arts/Dramatic Arts/Music etc)'), ('English Language and Literature', 'English Language and Literature'), ('French', 'French'), ('Geography', 'Geography'), ('Hausa', 'Hausa'), ('History/International Studies/Diplomacy', 'History/International Studies/Diplomacy'), ('Igbo', 'Igbo'), ('Language/Linguistics', 'Language/Linguistics'), ('Philosophy', 'Philosophy'), ('Political Science', 'Political Science'), ('Psychology', 'Psychology'), ('Religious Studies', 'Religious Studies'), ('Sociology', 'Sociology'), ('Yoruba', 'Yoruba'), ('Arts/Humanities(Other topics)', 'Arts/Humanities(Other topics)'))), ('Education', (('Adult/Non-Formal Education', 'Adult/Non-Formal Education'), ('Curriculum Studies', 'Curriculum Studies'), ('Educational Administration/Management', 'Educational Administration/Management'), ('Guidance and Counselling', 'Guidance and Counselling'), ('Library Studies', 'Library Studies'), ('Nursery/Primary Education', 'Nursery/Primary Education'), ('Physical and Health Education', 'Physical and Health Education'), ('Special Education', 'Special Education'), ('Teacher Education', 'Teacher Education'), ('Education(Other topics)', 'Education(Other topics)'))), ('Engineering/Environmental/Technology', (('Agricultural Engineering', 'Agricultural Engineering'), ('Architecture', 'Architecture'), ('Biomedical', 'Biomedical'), ('Chemical/Petroleum/Gas', 'Chemical/Petroleum/Gas'), ('Civil', 'Civil'), ('Computer', 'Computer'), ('Electrical/Electronics', 'Electrical/Electronics'), ('Estate Management', 'Estate Management'), ('Food Engineering/Technology', 'Food Engineering/Technology'), ('Land/Quantity Surveying', 'Land/Quantity Surveying'), ('Marine', 'Marine'), ('Mechanical/Production', 'Mechanical/Production'), ('Metallurgical and Materials', 'Metallurgical and Materials'), ('Polymer and Textile', 'Polymer and Textile'), ('Software', 'Software'), ('Urban and Regional Planning', 'Urban and Regional Planning'), ('Water Resources/Environmental', 'Water Resources/Environmental'), ('Engineering/Environmental/Technology(Other topics)', 'Engineering/Environmental/Technology(Other topics)'))), ('Law', (('Civil Law', 'Civil Law'), ('Common Law', 'Common Law'), ('International Law and Jurisprudence', 'International Law and Jurisprudence'), ('Islamic/Sharia Law', 'Islamic/Sharia Law'), ('Public Law', 'Public Law'), ('Law(Other topics)', 'Law(Other topics)'))), ('Medical', (('Basic Medical Sciences', 'Basic Medical Sciences'), ('Dentistry/Dental Technology', 'Dentistry/Dental Technology'), ('Human Medicine', 'Human Medicine'), ('Human Nutrition/Dietetics', 'Human Nutrition/Dietetics'), ('Medical Laboratory Science/Technology', 'Medical Laboratory Science/Technology'), ('Nursing', 'Nursing'), ('Optometry', 'Optometry'), ('Pharmacy/Pharmacology', 'Pharmacy/Pharmacology'), ('Physiotherapy', 'Physiotherapy'), ('Public Health', 'Public Health'), ('Radiography', 'Radiography'), ('Veterinary Medicine', 'Veterinary Medicine'), ('Medical(Other topics)', 'Medical(Other topics)'))), ('Science', (('Animal and Environmental Biology/Zoology', 'Animal and Environmental Biology/Zoology'), ('Biochemistry', 'Biochemistry'), ('Biotechnology/Genetics', 'Biotechnology/Genetics'), ('Botany', 'Botany'), ('Chemistry', 'Chemistry'), ('Computer Science', 'Computer Science'), ('Geology', 'Geology'), ('Mathematics/Statistics', 'Mathematics/Statistics'), ('Microbiology', 'Microbiology'), ('Physics', 'Physics'), ('Science(Other topics)', 'Science(Other topics)'))), ('Social/Management', (('Accounting', 'Accounting'), ('Banking and Finance', 'Banking and Finance'), ('Business Administration', 'Business Administration'), ('Economics', 'Economics'), ('Entrepreneurship', 'Entrepreneurship'), ('Insurance/Actuarial Science', 'Insurance/Actuarial Science'), ('Marketing', 'Marketing'), ('Project/Personnel Management', 'Project/Personnel Management'), ('Public Administration/Relation', 'Public Administration/Relation'), ('Taxation', 'Taxation'), ('Social/Management(Other topics)', 'Social/Management(Other topics)')))], max_length=60)),
                ('topic', models.CharField(max_length=300, unique=True)),
                ('publication', models.CharField(blank=True, max_length=250, null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('image1', models.ImageField(blank=True, default='image', null=True, upload_to='image')),
                ('image2', models.ImageField(blank=True, default='image', null=True, upload_to='image')),
                ('image3', models.ImageField(blank=True, default='image', null=True, upload_to='image')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('added_by', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('index_paper', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
                ('likes', models.IntegerField(default=0)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('added_by', models.CharField(max_length=50)),
                ('review_author', models.CharField(default='review_author', max_length=150)),
                ('paper_reviewed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Paper')),
            ],
        ),
        migrations.AddField(
            model_name='liked',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Review'),
        ),
        migrations.AlterUniqueTogether(
            name='liked',
            unique_together={('added_by', 'review')},
        ),
    ]
