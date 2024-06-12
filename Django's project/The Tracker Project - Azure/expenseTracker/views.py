from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate ,logout
from django.contrib.auth import login as dj_login
from django.contrib.auth.models import User
from .models import Addmoney_info,UserProfile
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.db.models import Sum
from django.http import JsonResponse
import datetime
from django.utils import timezone
from django.shortcuts import render,redirect
import requests
# Import the required library
from geopy.geocoders import Nominatim



# Create your views here.
def home(request):
    if request.session.has_key('is_logged'):
        return redirect('/homepage')
    return render(request,'home/loginBoostrap.html')
   # return HttpResponse('This is home')

def homePage(request):
    return render(request, 'homepageBoostrap.html')


def index(request):
    if request.session.has_key('is_logged'):
        user_id = request.session["user_id"]
        user = User.objects.get(id=user_id)
        addmoney_info = Addmoney_info.objects.filter(user=user).order_by('-Date')
        paginator = Paginator(addmoney_info , 4)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator,page_number)
        context = {
            # 'add_info' : addmoney_info,
           'page_obj' : page_obj
        }
    #if request.session.has_key('is_logged'):
        return render(request,'home/indexBoostrap.html',context)
    return redirect('home')
    #return HttpResponse('This is blog')

def phonePage(request):
    if request.session.has_key('is_logged'):   
        url = "https://validate-phone-by-api-ninjas.p.rapidapi.com/v1/validatephone" 
        headers = {
            "content-type": "application/octet-stream",
            "X-RapidAPI-Key": "6b6830f7f5msh36a077104b6fdcbp19d6b9jsn4eb36ae47d3f",
            "X-RapidAPI-Host": "validate-phone-by-api-ninjas.p.rapidapi.com"
        }

        geolocator = Nominatim(user_agent="MyApp")
        
        if request.method == "POST":
            

            phoneNumber = request.POST.get('phoneNumber', None)

            if phoneNumber == "":

                return render(request, "home/phonePage.html")
            
            querystring = {"number":phoneNumber}

        

            response = requests.get(url, headers=headers, params=querystring)

            d = response.json()
       
            location = d['location'] +" " +  d['country']
            format = d['format_international']
            timezones = d['timezones'][0]


            getLocation = geolocator.geocode(location)
            center = [getLocation.longitude, getLocation.latitude]
            
            mapbox_access_token = 'pk.eyJ1Ijoic2hpbmJ1ZHVrYWkiLCJhIjoiY2xoNnNrM2g3MDIzYjNubTEyY2l3NnFxbCJ9.UgetyVGAihDUp6nnBwpnAg'

            context = {
                'location': location,
                'phoneNumber' : phoneNumber,
                'format' : format,
                'timezones' : timezones,
                'mapbox_access_token':mapbox_access_token,
                'center':center

            }
           

            return render(request, "home/phonePage.html", context)

        return render(request, "home/phonePage.html")


def register(request):
    return render(request,'home/signUpBoostrap.html')
    #return HttpResponse('This is blog')
def password(request):
    return render(request,'home/password.html')

def charts(request):
    return render(request,'home/charts.html')
def search(request):
    if request.session.has_key('is_logged'):
        user_id = request.session["user_id"]
        user = User.objects.get(id=user_id)
        fromdate = request.GET['fromdate']
        todate = request.GET['todate']
        addmoney = Addmoney_info.objects.filter(user=user, Date__range=[fromdate,todate]).order_by('-Date')
        return render(request,'home/tables.html',{'addmoney':addmoney})
    return redirect('home')
def tables(request):
    if request.session.has_key('is_logged'):
        user_id = request.session["user_id"]
        user = User.objects.get(id=user_id)
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        addmoney = Addmoney_info.objects.filter(user=user).order_by('-Date')
        return render(request,'home/tables.html',{'addmoney':addmoney})
    return redirect('home')
def addmoney(request):
    return render(request,'home/addmoney.html')

def profile(request):
    if request.session.has_key('is_logged'):
        return render(request,'home/profile.html')
    return redirect('/home')

def profile_edit(request,id):
    if request.session.has_key('is_logged'):
        add = User.objects.get(id=id)
        # user_id = request.session["user_id"]
        # user1 = User.objects.get(id=user_id)
        return render(request,'home/profile_edit.html',{'add':add})
    return redirect("/home")

def profile_update(request,id):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            user = User.objects.get(id=id)
            user.first_name = request.POST["fname"]
            user.last_name = request.POST["lname"]
            user.email = request.POST["email"]
            user.userprofile.Savings = request.POST["Savings"]
            user.userprofile.income = request.POST["income"]
            user.userprofile.profession = request.POST["profession"]
            user.userprofile.save()
            user.save()
            return redirect("/profile")
    return redirect("/home")   

def handleSignup(request):
    if request.method =='POST':
            # get the post parameters
            uname = request.POST["uname"]
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email = request.POST["email"]
            profession = request.POST['profession']
            Savings = request.POST['Savings']
            income = request.POST['income']
            pass1 = request.POST["pass1"]
            pass2 = request.POST["pass2"]
            profile = UserProfile(Savings = Savings,profession=profession,income=income)
            # check for errors in input
            if request.method == 'POST':
                try:
                    user_exists = User.objects.get(username=request.POST['uname'])
                    messages.error(request," Username already taken, Try something else!!!")
                    return redirect("/register")    
                except User.DoesNotExist:
                    if len(uname)>15:
                        messages.error(request," Username must be max 15 characters, Please try again")
                        return redirect("/register")
            
                    if not uname.isalnum():
                        messages.error(request," Username should only contain letters and numbers, Please try again")
                        return redirect("/register")
            
                    if pass1 != pass2:
                        messages.error(request," Password do not match, Please try again")
                        return redirect("/register")
            
            # create the user
            user = User.objects.create_user(uname, email, pass1)
            user.first_name=fname
            user.last_name=lname
            user.email = email
            # profile = UserProfile.objects.all()

            user.save()
            # p1=profile.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request," Your account has been successfully created")
            return redirect("/")
    else:
        return HttpResponse('404 - NOT FOUND ')
    return redirect('/login')

def handlelogin(request):
    if request.method =='POST':
        # get the post parameters
        loginuname = request.POST["loginuname"]
        loginpassword1=request.POST["loginpassword1"]
        user = authenticate(username=loginuname, password=loginpassword1)
        if user is not None:
            dj_login(request, user)
            request.session['is_logged'] = True
            user = request.user.id 
            request.session["user_id"] = user
            messages.success(request, " Successfully logged in")
            return redirect('/homepage')
        else:
            messages.error(request," Invalid Credentials, Please try again")  
            return redirect("/")  
    return HttpResponse('404-not found')
def handleLogout(request):
        del request.session['is_logged']
        del request.session["user_id"] 
        logout(request)
        messages.success(request, " Successfully logged out")
        return redirect('home')

#add money form
def addmoney_submission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            user_id = request.session["user_id"]
            user1 = User.objects.get(id=user_id)
            addmoney_info1 = Addmoney_info.objects.filter(user=user1).order_by('-Date')
            add_money = request.POST["add_money"]
            quantity = request.POST["quantity"]
            Date = request.POST["Date"]
            Category = request.POST["Category"]
            add = Addmoney_info(user = user1,add_money=add_money,quantity=quantity,Date = Date,Category= Category)
            add.save()
            paginator = Paginator(addmoney_info1, 4)
            page_number = request.GET.get('page')
            page_obj = Paginator.get_page(paginator,page_number)
            context = {
                'page_obj' : page_obj
                }
            return render(request,'home/indexBoostrap.html',context)
    return redirect('/index')
def addmoney_update(request,id):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            add  = Addmoney_info.objects.get(id=id)
            add .add_money = request.POST["add_money"]
            add.quantity = request.POST["quantity"]
            add.Date = request.POST["Date"]
            add.Category = request.POST["Category"]
            add .save()
            return redirect("/index")
    return redirect("/home")        

def expense_edit(request,id):
    if request.session.has_key('is_logged'):
        addmoney_info = Addmoney_info.objects.get(id=id)
        user_id = request.session["user_id"]
        user1 = User.objects.get(id=user_id)
        return render(request,'home/expense_edit.html',{'addmoney_info':addmoney_info})
    return redirect("/home")  

def expense_delete(request,id):
    if request.session.has_key('is_logged'):
        addmoney_info = Addmoney_info.objects.get(id=id)
        addmoney_info.delete()
        return redirect("/index")
    return redirect("/home")  

def expense_month(request):
    todays_date = datetime.date.today()
    one_month_ago = todays_date-datetime.timedelta(days=30)
    user_id = request.session["user_id"]
    user1 = User.objects.get(id=user_id)
    addmoney = Addmoney_info.objects.filter(user = user1,Date__gte=one_month_ago,Date__lte=todays_date)
    finalrep ={}

    def get_Category(addmoney_info):
        # if addmoney_info.add_money=="Expense":
        return addmoney_info.Category    
    Category_list = list(set(map(get_Category,addmoney)))

    def get_expense_category_amount(Category,add_money):
        quantity = 0 
        filtered_by_category = addmoney.filter(Category = Category,add_money="Expense") 
        for item in filtered_by_category:
            quantity+=item.quantity
        return quantity

    for x in addmoney:
        for y in Category_list:
            finalrep[y]= get_expense_category_amount(y,"Expense")

    return JsonResponse({'expense_category_data': finalrep}, safe=False)


def stats(request):
    if request.session.has_key('is_logged') :
        todays_date = datetime.date.today()
        one_month_ago = todays_date-datetime.timedelta(days=30)
        user_id = request.session["user_id"]
        user1 = User.objects.get(id=user_id)
        addmoney_info = Addmoney_info.objects.filter(user = user1,Date__gte=one_month_ago,Date__lte=todays_date)
        sum = 0 
        for i in addmoney_info:
            if i.add_money == 'Expense':
                sum=sum+i.quantity
        addmoney_info.sum = sum
        sum1 = 0 
        for i in addmoney_info:
            if i.add_money == 'Income':
                sum1 =sum1+i.quantity
        addmoney_info.sum1 = sum1
        x= user1.userprofile.Savings+addmoney_info.sum1 - addmoney_info.sum
        y= user1.userprofile.Savings+addmoney_info.sum1 - addmoney_info.sum
        if x<0:
            messages.warning(request,'Your expenses exceeded your savings')
            x = 0
        if x>0:
            y = 0
        addmoney_info.x = abs(x)
        addmoney_info.y = abs(y)
        return render(request,'home/stats.html',{'addmoney':addmoney_info})

def expense_week(request):
    todays_date = datetime.date.today()
    one_week_ago = todays_date-datetime.timedelta(days=7)
    user_id = request.session["user_id"]
    user1 = User.objects.get(id=user_id)
    addmoney = Addmoney_info.objects.filter(user = user1,Date__gte=one_week_ago,Date__lte=todays_date)
    finalrep ={}

    def get_Category(addmoney_info):
        return addmoney_info.Category
    Category_list = list(set(map(get_Category,addmoney)))


    def get_expense_category_amount(Category,add_money):
        quantity = 0 
        filtered_by_category = addmoney.filter(Category = Category,add_money="Expense") 
        for item in filtered_by_category:
            quantity+=item.quantity
        return quantity

    for x in addmoney:
        for y in Category_list:
            finalrep[y]= get_expense_category_amount(y,"Expense")

    return JsonResponse({'expense_category_data': finalrep}, safe=False)
    
def weekly(request):
    if request.session.has_key('is_logged') :
        todays_date = datetime.date.today()
        one_week_ago = todays_date-datetime.timedelta(days=7)
        user_id = request.session["user_id"]
        user1 = User.objects.get(id=user_id)
        addmoney_info = Addmoney_info.objects.filter(user = user1,Date__gte=one_week_ago,Date__lte=todays_date)
        sum = 0 
        for i in addmoney_info:
            if i.add_money == 'Expense':
                sum=sum+i.quantity
        addmoney_info.sum = sum
        sum1 = 0 
        for i in addmoney_info:
            if i.add_money == 'Income':
                sum1 =sum1+i.quantity
        addmoney_info.sum1 = sum1
        x= user1.userprofile.Savings+addmoney_info.sum1 - addmoney_info.sum
        y= user1.userprofile.Savings+addmoney_info.sum1 - addmoney_info.sum
        if x<0:
            messages.warning(request,'Your expenses exceeded your savings')
            x = 0
        if x>0:
            y = 0
        addmoney_info.x = abs(x)
        addmoney_info.y = abs(y)
    return render(request,'home/weekly.html',{'addmoney_info':addmoney_info})

def check(request):
    if request.method == 'POST':
        user_exists = User.objects.filter(email=request.POST['email'])
        messages.error(request,"Email not registered, TRY AGAIN!!!")
        return redirect("/reset_password")

def info_year(request):
    todays_date = datetime.date.today()
    one_week_ago = todays_date-datetime.timedelta(days=30*12)
    user_id = request.session["user_id"]
    user1 = User.objects.get(id=user_id)
    addmoney = Addmoney_info.objects.filter(user = user1,Date__gte=one_week_ago,Date__lte=todays_date)
    finalrep ={}

    def get_Category(addmoney_info):
        return addmoney_info.Category
    Category_list = list(set(map(get_Category,addmoney)))


    def get_expense_category_amount(Category,add_money):
        quantity = 0 
        filtered_by_category = addmoney.filter(Category = Category,add_money="Expense") 
        for item in filtered_by_category:
            quantity+=item.quantity
        return quantity

    for x in addmoney:
        for y in Category_list:
            finalrep[y]= get_expense_category_amount(y,"Expense")

    return JsonResponse({'expense_category_data': finalrep}, safe=False)

def info(request):
    return render(request,'home/info.html')
     


#fityFeed's views
# def home(request):
#     breakfast=Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5]
#     lunch=Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
#     dinner=Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
#     snacks=Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5]
#     customers=Customer.objects.all()
#     context={'breakfast':breakfast,
#               'lunch':lunch,
#               'dinner':dinner,
#               'snacks':snacks,
#               'customers':customers,
#             }
#     return render(request,'main.html',context)

# #@login_required(login_url='login')
# def fooditem(request):
#     breakfast=Category.objects.filter(name='breakfast')[0].fooditem_set.all()
#     bcnt=breakfast.count()
#     lunch=Category.objects.filter(name='lunch')[0].fooditem_set.all()
#     lcnt=lunch.count()
#     dinner=Category.objects.filter(name='dinner')[0].fooditem_set.all()
#     dcnt=dinner.count()
#     snacks=Category.objects.filter(name='snacks')[0].fooditem_set.all()
#     scnt=snacks.count()
#     context={'breakfast':breakfast,
#               'bcnt':bcnt,
#               'lcnt':lcnt,
#               'scnt':scnt,
#               'dcnt':dcnt,
#               'lunch':lunch,
#               'dinner':dinner,
#               'snacks':snacks,
#             }
#     return render(request,'fooditem.html',context)

# #@login_required(login_url='login')
# def createfooditem(request):
#     form = fooditemForm()
#     if request.method == 'POST':
#         form = fooditemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context={'form':form}
#     return render(request,'createfooditem.html',context)

# def registerPage(request):
#     form=createUserForm()
#     if request.method=='POST':
#         form=createUserForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             username=form.cleaned_data.get('username')
#             group=Group.objects.get(name='user')
#             user.groups.add(group)
#             email=form.cleaned_data.get('email')
#             Customer.objects.create(user=user, name=username,email=email)
#             messages.success(request,'Account created for '+username)
#             return redirect('login')
#     context={'form':form}
#     return render(request,'register.html',context)

# def loginPage(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             messages.info(request,'username or password is invalid')
#     return render(request,'login.html')

# #@login_required(login_url='login')
# def logoutUser(request):
#     logout(request)
#     return redirect('login')

# def userPage(request):
#     user=request.user
#     cust=user.customer
#     fooditems=Fooditem.objects.filter()
#     myfilter = fooditemFilter(request.GET,queryset=fooditems)
#     fooditems=myfilter.qs
#     total=UserFooditem.objects.all()
#     myfooditems=total.filter(customer=cust)
#     cnt=myfooditems.count()
#     querysetFood=[]
#     for food in myfooditems:
#         querysetFood.append(food.fooditem.all())
#     finalFoodItems=[]
#     for items in querysetFood:
#         for food_items in items:
#             finalFoodItems.append(food_items)
#     totalCalories=0
#     for foods in finalFoodItems:
#         totalCalories+=foods.calorie
#     CalorieLeft=2000-totalCalories
#     context={'CalorieLeft':CalorieLeft,'totalCalories':totalCalories,'cnt':cnt,'foodlist':finalFoodItems,'fooditem':fooditems,'myfilter':myfilter}
#     return render(request,'user.html',context)

# def addFooditem(request):
#     user=request.user
#     cust=user.customer
#     if request.method=="POST":
#         form =addUserFooditem(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     form=addUserFooditem()
#     context={'form':form}
#     return render(request,'addUserFooditem.html',context)