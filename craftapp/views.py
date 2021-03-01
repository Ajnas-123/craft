from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect,JsonResponse
from craftapp.models import *
import hashlib
import random
import string
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.cache import cache_control
@cache_control(no_cache=True,must_revalidate=True,no_store=True)

# Create your views here.
def display(request):
	view=product_tb.objects.all().filter(status='approve')
	return render(request,'index.html',{'view':view})


def about(request):
	return render(request,'about.html')


def blog(request):
	return render(request,'blog.html')

def contact(request):
	return render(request,'contact.html')


def login(request):
	return render(request,'login.html')

def register(request):
	return render(request,'register.html')

def user_register(request):
	if request.method=='POST':
		fname=request.POST['first_name']
		lname=request.POST['last_name']
		uemail=request.POST['email']
		upass=request.POST['password']
		hashpass=hashlib.md5(upass.encode('utf8')).hexdigest()

		check=user_tb.objects.all().filter(email=uemail)
		if check:
			return render(request,'register.html',{'msg':'already exist'})

		else:
			x = ''.join(random.choices(fname + lname + string.digits, k=8))
			y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
			subject = 'welcome to Louis craft'
			message = f'Hi {fname} {lname}, thank you for registering in Louis. your  email: {uemail} and  password: {upass}.'
			email_from = settings.EMAIL_HOST_USER 
			recipient_list = [uemail, ] 
			send_mail( subject, message, email_from, recipient_list ) 


			query=user_tb(firstname=fname,lastname=lname,password=hashpass,email=uemail)
			query.save()
			view=product_tb.objects.all().filter(status='approve')
			return render(request,"index.html",{'view':view})
			
	else:
		view=product_tb.objects.all().filter(status='approve')
		return render(request,"index.html",{'view':view})
		




################################################################################################




@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def user_login(request):
	if request.method=='POST':
		uemail=request.POST['email']
		upass=request.POST['password']
		hashpass=hashlib.md5(upass.encode('utf8')).hexdigest()

		query=user_tb.objects.filter(email=uemail,password=hashpass)
		if query:
			for x in query:
				request.session['userid']=x.id
				request.session['username']=x.firstname

				uid=request.session['userid']
			view=product_tb.objects.all().filter(status='approve')
			return HttpResponseRedirect("/",{'view':view,'success':"login Succesful"})

			
		else:

			return render(request,'login.html',{'error':"Incorrect username/password"})	
	else:
		view=product_tb.objects.all().filter(status='approve')
		return render(request,"index.html",{'view':view})
			

################################################################################################


def logout(request):
	if request.session.has_key('userid'):
		del request.session['userid']
	view=product_tb.objects.all().filter(status='approve')

	return render(request,"index.html",{'view':view})

	





###############################################################
def admin_login(request):
	if request.method=='POST':
		uname=request.POST['name']
		upass=request.POST['password']

		query=admin_tb.objects.filter(name=uname,password=upass)
		if query:
			for x in query:
				request.session['adminid']=x.id
				request.session['adminname']=x.name
			return render(request,"admin/adminpage.html")
		else:
			return render(request,'admin/adminlogin.html',{'error':"Incorrect username/password"})	
	else:
		return render(request,'admin/adminlogin.html')
	

#################################################################################################


def admin_page(request):
	if request.session.has_key('adminid'):
		return render(request,"admin/adminpage.html")
	else:
		return render(request,'admin/adminlogin.html')

################################################################################################



def admin_logout(request):
	if request.session.has_key('adminid'):
		del request.session['adminid']
		del request.session['adminname']
	view=product_tb.objects.all().filter(status='approve')
	return render(request,"index.html",{'view':view})



################################################################################################

def add_product(request):
	if request.method=='POST':
		uitem=request.FILES['item']
		uproduct=request.POST['product']
		ucategory=request.POST['category']
		udescription=request.POST['description']
		user=request.session['userid']
		uid=user_tb.objects.get(id=user)

		print(user)
		query=product_tb(item=uitem,name=uproduct,category=ucategory,description=udescription,user=uid,status="pending")
		query.save()
		view=product_tb.objects.all().filter(status='approve')
		return render(request,"index.html",{'view':view})
	else:
		return render(request,"add_product.html")


################################################################################################

def product_details(request):
	if request.session.has_key('adminid'):
		view=product_tb.objects.all().filter(status='pending')
		return render(request,'admin/table.html',{'view':view})
	else:
		return render(request,'admin/adminlogin.html')

################################################################################################


def approved_products(request):
	# if request.session.has_key['adminid']:
	dd=request.GET['nid']
	pid=product_tb.objects.filter(id=dd).update(status='approve')
	return HttpResponseRedirect('/product_details/')

		# return render(request,'admin/adminlogin.html')

################################################################################################

def rejected_products(request):
	# if request.session.has_key['adminid']:
	pd=request.GET['pid']
	pid=product_tb.objects.filter(id=pd).update(status='reject')
	return HttpResponseRedirect('/product_view/')

################################################################################################

def view_product(request):
	if request.session.has_key('userid'):
		view=product_tb.objects.all().filter(status='approve')
		return render(request,'index.html',{'view':view})
	else:
		return render(request,'login.html')


################################################################################################

def user_details(request):
	if request.session.has_key('adminid'):
		user=product_tb.objects.all()
		return render(request,'admin/user_details.html',{'user':user})
	else:
		return render(request,'admin/adminlogin.html')


################################################################################################

def query_details(request):
	if request.method=='POST':
		qname=request.POST['name']
		qemail=request.POST['email']
		qphone=request.POST['number']
		qsubject=request.POST['subject']
		qmessage=request.POST['message']
		query=contact_tb(name=qname,email=qemail,number=qphone,subject=qsubject,message=qmessage)
		query.save()
		view=product_tb.objects.all().filter(status='approve')
		return render(request,"index.html",{'view':view})
	else:
		return render(request,'contact.html')


################################################################################################

def contact_details(request):
	if request.session.has_key('adminid'):
		con=contact_tb.objects.all()
		return render(request,'admin/contact_details.html',{'con':con})
	else:
		return render(request,'admin/adminlogin.html')

################################################################################################


def single_page(request):
	if request.session.has_key('userid'):
		qd=request.GET['iid']
		qid=product_tb.objects.filter(id=qd)
		view=review_tb.objects.filter(product_id=qd)
		return render(request,"singlepage.html",{'qid':qid,'view':view})
	else:
		view=product_tb.objects.all().filter(status='approve')
		return render(request,"index.html",{'view':view})


################################################################################################







def review(request):
	if request.method=='POST':
		ureview=request.POST['review']
		user=request.session['userid']
		pd=request.POST['nid']
		print(pd)
		uid=user_tb.objects.get(id=user)
		pid=product_tb.objects.get(id=pd)
		date=datetime.date.today()
		# pid=product_tb.objects.get(id=prid)
		review=review_tb(review=ureview,user_id=uid,product_id=pid,date=date,)
		review.save()
		view=product_tb.objects.all().filter(status='approve')
		return render(request,"index.html",{'view':view})
	else:
		return render(request,'singlepage.html')



################################################################################################

def search(request):
	if request.method=='POST':
		fn=request.POST['q']
		qid=product_tb.objects.filter(name__icontains=fn,status='approve')
		return render(request,"index.html",{'view':qid})
	else:
		view=product_tb.objects.all().filter(status='approve')
		return render(request,"index.html",{'view':view})


