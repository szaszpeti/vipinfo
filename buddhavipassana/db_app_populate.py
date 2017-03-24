import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','buddhavipassana.settings')

import django
# Import settings
django.setup()

import random
from db_app.models import Meditator
from faker import Faker

fakegen = Faker()
course = ['Basic','Intro','Retreat','Assistant']

def add_course():
    t = copic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    course_type = ['Basic', 'Intro', 'Retreat', 'Assistant']
    teacher_name = ['Thanat', 'Kate', 'Mohamad', 'Sandra', 'Asher', 'Hildegard', 'Jonathan', 'Hannah', 'Phra Ofer', 'Edward']
    gender_type = ['Male', 'Femail']


    for entry in range(N):

        # Create Fake Data for entry
        name = fakegen.name()
        country = fakegen.country()
        born = fakegen.year()
        gender = random.choice(gender_type)
        email = fakegen.email()
        phone = fakegen.phone_number()
        profession = fakegen.job()
        course = random.choice(course_type)
        course_date = fakegen.date()
        teacher = random.choice(teacher_name)
        remarks = fakegen.text(30)


        # Create new Webpage Entry
        medit = Meditator.objects.get_or_create(name=name, country=country, born=born, gender=gender, email=email,
                                                phone=phone, profession=profession, course=course, course_date = course_date,
                                                teacher=teacher, remarks=remarks)




if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(1000)
    print('Populating Complete')
