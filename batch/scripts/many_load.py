import csv
from os import name  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete
    Region.objects.all().delete()
    Site.objects.all().delete()


    # Format
    # name, description, justification, year, longitude, latitude, area_hectares,
    # category, state, region, iso

    for row in reader:
        print(row)

        cat, created = Category.objects.get_or_create(name=row[7])
        st, created = State.objects.get_or_create(name=row[8])
        reg, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
            desc = row[1]
        except:
            desc = None
        
        try:
            just = row[2]
        except:
            just = None
        
        try:
            y = int(row[3])
        except:
            y = None

        try:
            long = float(row[4])
        except:
            long = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            area = float(row[5])
        except:
            area = None
    
        site = Site(name=row[0], description=desc, justification=just, year=y, longitude=long, latitude=lat, area_hectares=area, category=cat, state=st, region=reg, iso=i)
        site.save()