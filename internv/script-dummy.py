from backend.models import User, ActivityPeriod
from faker import Faker
import random
import pytz
from datetime import datetime  
from datetime import timedelta  
fake = Faker()

for x in range(100):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    idsq= fake.bothify(text='?#??###??#', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
    rname= fake.name()
    tzone= random.choice(TIMEZONES)
    user = User(id=idsq , real_name=rname , tz=tzone)
    user.save()
    for y in range(4):
        stdate=fake.date_time(tzinfo=None, end_datetime=None)
        endate=stdate+timedelta(minutes=random.randint(1,100))
        ap=ActivityPeriod(ids=idsq, start_time=stdate, end_time= endate )
        ap.save()
        
    

        
