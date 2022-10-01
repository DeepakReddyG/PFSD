from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail 
from django.core.mail import send_mass_mail 
import csv
# Create your views here.
def home(request):
	return HttpResponse("Hello World Example of PFSD") 
def about(request):
	return render(request,'about.html')
def modi(request):
	return render(request,'modi.html')
def counter(request):
	return render(request,'index.html')
def getFile(request):
	response = HttpResponse(content_type='text/csv') 
	response['Content-Disposition'] = 'attachment; filename="students.csv"' 
	writer = csv.writer(response)
	writer.writerow(['2100030101','Absent']) 
	writer.writerow(['2100030102','present']) 
	
	
def mail1(request):
	send_mail(
	'Test Mail using django framwork',
	'Greetings',
	'deepakreddygathpa@gmail.com',
	['deepak@kluniversity.in'],
	fail_silently = False,
	)
	return print('Mail sent') 
