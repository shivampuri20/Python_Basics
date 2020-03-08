import datetime
import pytz #standary library for timezones
d=datetime.date(2016,7,24)
print d
print d.strftime('%B %d ,%Y')


dt_str='july 26 ,2016'
dt=datetime.datetime.strptime(dt_str,'%B %d ,%Y')
print dt

tday=datetime.date.today()
#print tday.weekday()  #monday=0 and sunday =6
#print tday.isoweekday() #monday=1

tdelta=datetime.timedelta(days=7)
print tday +tdelta


bday=datetime.date(2019,12,17)
till_bday=bday-tday                  #finding remaining days till bday 
print till_bday.days

#now working with time 

t=datetime.time(9,30,45,1000)
print t.hour

#combined

dt=datetime.datetime(2016,7,26,12,30,45,1000)
print dt.time() 

#dt_today=datetime.datetime.today()
#dt_now=datetime.datetime.now()
#dt_utcnow=datetime.datetime.utcnow()

#print dt_today
#print dt_now
#print dt_utcnow  #universal time

#using pytz USED TO LOCALIZE THE TIME ACCORDING TO UNIVERSAL TIME 
dt=datetime.datetime(2016,7,26,12,30,45,tzinfo=pytz.UTC) 
print dt

#dt_now=datetime.datetime.now(tz=pytz.UTC)
#print dt_now


dt_utcnow=datetime.datetime.now(tz=pytz.UTC)
print dt_utcnow

#dt_calc=dt_utcnow.astimezone(pytz.timezone('ASIA/CALCUTTA'))  #printing calcultta live time 
#print dt_calc

#for tz in pytz.all_timezones:   #printing  all   time zones
#    print tz

dt_calcutta=datetime.datetime.now()        #another method using localize
calcutta_tz=pytz.timezone('ASIA/CALCUTTA')

dt_calcutta=calcutta_tz.localize(dt_calcutta)

#print dt_calcutta

#dt_dubai=dt_calcutta.astimezone(pytz.timezone('ASIA/DUBAI')   #conerting calcutta time to dubai time 
#print dt_dubai














