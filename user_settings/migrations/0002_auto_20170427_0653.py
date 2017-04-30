# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='body_type',
            field=models.IntegerField(choices=[(1, b'Athletic'), (2, b'Average'), (3, b'Slim'), (4, b'Heavy')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='cast',
            field=models.CharField(blank=True, max_length=120, verbose_name='Cast'),
        ),
        migrations.AddField(
            model_name='profile',
            name='complexion',
            field=models.IntegerField(choices=[(1, b'Dark'), (2, b'Fair'), (3, b'Wheatish Brown')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='current_location',
            field=models.CharField(blank=True, max_length=200, verbose_name='Current Location'),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.IntegerField(choices=[(0, b'Select Option'), (b'1.37', b'1.37m (4\' 6")'), (b'1.38', b'1.38m'), (b'1.39', b'1.39m'), (b'1.4', b'1.40m (4\' 7")'), (b'1.41', b'1.41m'), (b'1.42', b'1.42m (4\' 8")'), (b'1.43', b'1.43m'), (b'1.44', b'1.44m'), (b'1.45', b'1.45m (4\' 9")'), (b'1.46', b'1.46m'), (b'1.47', b'1.47m (4\' 10")'), (b'1.48', b'1.48m'), (b'1.49', b'1.49m'), (b'1.5', b'1.50m (4\' 11")'), (b'1.51', b'1.51m'), (b'1.52', b'1.52m (5\' 0")'), (b'1.53', b'1.53m'), (b'1.54', b'1.54m'), (b'1.55', b'1.55m (5\' 1")'), (b'1.56', b'1.56m'), (b'1.57', b'1.57m (5\' 2")'), (b'1.58', b'1.58m'), (b'1.59', b'1.59m'), (b'1.6', b'1.60m (5\' 3")'), (b'1.61', b'1.61m'), (b'1.62', b'1.62m'), (b'1.63', b'1.63m (5\' 4")'), (b'1.64', b'1.64m'), (b'1.65', b'1.65m (5\' 5")'), (b'1.66', b'1.66m'), (b'1.67', b'1.67m'), (b'1.68', b'1.68m (5\' 6")'), (b'1.69', b'1.69m'), (b'1.7', b'1.70m (5\' 7")'), (b'1.71', b'1.71m'), (b'1.72', b'1.72m'), (b'1.73', b'1.73m (5\' 8")'), (b'1.74', b'1.74m'), (b'1.75', b'1.75m (5\' 9")'), (b'1.76', b'1.76m'), (b'1.77', b'1.77m'), (b'1.78', b'1.78m (5\' 10")'), (b'1.79', b'1.79m'), (b'1.8', b'1.80m (5\' 11")'), (b'1.81', b'1.81m'), (b'1.82', b'1.82m'), (b'1.83', b'1.83m (6\' 0")'), (b'1.84', b'1.84m'), (b'1.85', b'1.85m (6\' 1")'), (b'1.86', b'1.86m'), (b'1.87', b'1.87m'), (b'1.88', b'1.88m (6\' 2")'), (b'1.89', b'1.89m'), (b'1.9', b'1.90m'), (b'1.91', b'1.91m (6\' 3")'), (b'1.92', b'1.92m'), (b'1.93', b'1.93m (6\' 4")'), (b'1.94', b'1.94m'), (b'1.95', b'1.95m'), (b'1.96', b'1.96m (6\' 5")'), (b'1.97', b'1.97m'), (b'1.98', b'1.98m (6\' 6")'), (b'1.99', b'1.99m'), (b'2', b'2.00m'), (b'2.01', b'2.01m (6\' 7")'), (b'2.02', b'2.02m'), (b'2.03', b'2.03m (6\' 8")'), (b'2.04', b'2.04m'), (b'2.05', b'2.05m'), (b'2.06', b'2.06m (6\' 9")'), (b'2.07', b'2.07m'), (b'2.08', b'2.08m (6\' 10")'), (b'2.09', b'2.09m'), (b'2.1', b'2.10m'), (b'2.11', b'2.11m (6\' 11")'), (b'2.12', b'2.12m'), (b'2.13', b'2.13m (7\' 0")'), (b'2.14', b'2.14m'), (b'2.15', b'2.15m'), (b'2.16', b'2.16m (7\' 1")')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='income',
            field=models.IntegerField(choices=[(0, b'Prefer not to say'), (1, b'Under Rs 50,000'), (2, b'Rs 50,000 - Rs 1,00,000'), (3, b'Rs 1,00,000 - Rs 3,00,000'), (4, b'Rs 3,00,000 - Rs 5,00,000'), (4, b'Rs 5,00,000 - Rs 10,00,000'), (6, b'Above Rs 10,00,000')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_inter_cast',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='marital_status',
            field=models.IntegerField(choices=[(0, b'Never Married'), (1, b'Divorced'), (2, b'Seperated'), (3, b'Widow/Widower')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.IntegerField(choices=[(0, b'Select Occupation'), (3, b'Accountant'), (4, b'Acting Professional'), (5, b'Actor'), (6, b'Administration Professional'), (7, b'Advertising Professional'), (100, b'Advocate'), (8, b'Air Hostess'), (9, b'Architect'), (10, b'Artisan'), (11, b'Audiologist'), (102, b'Autocade Engineer'), (12, b'Banker'), (13, b'Beautician'), (14, b'Biologist / Botanist'), (95, b'Business'), (15, b'Business Person'), (16, b'Chartered Accountant'), (17, b'Civil Engineer'), (18, b'Clerical Official'), (19, b'Commercial Pilot'), (20, b'Company Secretary'), (21, b'Computer Professional'), (22, b'Consultant'), (23, b'Contractor'), (24, b'Cost Accountant'), (25, b'Creative Person'), (26, b'Customer Support Professional'), (27, b'Defense Employee'), (28, b'Dentist'), (29, b'Designer'), (105, b'Diploma Electronic &amp; comm. Engineering'), (106, b'Diploma Electronic &amp; comm. Engineering'), (118, b'Diploma in Hotel Management'), (117, b'Diploma in Hotel Managment'), (30, b'Doctor'), (31, b'Economist'), (93, b'Education officer.'), (121, b'Educational Evelution Work'), (94, b'Electrical Engineer'), (32, b'Engineer'), (33, b'Engineer (Mechanical)'), (34, b'Engineer (Project)'), (35, b'Entertainment Professional'), (36, b'Event Manager'), (37, b'Executive'), (38, b'Factory worker'), (39, b'Farmer'), (40, b'Fashion Designer'), (103, b'Film Director'), (41, b'Finance Professional'), (42, b'Flight Attendant'), (43, b'Government Employee'), (44, b'Health Care Professional'), (45, b'Home Maker'), (46, b'Hotel &amp; Restaurant Professional'), (98, b'House Hold work'), (47, b'Human Resources Professional'), (104, b'Insurance Adviser'), (48, b'Interior Designer'), (49, b'Investment Professional'), (50, b'IT / Telecom Professional'), (114, b'Job'), (97, b'Job in Bank'), (101, b'Job In Call Centre.'), (119, b'Job in Infrastructure Company'), (109, b'Job in Multi National Company'), (96, b'Job in Private Company'), (99, b'Job in Private Office'), (51, b'Journalist'), (107, b'Lab Technician'), (52, b'Lawyer'), (53, b'Lecturer'), (54, b'Legal Professional'), (113, b'Librerian'), (55, b'Manager'), (56, b'Marketing Professional'), (57, b'Media Professional'), (58, b'Medical Professional'), (108, b'Medical Representative'), (59, b'Medical Transcriptionist'), (60, b'Merchant Naval Officer'), (2, b'Non-mainstream professional'), (1, b'Not working'), (61, b'Nurse'), (62, b'Occupational Therapist'), (63, b'Optician'), (64, b'Pharmacist'), (65, b'Physician Assistant'), (66, b'Physicist'), (67, b'Physiotherapist'), (68, b'Pilot'), (69, b'Politician'), (70, b'Production professional'), (71, b'Professor'), (72, b'Psychologist'), (73, b'Public Relations Professional'), (74, b'Real Estate Professional'), (120, b'Relationship Manager'), (75, b'Research Scholar'), (112, b'Research Scientist'), (77, b'Retail Professional'), (76, b'Retired Person'), (78, b'Sales Professional'), (79, b'Scientist'), (122, b'Searching Job'), (80, b'Self-employed Person'), (81, b'Social Worker'), (82, b'Software Consultant'), (111, b'Software Engineer'), (83, b'Sportsman'), (84, b'Student'), (85, b'Teacher'), (86, b'Technician'), (87, b'Training Professional'), (88, b'Transportation Professional'), (110, b'Tuition Class'), (115, b'Typiest'), (89, b'Veterinary Doctor'), (90, b'Volunteer'), (116, b'Web Designer'), (91, b'Writer'), (92, b'Zoologist'), (123, b'Other')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='permanent_location',
            field=models.CharField(blank=True, max_length=200, verbose_name='Permanent Location'),
        ),
        migrations.AddField(
            model_name='profile',
            name='qualification',
            field=models.IntegerField(choices=[(0, b'Select Qualification'), (1, b'Alim / Alima'), (2, b'B. Architect'), (3, b'B.E  (Chemical)'), (4, b'B.E  Bio Medical Instrumentation Engineer'), (5, b'B.E ( Automobile Engineering )'), (6, b'B.E ( Civil Engineer )'), (7, b'B.E ( Computer Engineer )'), (8, b'B.E ( Electrical )'), (9, b'B.E ( Electronics &amp; Communication )'), (10, b'B.E ( I.T )'), (11, b'B.E ( Manufacturing )'), (12, b'B.E ( Software Engineer )'), (13, b'B.E (Electronics)'), (14, b'B.E (Industrial)'), (15, b'B.E (Instrumentation &amp; Control)'), (16, b'B.E (Mechanical)'), (17, b'B.E Metallurgy'), (18, b'B.E Structural Engineer'), (19, b'B.E Textile Engineer'), (20, b'B.E.( Plastic )'), (21, b'B.E.(Production)'), (22, b'B.H.M.S'), (23, b'B.P.Ed'), (24, b'B.Tech'), (25, b'Bachelor in Hotel Management'), (26, b'Bachelor in Interior Designing'), (27, b'Bachelor in Prosthetics and Orthotics'), (28, b'Bachelor of an Airhostess'), (29, b'Bachelor of Arts'), (30, b'Bachelor of Business Administration'), (31, b'Bachelor of Commerce'), (32, b'Bachelor of Computer Applications'), (33, b'Bachelor of Computer Science'), (34, b'Bachelor of Design'), (35, b'Bachelor of Education'), (36, b'Bachelor of Engineering civil'), (37, b'Bachelor of Home Science'), (38, b'Bachelor of Management Science for Finance'), (39, b'Bachelor of Medicine in Electro-Homoeopathy'), (40, b'Bachelor of Nursing'), (41, b'Bachelor of Occupational Therapy'), (42, b'Bachelor of Optometrist'), (43, b'Bachelor of Pharmacy'), (44, b'Bachelor of Physiotherapy'), (45, b'Bachelor of Science'), (46, b'Bachelor of Veterinary Science and Animal Husbandry'), (47, b'Bachelors  in  Hospitality &amp; Tourism  Management'), (48, b'Bachelors of Psychology'), (49, b'BAMS'), (50, b'BDS'), (51, b'BE ( Environmental Engineering)'), (52, b'BSW'), (53, b'BUMS'), (54, b'Chartered Accountant'), (55, b'Company Secretary'), (56, b'DHMS'), (57, b'Dialysis Technician Course'), (58, b'Diploma  in Mechanical  Engineering'), (59, b'Diploma  in Multimedia'), (60, b'Diploma Computer Engineer'), (61, b'Diploma Electronic &amp; comm. Engineering'), (62, b'Diploma in Automobiles Engineer'), (63, b'Diploma in Beauty Parlor'), (64, b'Diploma in Ceramic Engineer'), (65, b'Diploma in Chemical Engineering'), (66, b'Diploma in Civil Engineer'), (67, b'Diploma In Computer Application'), (68, b'Diploma in Electrical  Engineering'), (69, b'Diploma in Fashion Designing'), (70, b'Diploma in Home Science'), (71, b'Diploma in Hotel managment'), (72, b'Diploma in Medical Laboratory Technology'), (73, b'Diploma in Nursing'), (74, b'Diploma in Pharmacy'), (75, b'Diploma in Plastic Engineering'), (76, b'Diploma in Software Engineering'), (77, b'Diploma'), (78, b'Fashion Designing'), (79, b'Fine Arts'), (80, b'General Nursing &amp; Midwifery'), (81, b'H.S.C.'), (82, b'I.T Professional'), (83, b'ITI - Industrial Training Institute'), (84, b'LLB'), (85, b'LLM'), (86, b'M. Lib'), (87, b'M.B.A'), (88, b'M.B.B.S.'), (89, b'M.C.A'), (90, b'M.Com.'), (91, b'M.D ( Anesthesia )'), (92, b'M.D (Physician)'), (93, b'M.D (Pidiatric)'), (94, b'M.E  (Chemical)'), (95, b'M.E ( I.T)'), (96, b'M.E ( Mechanical )'), (97, b'M.E (Electronic &amp; Communication )'), (98, b'M.E Civil ( Geotech )'), (99, b'M.E. ( Structure )'), (100, b'M.E.(Production)'), (101, b'M.Ed ( Masters in Education )'), (102, b'M.Pharmacy'), (103, b'M.Phil'), (104, b'M.S.W ( Master in Social Work )'), (105, b'M.Sc ( I.T )'), (106, b'M.Tech'), (107, b'Master  Degree  in Development  Communication'), (108, b'Master  of   Fine Arts'), (109, b'Master in Computer Science'), (110, b'Master Of Accounting and Financial Management'), (111, b'Master of Arts'), (112, b'Master of Computer Engineering'), (113, b'Master of E-Commerce'), (114, b'Master of MASS Comunication'), (115, b'Master of PhysioTherapy'), (116, b'Master of Science'), (117, b'Masters in Clinical Psychology'), (118, b'Masters in Project Management &amp; Security System'), (119, b'MD( Pidiatric)'), (120, b'MDS ( Master of Dental surgery )'), (121, b'NDDY ( Naturopathy Doctor )'), (122, b'Occupational Theraphy'), (123, b'P.G  in Human Resaurce Management'), (124, b'P.T.C'), (125, b'PGDIT'), (126, b'Ph.D'), (127, b'S.S.C.'), (128, b'Sanitary inspector'), (129, b'School level'), (130, b'Other')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='reason_registration',
            field=models.IntegerField(choices=[(1, b"I'm registring to find myself a partner"), (2, b"I'm registring to find my friend a partner"), (3, b"I'm registring to find my son a partner"), (4, b"I'm registring to find my daughter a partner"), (5, b"I'm registring to find my brother a partner"), (6, b"I'm registring to find my sister a partner")], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(choices=[(0, b'Select Option'), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99), (100, 100), (101, 101), (102, 102), (103, 103), (104, 104), (105, 105), (106, 106), (107, 107), (108, 108), (109, 109), (110, 110), (111, 111), (112, 112), (113, 113), (114, 114), (115, 115), (116, 116), (117, 117), (118, 118), (119, 119), (120, 120)], null=True),
        ),
    ]
