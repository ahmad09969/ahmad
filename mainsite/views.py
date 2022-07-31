
from django.shortcuts import render
from django.http import  HttpResponseBadRequest
from django.template import loader
from . import models

#هذا الكود هو من أجل عرض صفحة تسجيل الدخول
def show_login(rquest):
    dict = {
        "author_name" : "أحمد عمار الزرعد" ,
        "discripshin" : "صفحة تسجيل الدخول" ,
        "page_title" : "صفحة تسجيل الدخول" ,
    }
    return render(rquest , "mainsite/log_in_page.html" , dict )


#هذا ما سيحدث عندما يقوم المستخدم بتجيل الدخول إلى قسمه
def sign_in(rquest):
    user_name = rquest.POST['user_name']
    password = rquest.POST['password']
    list_user = models.users.objects.all()
    chack_pass = 0 # عدم وجود كلمة سر  مطابقة في قاعدة البيانات
    chak_name = 0 # عدم وجود أسم مطابق في قاعدة البيانات
    for x in list_user :
        if x.full_name == user_name and x.password_user == password:
            dict = {
        "author_name" : "أحمد عمار الزرعد" ,
        "discripshin" : "الصفحة الرأيسية" ,
        "page_title" : "الصفحة الرأيسية" ,
        "password" : password ,
        "user_name" : user_name ,
            }
            return render(rquest , "mainsite/main_page.html" , dict )
        if x.full_name == user_name :
            chak_name = 1 
        if x.password_user == password :
            chack_pass = 1
    if chak_name == 0 :
        return render(rquest , "mainsite/error_page.html" ,
             {"error_massage" : " لا يوجد حساب على موقع أحمد بأسم" + user_name ,})
    elif chak_name == 1 and chack_pass == 0 :
        return render(rquest , "mainsite/error_page.html" ,
             {"error_massage" : "كلمة المرور غير صحيحة",})

    

        

#هذا الكود هو من أجل عرض صفحة أنشاء حساب جديد
def show_logup(request):
    dict = {
        "author_name" : "أحمد عمار الزرعد" ,
        "discripshin" : "صفحة انشاء حساب جديد" ,
        "page_title" : "صفحة انشاء حساب جديد" ,
    }
    return render(request , "mainsite/log_up_page.html" , dict )

#هذا ما سيحدث عندما يقوم المستخدم بأنشاء حساب جديد
def sign_up(rquest):
    user_name = rquest.POST['user_name']
    password = rquest.POST['password']
    list_user = models.users.objects.all()
    for x in list_user :
        if x.full_name == user_name and x.password_user == password:
            return render(rquest , "mainsite/error_page.html" ,
             {"error_massage" : "أسم المستخدم هذا موجد بالفعل في موقع أحمد جرب أسماً آخر" ,})
    dict = {
        "author_name" : "أحمد عمار الزرعد" ,
        "discripshin" : "الصفحة الرأيسية" ,
        "page_title" : "الصفحة الرأيسية" ,
        "password" : password ,
        "user_name" : user_name ,
            }
    new_user = models.users(full_name = user_name , password_user = password )
    new_user.save()
    return render(rquest , "mainsite/main_page.html" , dict )

    
