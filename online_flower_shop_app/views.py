from datetime import datetime, timedelta
from urllib import request

from django.core.files.storage import FileSystemStorage
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from online_flower_shop_app.models import *

# Create your views here.
def public_home(request):
    var=tbl_Itemmaster.objects.all()
    return render(request,'public_pages/public_home.html',{'data':var})

def customer_header2(request):
    return render(request,'customer_pages/customer_header2.html')


def public_login(request):
    if 'Submit' in request.POST:
        username=request.POST['Username']
        password=request.POST['Password']
        qa=tbl_Login.objects.filter(Username=username,Password=password)
        if qa.exists():
            qa1 = tbl_Login.objects.get(Username=username, Password=password)
            request.session['lid']=qa1.id

            if qa1.User_Type == 'admin':
                return HttpResponse("<script>alert('Successfully Login');window.location='/admin_home'</script>")
                # return redirect('/admin_home')
            elif qa1.User_Type == 'Staff':
                return HttpResponse("<script>alert('Successfully Login');window.location='/staff_home'</script>")
            elif qa1.User_Type == 'Customer':
                return HttpResponse("<script>alert('Successfully Login');window.location='/customer_home'</script>")
            # elif qa1.User_Type == 'Customer':
            #     return HttpResponse("<script>alert('Successfully Login');window.location='/courier_home'</script>")

    return render(request,'public_pages/publicindex.html')





def public_signup(request):
    q3=tbl_Customer.objects.all()
    
    if 'Submit' in request.POST:
        Username=request.POST['Username']
        Password=request.POST['Password']
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Gender=request.POST['Gender']
        DOB=request.POST['DOB']
        House=request.POST['House']
        Place=request.POST['Place']
        City=request.POST['City']
        Dist=request.POST['Dist']
        Pin=request.POST['Pin']
        Phone=request.POST['Phone']
        
        q1=tbl_Login(Username=Username,Password=Password,User_Type='Customer',Status='Active')
        q1.save()
        
        q2=tbl_Customer(USERNAME_id=q1.pk,C_Fname=Fname,C_Lname=Lname,C_Gender=Gender,
                     C_DOB=DOB,C_House=House,C_Place=Place,C_City=City,C_Dist=Dist,
                     C_Pin=Pin,C_Phone=Phone,C_Status='Active')
        q2.save()
        
        return HttpResponse("<script>alert('Successfully Stored');window.location='/public_login'</script>")
 
    return render(request,'public_pages/public_signup.html',{'q3':q3})
        

def admin_home(request):
    return render(request,'admin_pages/admin_home.html')

def staff_home(request):
    return render(request,'staff_pages/staff_home.html')

def customer_home(request):
    var=tbl_Itemmaster.objects.all()
    return render(request,'customer_pages/customer_home.html',{'data':var})

def admin_manage_staff(request):
    q3=tbl_Staff.objects.all()
    
    if 'Submit' in request.POST:
        Username=request.POST['Username']
        Password=request.POST['Password']
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Gender=request.POST['Gender']
        DOB=request.POST['DOB']
        House=request.POST['House']
        Place=request.POST['Place']
        City=request.POST['City']
        Dist=request.POST['Dist']
        Pin=request.POST['Pin']
        Phone=request.POST['Phone']
        Photo=request.FILES['Photo']
        a=request.POST['a']

        q1=tbl_Login(Username=Username,Password=Password,User_Type='Staff',Status='Active')
        q1.save()
        q2=tbl_Staff(USERNAME_id=q1.pk,Staff_Fname=Fname,Staff_Lname=Lname,Staff_Gender=Gender,
                     Staff_DOB=DOB,Staff_House=House,Staff_Place=Place,Staff_City=City,Staff_Dist=Dist,
                     Staff_Pin=Pin,Staff_Phone=Phone,Staff_Photo=Photo,Staff_Status='Active',Type=a)
        q2.save()
        
        return HttpResponse("<script>alert('Successfully Stored');window.location='/admin_manage_staff'</script>")
 
    return render(request,'admin_pages/admin_manage_staff.html',{'q3':q3})


def inactive_staff(request,id):
    var=tbl_Staff.objects.filter(id=id).update(Staff_Status='Inactive')
    return HttpResponse("<script>alert('inactived');window.location='/admin_manage_staff'</script>")
#
def active_staff(request,id):
    var=tbl_Staff.objects.filter(id=id).update(Staff_Status='Active')
    return HttpResponse("<script>alert('Active');window.location='/admin_manage_staff'</script>")



def admin_update_staff(request,id):
     q1=tbl_Staff.objects.get(id=id) 
     
     if 'Update' in request.POST:
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Gender=request.POST['Gender']
        DOB=request.POST['DOB']
        House=request.POST['House']
        Place=request.POST['Place']
        City=request.POST['City']
        Dist=request.POST['Dist']
        Pin=request.POST['Pin']
        Phone=request.POST['Phone']

        if 'Photo' in request.FILES:
            Photo = request.FILES['Photo']
            date=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.jpg'
            fs=FileSystemStorage()
            fs.save(date,Photo)
            path=fs.url(date)
            q1.Staff_Photo = path

        q1.Staff_Fname=Fname
        q1.Staff_Lname=Lname
        q1.Staff_Gender=Gender
        q1.Staff_DOB=DOB
        q1.Staff_House=House
        q1.Staff_Place=Place
        q1.Staff_City=City
        q1.Staff_Dist=Dist
        q1.Staff_Pin=Pin
        q1.Staff_Phone=Phone

        q1.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/admin_manage_staff'</script>")
       
     return render(request,'admin_pages/admin_manage_staff.html',{'q1':q1})


def admin_manage_vendor(request):
    
    a3=tbl_Vendor.objects.all()
    
    if 'Submit' in request.POST:
        Vname=request.POST['Vname']
        Vemail=request.POST['Vemail']
        Place=request.POST['Place']
        Dist=request.POST['Dist']
        Pin=request.POST['Pin']
        Phone=request.POST['Phone']
        
        a1=tbl_Vendor(V_name=Vname,V_Email=Vemail,V_Place=Place,V_Dist=Dist,V_Pin=Pin,V_Phone=Phone,V_Status='Active',LOGIN_id=1)
        a1.save()
        
        return HttpResponse("<script>alert('Successfully Stored');window.location='/admin_manage_vendor'</script>")
        
    return render(request,'admin_pages/admin_manage_vendor.html',{'a3':a3})

def admin_update_vendor(request,id):
     q1=tbl_Vendor.objects.get(id=id) 
     
     if 'Update' in request.POST:
        Vname=request.POST['Vname']
        Vemail=request.POST['Vemail']
        Place=request.POST['Place']
        Dist=request.POST['Dist']
        Pin=request.POST['Pin']
        Phone=request.POST['Phone']
        
        q1.V_name=Vname
        q1.V_Email=Vemail
        q1.V_Place=Place
        q1.V_Dist=Dist
        q1.V_Pin=Pin
        q1.V_Phone=Phone
        
        q1.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/admin_manage_vendor'</script>")
       
     return render(request,'admin_pages/admin_manage_vendor.html',{'q1':q1})


def admin_manage_category(request):
    
    a6=tbl_Category.objects.all()
    
    if 'Submit' in request.POST:
        Catname=request.POST['Catname']
        Catdesc=request.POST['Catdesc']
        
        a5=tbl_Category(Cat_Name=Catname,Cat_Desc=Catdesc)
        a5.save()
        
        return HttpResponse("<script>alert('Successfully Stored');window.location='/admin_manage_category'</script>")
        
    return render(request,'admin_pages/admin_manage_category.html',{'a6':a6})
 
 
def admin_update_category(request,id):
    q1=tbl_Category.objects.get(id=id) 
     
    if 'Update' in request.POST:
        Catname=request.POST['Catname']
        Catdesc=request.POST['Catdesc']
        
        q1.Cat_Name=Catname
        q1.Cat_Desc=Catdesc
        
        q1.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/admin_manage_category'</script>")
       
    return render(request,'admin_pages/admin_manage_category.html',{'q1':q1})


from django.http import HttpResponse
from django.shortcuts import render
from .models import tbl_Itemmaster, tbl_Itemchild, tbl_Flower, tbl_Category


# def admin_manage_item(request):
#     a3 = tbl_Itemmaster.objects.all()
#     a2 = tbl_Category.objects.all()
#     a1 = tbl_Flower.objects.all()
#
#     if 'Submit' in request.POST:
#         Itemname = request.POST['Itemname']
#         Itemdesc = request.POST['Itemdesc']
#         Itemimg = request.FILES['Itemimg']
#         Price = request.POST['Price']
#         Profit = request.POST['Profit']
#         Category = request.POST['Category']
#         Flower = request.POST.getlist('flower')
#
#         q2 = tbl_Itemmaster(Item_Name=Itemname, Item_Cost=Price, Item_Img=Itemimg, Stock=1, CAT_id=Category,
#                             Item_Status='Active', Item_Desc=Itemdesc, Profit_Per=Profit)
#         q2.save()
#
#         for i in Flower:
#             q1 = tbl_Itemchild(FLOWER_id=i, ITEM_id=q2.id)
#             q1.save()
#
#         return HttpResponse("<script>alert('Successfully Stored');window.location='/admin_manage_item'</script>")
#     return render(request, 'admin_pages/admin_manage_item.html', {'a3': a3, 'a2': a2})


def admin_manage_item(request):
    a3 = tbl_Itemmaster.objects.all()
    a2 = tbl_Category.objects.all()
    a1 = tbl_Flower.objects.all()

    if 'Submit' in request.POST:
        Itemname = request.POST['Itemname']
        Itemdesc = request.POST['Itemdesc']
        Itemimg = request.FILES['Itemimg']
        Price = request.POST['Price']
        Profit = request.POST['Profit']
        Category = request.POST['Category']
        Flower = request.POST.getlist('flower')

        # var=tbl_Category.objects.get(id=Category)


        q2 = tbl_Itemmaster(Item_Name=Itemname, Item_Cost=Price, Item_Img=Itemimg, Stock=1, CAT_id=Category,
                            Item_Status='Active', Item_Desc=Itemdesc, Profit_Per=Profit)
        q2.save()

        for i in Flower:
            q1 = tbl_Itemchild(FLOWER_id=i, ITEM_id=q2.pk)
            q1.save()
            print(i)
        return HttpResponse("<script>alert('Successfully Stored');window.location='/admin_manage_item'</script>")
    return render(request, 'admin_pages/admin_manage_item.html', {'a3': a3, 'a2': a2, 'a1': a1})




def active_item(request,id):
    var=tbl_Itemmaster.objects.filter(id=id).update(Item_Status="Active")
    return HttpResponse("<script>alert('Active');window.location='/admin_manage_item'</script>")

def deactive_item(request,id):
    var=tbl_Itemmaster.objects.filter(id=id).update(Item_Status="Deactive")
    return HttpResponse("<script>alert('Deactive');window.location='/admin_manage_item'</script>")


def add_flower(request,id):
    a1=tbl_Flower.objects.all()


    if 'Submit' in request.POST:
        fid=request.POST['Flower']
        a=tbl_Itemchild.objects.filter(FLOWER_id=fid,ITEM_id=id)
        if a.exists():
            return HttpResponse("<script>alert('Already Added');window.location='/admin_manage_item'</script>")

        a2=tbl_Itemchild(FLOWER_id=fid,ITEM_id=id)
        a2.save()
        return HttpResponse("<script>alert('Successfully added');window.location='/admin_manage_item'</script>")
        # return HttpResponse("<script>alert('Successfully added');window.location='/add_flower/{id}'</script>")

    return render(request,'admin_pages/add_flower.html',{'a1':a1})


def admin_update_item(request,id):
    q1=tbl_Itemmaster.objects.get(id=id) 
    q2=tbl_Category.objects.all() 
    q3=tbl_Flower.objects.all()
     
    if 'Update' in request.POST:
        try:
            Itemname=request.POST['Itemname']
            Itemdesc=request.POST['Itemdesc']
            Itemimg=request.FILES['Itemimg']
            Price=request.POST['Price']
            Profit=request.POST['Profit']
            Category=request.POST['Category']
            Flower=request.POST.getlist('flower')
            
            q1.Item_Name=Itemname
            q1.Item_Desc=Itemdesc
            q1.Item_Img=Itemimg
            q1.Item_Cost=Price
            q1.Profit_Per=Profit
            q1.CAT_id=Category
            q1.FLOWER_id=Flower
            
            q1.save()
            
        except:
            Itemname=request.POST['Itemname']
            Itemdesc=request.POST['Itemdesc']
            Price=request.POST['Price']
            Profit=request.POST['Profit']
            Category=request.POST['Category']
            Flower=request.POST.getlist('flower')
            
            q1.Item_Name=Itemname
            q1.Item_Desc=Itemdesc
            q1.Item_Cost=Price
            q1.Profit_Per=Profit
            q1.CAT_id=Category
            q1.FLOWER_id=Flower
            
            q1.save()
            
        return HttpResponse("<script>alert('Successfully Updated');window.location='/admin_manage_item'</script>")
       
    return render(request,'admin_pages/admin_manage_item.html',{'q1':q1,'q2':q2,'q3':q3})

def item_view_more(request,id):
    print(id,'////////////////////////')
    
    q1=tbl_Itemchild.objects.filter(ITEM_id=id)
    
    return render(request,'admin_pages/item_view_more.html',{'q1':q1})

def admin_manage_flower(request):
     a3=tbl_Flower.objects.all()
    
     if 'Submit' in request.POST:
        Flowername=request.POST['Flowername']
        Color=request.POST['Color']
        Flowerimg=request.FILES['Flowerimg']
        Type=request.POST['Type']
        
        a1=tbl_Flower(Flower_Name=Flowername,Color=Color,Img=Flowerimg,Type=Type,Flower_Status='Active')
        a1.save()
        
        return HttpResponse("<script>alert('Successfully Stored');window.location='/admin_manage_flower'</script>")
    
     return render(request,'admin_pages/admin_manage_flower.html',{'a3':a3})
 
 
def admin_update_flower(request,id):
    q1=tbl_Flower.objects.get(id=id) 
     
    if 'Update' in request.POST:
        Flowername=request.POST['Flowername']
        Color=request.POST['Color']
        Flowerimg=request.FILES['Flowerimg']
        Type=request.POST['Type']
        
        q1.Flower_Name=Flowername
        q1.Color=Color
        q1.Img=Flowerimg
        q1.Type=Type
        
        q1.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/admin_manage_flower'</script>")
       
    return render(request,'admin_pages/admin_manage_flower.html',{'q1':q1})


def admin_view_customer(request):
    a3=tbl_Customer.objects.all()
    return render(request,'admin_pages/admin_view_customer.html',{'a3':a3})

def admin_view_order(request):
    a3=tbl_Order.objects.all()
    return render(request,'admin_pages/admin_view_orders.html',{'data':a3})




def admin_view_order_more(request,id):
    a=tbl_Cartmaster.objects.get(id=id)
    b=tbl_Cartchild.objects.filter(CARTMAST_id=id)
    var=tbl_Order.objects.filter(CARTMAST_id=id)
    l=[]
    # for i in b:
    #     if cart_child_customization.objects.filter(CART_CHILD_id=i.id).exists():

    return render(request, 'admin_pages/admin_view_order_more.html', {'data': var,'a':a,'b':b})


def admin_view_customization(request,id):
    var = cart_child_customization.objects.filter(CART_CHILD_id=id)
    if var.exists():

        if 'submit' in request.POST:
            id = request.POST.getlist('id')
            amount = request.POST.getlist('amount')
            for i in range(len(id)):
                a = cart_child_customization.objects.get(id=id[i])
                a.Add_Amt = amount[i]
                a.save()
                return HttpResponse(
                    "<script>alert('Successfully Updated');window.location='/admin_view_order'</script>")

        return render(request, 'admin_pages/view customization.html', {'data': var})
    else:
        return HttpResponse("<script>alert('Nothing Here....');window.location='/admin_view_order'</script>")





def admin_view_purchase(request):
    a3=tbl_Purchild.objects.all()
    return render(request,'admin_pages/admin_view_purchase.html',{'data':a3})

def admin_view_review(request):
    a3=tbl_Review.objects.all()
    return render(request,'admin_pages/admin_view_review.html',{'a3':a3})

def staff_manage_vendor(request):
    
    a3=tbl_Vendor.objects.all()
    
    if 'Submit' in request.POST:
        Vname=request.POST['Vname']
        Vemail=request.POST['Vemail']
        Place=request.POST['Place']
        Dist=request.POST['Dist']
        Pin=request.POST['Pin']
        Phone=request.POST['Phone']
        
        a1=tbl_Vendor(V_name=Vname,V_Email=Vemail,V_Place=Place,V_Dist=Dist,V_Pin=Pin,V_Phone=Phone,V_Status='Active',STAFF_id=1)
        a1.save()
        
        return HttpResponse("<script>alert('Successfully Stored');window.location='/staff_manage_vendor'</script>")
        
    return render(request,'staff_pages/staff_manage_vendor.html',{'a3':a3})





def staff_update_vendor(request,id):
     q8=tbl_Vendor.objects.get(id=id) 
     
     if 'Update' in request.POST:
        Vname=request.POST['Vname']
        Vemail=request.POST['Vemail']
        Place=request.POST['Place']
        Dist=request.POST['Dist']
        Pin=request.POST['Pin']
        Phone=request.POST['Phone']
        
        q8.V_name=Vname
        q8.V_Email=Vemail
        q8.V_Place=Place
        q8.V_Dist=Dist
        q8.V_Pin=Pin
        q8.V_Phone=Phone
        
        q8.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/staff_manage_vendor'</script>")
       
     return render(request,'staff_pages/staff_manage_vendor.html',{'q8':q8})
  

def staff_view_customer(request):
    a3=tbl_Customer.objects.all()
    return render(request,'staff_pages/staff_view_customer.html',{'a3':a3})


def staff_manage_category(request):
    
    a6=tbl_Category.objects.all()
    
    if 'submit' in request.POST:
        Catname=request.POST['Catname']
        Catdesc=request.POST['Catdesc']
        
        a5=tbl_Category(Cat_Name=Catname,Cat_Desc=Catdesc)
        a5.save()
        
        return HttpResponse("<script>alert('Successfully Stored');window.location='/staff_manage_category'</script>")
        
    return render(request,'staff_pages/staff_manage_category.html',{'a6':a6})

def staff_update_category(request,id):
    q0=tbl_Category.objects.get(id=id) 
     
    if 'Update' in request.POST:
        Catname=request.POST['Catname']
        Catdesc=request.POST['Catdesc']
        
        q0.Cat_Name=Catname
        q0.Cat_Desc=Catdesc
        
        q0.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/staff_manage_category'</script>")
       
    return render(request,'staff_pages/staff_manage_category.html',{'q0':q0})


def staff_manage_flower(request):
    
    a3=tbl_Flower.objects.all()
    
    if 'Submit' in request.POST:
        Flowername=request.POST['Flowername']
        Color=request.POST['Color']
        Flowerimg=request.FILES['Flowerimg']
        Type=request.POST['Type']
        
        a1=tbl_Flower(Flower_Name=Flowername,Color=Color,Img=Flowerimg,Type=Type,Flower_Status='1')
        a1.save()
        
        return HttpResponse("<script>alert('Successfully Stored');window.location='/staff_manage_flower'</script>")
    
    return render(request,'staff_pages/staff_manage_flower.html',{'a3':a3})

  
def staff_update_flower(request,id):
    q6=tbl_Flower.objects.get(id=id) 
     
    if 'Update' in request.POST:
        Flowername=request.POST['Flowername']
        Color=request.POST['Color']
        Flowerimg=request.FILES['Flowerimg']
        Type=request.POST['Type']
        
        q6.Flower_Name=Flowername
        q6.Color=Color
        q6.Img=Flowerimg
        q6.Type=Type
        
        q6.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/staff_manage_flower'</script>")
       
    return render(request,'staff_pages/staff_manage_flower.html',{'q6':q6})

def staff_manage_item(request):
    
    a3=tbl_Itemmaster.objects.all()
    a2=tbl_Category.objects.all()
    a1=tbl_Flower.objects.all()
    
    if 'Submit' in request.POST:
        Itemname=request.POST['Itemname']
        Itemdesc=request.POST['Itemdesc']
        Itemimg=request.FILES['Itemimg']
        Price=request.POST['Price']
        Profit=request.POST['Profit']
        Category=request.POST['Category']
        Flower=request.POST.getlist('flower')

        # var=tbl_Category.objects.get(id=Category)
        
        
        q2=tbl_Itemmaster(Item_Name=Itemname,Item_Cost=Price,Item_Img=Itemimg,Stock=1,CAT_id=Category,Item_Status='Active',Item_Desc=Itemdesc,Profit_Per=Profit)
        q2.save()
        
        for i in Flower:
            q1=tbl_Itemchild(FLOWER_id=i,ITEM_id=q2.pk)
            q1.save()
            print(i)
        return HttpResponse("<script>alert('Successfully Stored');window.location='/staff_manage_item'</script>")
    return render(request,'staff_pages/staff_manage_item.html',{'a3':a3,'a2':a2,'a1':a1})


def staff_manage_item(request):
    a3 = tbl_Itemmaster.objects.all()
    a2 = tbl_Category.objects.all()
    a1 = tbl_Flower.objects.all()

    if 'Submit' in request.POST:
        Itemname = request.POST['Itemname']
        Itemdesc = request.POST['Itemdesc']
        Itemimg = request.FILES['Itemimg']
        Price = request.POST['Price']
        Profit = request.POST['Profit']
        Category = request.POST['Category']
        Flower = request.POST.getlist('flower')

        # var=tbl_Category.objects.get(id=Category)



        q2 = tbl_Itemmaster(Item_Name=Itemname, Item_Cost=Price, Item_Img=Itemimg, Stock=1, CAT_id=Category,
                            Item_Status='Active', Item_Desc=Itemdesc, Profit_Per=Profit)
        q2.save()

        for i in Flower:
            q1 = tbl_Itemchild(FLOWER_id=i, ITEM_id=q2.pk)
            q1.save()
            print(i)
            print(q1)



        return HttpResponse("<script>alert('Successfully Stored');window.location='/staff_manage_item'</script>")
    return render(request, 'staff_pages/staff_manage_item.html', {'a3': a3, 'a2': a2, 'a1': a1})





def staff_active_item(request,id):
    var=tbl_Itemmaster.objects.filter(id=id).update(Item_Status="Active")
    return HttpResponse("<script>alert('Active');window.location='/staff_manage_item'</script>")

def staff_deactive_item(request,id):
    var=tbl_Itemmaster.objects.filter(id=id).update(Item_Status="Deactive")
    return HttpResponse("<script>alert('Deactive');window.location='/staff_manage_item'</script>")














def staff_update_item(request,id):
    q6=tbl_Itemmaster.objects.get(id=id) 
    q7=tbl_Category.objects.all() 
    q8=tbl_Flower.objects.all()
     
    if 'Update' in request.POST:
        try:
            Itemname=request.POST['Itemname']
            Itemdesc=request.POST['Itemdesc']
            Itemimg=request.FILES['Itemimg']
            Price=request.POST['Price']
            Profit=request.POST['Profit']
            Category=request.POST['Category']
            Flower=request.POST.getlist('flower')
            
            q6.Item_Name=Itemname
            q6.Item_Desc=Itemdesc
            q6.Item_Img=Itemimg
            q6.Item_Cost=Price
            q6.Profit_Per=Profit
            q6.CAT_id=Category
            q6.FLOWER_id=Flower
            
            q6.save()
        
        except:
            Itemname=request.POST['Itemname']
            Itemdesc=request.POST['Itemdesc']
            Price=request.POST['Price']
            Profit=request.POST['Profit']
            Category=request.POST['Category']
            Flower=request.POST.getlist('flower')
            
            q6.Item_Name=Itemname
            q6.Item_Desc=Itemdesc
            q6.Item_Cost=Price
            q6.Profit_Per=Profit
            q6.CAT_id=Category
            q6.FLOWER_id=Flower
            
            q6.save()
            
        return HttpResponse("<script>alert('Successfully Updated');window.location='/staff_manage_item'</script>")
       
    return render(request,'staff_pages/staff_manage_item.html',{'q6':q6,'q7':q7,'q8':q8})


def staff_item_view_more(request,id):
    print(id,'////////////////////////')
    
    q1=tbl_Itemchild.objects.filter(ITEM_id=id)
    q2_list = []
    
    for i in q1:
        print(i)
        q2 = tbl_Flower.objects.get(id=i.FLOWER_id)
        q2_list.append(q2)
        if q2_list:
        
            return render(request,'staff_pages/staff_item_view_more.html',{'q2_list':q2_list})
    return render(request,'staff_pages/staff_item_view_more.html')



def staff_view_review(request):
    a3=tbl_Review.objects.all()
    return render(request,'staff_pages/staff_view_review.html',{'a3':a3})



def staff_view_purchase(request):
    var=tbl_Purchild.objects.all()
    return render(request,'staff_pages/staff_view_purchase.html',{'data':var})


def staff_view_order(request):
    var=tbl_Order.objects.all()
    return render(request,'staff_pages/staff_view_orders.html',{'data':var})

def staff_update_order(request,id):
    var=tbl_Order.objects.filter(id=id).update(Order_Status='Delivered')
    return HttpResponse("<script>alert('Delivered');window.location='/staff_view_order'</script>")


def customer_manage_review(request,id):
    var=tbl_Order.objects.get(id=id)

    if 'submit' in request.POST:
        id=request.POST['id']
        review=request.POST['review']
        var=tbl_Review()
        var.CUSTOMER=tbl_Customer.objects.get(USERNAME_id=request.session['lid'])
        var.ORDER=tbl_Order.objects.get(id=id)
        var.Review_Desc=review
        var.save()
        return HttpResponse("<script>alert('Successfully ');window.location='/customer_home'</script>")




    return render(request,'customer_pages/customer_manage_review.html',{'data':var})

def bill(request,id):
    q = tbl_Order.objects.get(id=id)
    qt = tbl_Payment.objects.get(ORDER_id=id)
    qi = tbl_Cartchild.objects.filter(CARTMAST_id=q.CARTMAST_id)
    return render(request, 'customer_pages/bill.html', {'q': q, 'qi': qi, 'qt': qt})




def customer_view_orders(request):
    var=tbl_Order.objects.filter(CARTMAST__CUSTOMER__USERNAME_id=request.session['lid'],Order_Status='ordered')
    return render(request,'customer_pages/customer_view_orders.html',{'data':var})

def customer_view_profile(request):
    var=tbl_Customer.objects.get(USERNAME_id=request.session['lid'])
    return render(request,'customer_pages/customer_view_profile.html',{'data':var})



def edit_profile(request):
    var=tbl_Customer.objects.get(USERNAME_id=request.session['lid'])

    if 'submit' in request.POST:
        first=request.POST['first']
        last=request.POST['last']
        # dob=request.POST['dob']
        phone=request.POST['phone']
        house=request.POST['house']
        place=request.POST['place']
        city=request.POST['city']
        district=request.POST['district']
        pin=request.POST['pin']


        a=tbl_Customer.objects.get(USERNAME_id=request.session['lid'])
        a. C_Fname=first
        a.C_Lname=last
        a.C_House=house
        a.C_City=city
        a.C_Dist=district
        a.C_Pin=pin
        a.C_Place=place
        a.C_Phone=phone
        # a.C_DOB=dob
        a.save()
        return HttpResponse("<script>alert('Successfully Updated');window.location='/customer_view_profile'</script>")

    return render(request,'customer_pages/edit_profile.html',{'data':var})


def customer_view_products(request):
    categories = tbl_Category.objects.all()
    items = tbl_Itemmaster.objects.all()

    if 'submit' in request.POST:
        name = request.POST['category']
        items = tbl_Itemmaster.objects.filter(CAT_id=name)

        return render(request, 'customer_pages/customer_view_products.html', {'items': items, 'categories': categories})

    return render(request, 'customer_pages/customer_view_products.html', {'items': items, 'categories': categories})






def customer_cart(request):
    if tbl_Cartchild.objects.filter(CARTMAST__CUSTOMER__USERNAME_id=request.session['lid'],CARTMAST__Cart_Status='pending').exists():
        var=tbl_Cartchild.objects.filter(CARTMAST__CUSTOMER__USERNAME_id=request.session['lid'],
                                         CARTMAST__Cart_Status='pending')
        cd=tbl_Cartmaster.objects.get(CUSTOMER__USERNAME_id=request.session['lid'],Cart_Status='pending')

        return render(request,'customer_pages/customer_cart.html',{'data':var,'data2':cd})
    else:
        return HttpResponse("<script>alert('No Product in cart');window.location='/customer_home'</script>")



# def add_cart(request,id):
#     q=tbl_Itemmaster.objects.get(id=id)
#     amount=q.Item_Cost
#     if tbl_Cartmaster.objects.filter(CUSTOMER__USERNAME_id=request.session['lid'],Cart_Status='pending').exists():
#         f=tbl_Cartmaster.objects.get(CUSTOMER__USERNAME_id=request.session['lid'],Cart_Status='pending')
#
#
#         if tbl_Cartchild.objects.filter(CARTMAST_id=f.pk,ITEM_id=id).exists():
#              return HttpResponse("<script>alert('Already in cart');window.location='/customer_view_products';</script>")
#         else:
#             ff=tbl_Cartchild(Cart_Quantity=1,CARTMAST_id=f.pk,ITEM_id=id)
#             ff.save()
#             f.Total_Amount = str(int(f.Tot_Amount) + int(amount))
#             print(f)
#             f.save()
#             return HttpResponse("<script>alert('success');window.location='/customer_cart';</script>")
#     else:
#         # qi=tbl_Cart_Master(Total_Amount=amount,Cart_Status='pending',CUSTOMER__USERNAME_id=request.session['lid'])
#         qi=tbl_Cartmaster(Tot_Amount=amount,Cart_Status='pending',CUSTOMER_id=request.session['lid'])
#         qi.save()
#         qt=tbl_Cartchild(Cart_Quantity=1,CARTMAST_id=qi.pk,ITEM_id=id)
#         qt.save()
#         return HttpResponse("<script>alert('success Added');window.location='/customer_cart';</script>")
#
#

#
# def remove_cart(request, id):
#     cart_item = tbl_Cartchild.objects.get(id=id)
#     cart_master = cart_item.CARTMAST
#
#     amount = int(cart_item.ITEM.Item_Cost) * int(cart_item.Cart_Quantity)
#
#     cart_master.Tot_Amount = str(int(cart_master.Tot_Amount) - int(str(amount)))
#     cart_master.save()
#
#     cart_item.delete()
#
#     if cart_master.cartchild_set.count() == 0:
#         cart_master.delete()
#
        # return HttpResponse("<script>alert('Successfully Removed');window.location='/customer_cart'</script>")
#     # except tbl_Cartchild.DoesNotExist:
#     #     return HttpResponse("<script>alert('Successfully Stored');window.location='/customer_cart'</script>")
#     # except Exception as e:
#         return HttpResponse("<script>alert('Successfully Stored');window.location='/customer_cart'</script>")


from django.http import HttpResponse
from .models import tbl_Cartchild


def remove_cart(request, id):
    try:
        cart_item = tbl_Cartchild.objects.get(id=id)
        cart_master = cart_item.CARTMAST

        amount = int(cart_item.ITEM.Item_Cost) * int(cart_item.Cart_Quantity)

        # Update the total amount in the cart master
        cart_master.Tot_Amount = str(int(cart_master.Tot_Amount) - amount)
        cart_master.save()

        # Delete the cart item
        cart_item.delete()
        return HttpResponse("<script>alert('Successfully Removed');window.location='/customer_cart';</script>")

        # If there are no more items in the cart, delete the cart master as well
        if cart_master.cartchild_set.count() == 0:
            cart_master.delete()
            return HttpResponse("<script>alert('Successfully Removed');window.location='/customer_cart';</script>")


    # except tbl_Cartchild.DoesNotExist:
    #     return HttpResponse('''<script>alert('Removed');window.location='/customer_cart'</script>''')


    except Exception as e:
        return HttpResponse(f"<script>alert('An error occurred: {e}');window.location='/customer_cart'</script>")


def increase_qty(request, id):
    q = tbl_Cartchild.objects.get(id=id)
    q.Cart_Quantity = str(int(q.Cart_Quantity) + 1)
    q.save()

    cid = q.CARTMAST_id
    qi = tbl_Cartmaster.objects.get(id=cid)

    # Convert Item_Cost to float before adding to Tot_Amount
    qi.Tot_Amount = str(float(qi.Tot_Amount) + float(q.ITEM.Item_Cost))
    qi.save()

    return HttpResponse("<script>window.location='/customer_cart'</script>")

# def increase_qty(request, id):
#     q = tbl_Cartchild.objects.get(id=id)
#     q.Cart_Quantity = str(int(q.Cart_Quantity) + 1)
#     q.save()
#
#     cid = q.CARTMAST_id
#     qi = tbl_Cartmaster.objects.get(id=cid)
#     qi.Tot_Amount = str(int(qi.Tot_Amount) + int(q.ITEM.Item_Cost))
#     qi.save()
#     return HttpResponse("<script>window.location='/customer_cart'</script>")

#
# def decrease(request, id):
#     try:
#         # Get the cart item
#         cart_item = tbl_Cartchild.objects.get(id=id)
#
#         # Check if the quantity is already 1
#         if int(cart_item.Cart_Quantity) > 1:
#             # If quantity is greater than 1, decrease it
#             cart_item.Cart_Quantity = str(int(cart_item.Cart_Quantity) - 1)
#             cart_item.save()
#
#             # Update the total amount in the cart master
#             cart_master = tbl_Cartmaster.objects.get(id=cart_item.CARTMAST_id)
#             cart_master.Tot_Amount = str(int(cart_master.Tot_Amount) - int(cart_item.ITEM.Item_Cost))
#             cart_master.save()
#
#         return HttpResponse("<script>window.location='/customer_cart'</script>")
#
#     except tbl_Cartchild.DoesNotExist:
#         return HttpResponse("<script>alert('Cart item does not exist');window.location='/customer_cart'</script>")
#
#     except Exception as e:
#         return HttpResponse("<script>alert('An error occurred');window.location='/customer_cart'</script>")



# def decrease(request, id):
#     q = tbl_Cartchild.objects.get(id=id)
#     q.Cart_Quantity = str(int(q.Cart_Quantity) - 1)
#     q.save()
#
#     cid = q.CARTMAST_id
#     qi = tbl_Cartmaster.objects.get(id=cid)
#
#     # Convert Item_Cost to float before adding to Tot_Amount
#     qi.Tot_Amount = str(float(qi.Tot_Amount) - float(q.ITEM.Item_Cost))
#     qi.save()
#
#     return HttpResponse("<script>window.location='/customer_cart'</script>")
#

from django.http import HttpResponse
from .models import tbl_Cartchild, tbl_Cartmaster

def decrease(request, id):
    q = tbl_Cartchild.objects.get(id=id)

    # Check if the quantity is already 1 before decreasing
    if int(q.Cart_Quantity) > 1:
        q.Cart_Quantity = str(int(q.Cart_Quantity) - 1)
        q.save()

        cid = q.CARTMAST_id
        qi = tbl_Cartmaster.objects.get(id=cid)

        # Convert Item_Cost to float before subtracting from Tot_Amount
        qi.Tot_Amount = str(float(qi.Tot_Amount) - float(q.ITEM.Item_Cost))
        qi.save()

    return HttpResponse("<script>window.location='/customer_cart'</script>")






from django.db.models import Max
from django.utils import timezone
#
# def order_fill(request, id):
#     q = tbl_Cartmaster.objects.get(id=id)
#     amount = q.Tot_Amount
#     q.Cart_Status = 'pending'
#     q.save()
#
#     if 'submit' in request.POST:
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         city = request.POST['city']
#         house = request.POST['house']
#         district = request.POST['district']
#         pincode = request.POST['pincode']
#         place = request.POST['place']
#         phone = request.POST['phone']
#
#         latest_bill_no = tbl_Order.objects.aggregate(Max('Bill_No'))['Bill_No__max']
#         if latest_bill_no is None:
#             latest_bill_no = 1000
#         else:
#             try:
#                 latest_bill_no = int(latest_bill_no)
#             except ValueError:
#                 latest_bill_no = 1000
#
#         new_bill_no = str(latest_bill_no + 1)
#
#         q = tbl_Order(
#             A_Fname=fname, A_Lname=lname, A_City=city, A_House=house, A_Dist=district, A_Pin=pincode,
#             A_Place=place, A_Phone=phone, Order_Status='Ordered', Order_Date=timezone.now().date(),
#             Order_Total=amount, Bill_No=new_bill_no, CARTMAST_id=id
#         )
#         q.save()
#         id2 = q.pk
#         return HttpResponse("<script>alert('ordered');window.location='/payment'</script>")
#
#     return render(request, 'customer_pages/order_page.html')



def order_fill(request, id):
    q = tbl_Cartmaster.objects.get(id=id)
    amount = q.Tot_Amount
    q.Cart_Status = 'ordered'
    q.save()

    if 'submit' in request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        city = request.POST['city']
        house = request.POST['house']
        district = request.POST['district']
        pincode = request.POST['pincode']
        place = request.POST['place']
        phone = request.POST['phone']



        latest_bill_no = tbl_Order.objects.aggregate(Max('Bill_No'))['Bill_No__max']
        if latest_bill_no is None:
            latest_bill_no = 1000
        else:
            try:
                latest_bill_no=int(latest_bill_no)
            except:
                latest_bill_no=1000

        new_bill_no = int(latest_bill_no) + int(1)

        q = tbl_Order(
            A_Fname=fname, A_Lname=lname, A_City=city, A_House=house, A_Dist=district, A_Pin=pincode,
            A_Place=place, A_Phone=phone, Order_Status='ordered', Order_Date=datetime.now().date(),
            Order_Total=amount, Bill_No=new_bill_no, CARTMAST_id=id
        )
        q.save()
        id2 = q.pk
        return HttpResponse(f"<script>alert('ordered');window.location='/payment/{id2}'</script>")
        # return HttpResponse(f"<script>alert('ordered');window.location='/payment'</script>")

    return render(request, 'customer_pages/order_page.html')












from django.http import HttpResponse
from .models import tbl_Itemmaster, tbl_Cartmaster, tbl_Cartchild

def add_cart(request, id):
    try:
        item = tbl_Itemmaster.objects.get(id=id)
        amount = item.Item_Cost

        if tbl_Cartmaster.objects.filter(CUSTOMER__USERNAME_id=request.session['lid'], Cart_Status='pending').exists():
            cart_master = tbl_Cartmaster.objects.get(CUSTOMER__USERNAME_id=request.session['lid'], Cart_Status='pending')

            if tbl_Cartchild.objects.filter(CARTMAST_id=cart_master.pk, ITEM_id=id).exists():
                return HttpResponse("<script>alert('Item already in cart');window.location='/customer_view_products';</script>")
            else:
                cart_item = tbl_Cartchild.objects.create(Cart_Quantity=1, CARTMAST_id=cart_master.pk, ITEM_id=id)
                cart_master.Tot_Amount = str(int(cart_master.Tot_Amount) + int(amount))
                cart_master.save()
                return HttpResponse("<script>alert('Item added to cart');window.location='/customer_cart';</script>")
        else:
            cart_master = tbl_Cartmaster.objects.create(Tot_Amount=amount, Cart_Status='pending', CUSTOMER_id=request.session['lid'])
            cart_item = tbl_Cartchild.objects.create(Cart_Quantity=1, CARTMAST_id=cart_master.pk, ITEM_id=id)
            return HttpResponse("<script>alert('Item added to cart');window.location='/customer_cart';</script>")
    except tbl_Itemmaster.DoesNotExist:
        return HttpResponse("<script>alert('Item does not exist');window.location='/customer_view_products';</script>")
    except Exception as e:
        return HttpResponse("<script>alert('Error occurred');window.location='/customer_view_products';</script>")









# 20-2-24
def payment(request, id):
    s = tbl_Order.objects.get(id=id)
    f = None
    if tbl_Card.objects.filter(CUSTOMER__USERNAME_id=request.session['lid']).exists():
        f = tbl_Card.objects.filter(CUSTOMER__USERNAME_id=request.session['lid']).latest('id')

    if 'submit' in request.POST:
        dd = id
        cardno = request.POST.get('cardno')
        holdername = request.POST.get('holdername')
        expdate = request.POST.get('expdate')

        if not f:
            f = tbl_Card(Card_No=cardno, Card_Holdername=holdername, Expiry_Date=expdate,
                         CUSTOMER__USERNAME_id=request.session['lid'])
            f.save()

        qi = tbl_Payment(Payment_Date=datetime.now().date(), Payment_Status='Paid', CARD_id=f.pk, ORDER_id=id)
        qi.save()
        return HttpResponse(f"<script>alert('payment successful');window.location='/cust_view_bill/{dd}'</script>")

    return render(request, 'customer_pages/card_payment.html', {'f': f, 's': s})








from django.shortcuts import render, HttpResponse, redirect
from .models import tbl_Order, tbl_Card, tbl_Payment
# from .forms import PaymentForm  # Import the form for card details
from datetime import datetime










def cust_view_bill(request,id):
    q=tbl_Order.objects.get(id=id)
    qt=tbl_Payment.objects.get(ORDER_id=id)
    qi=tbl_Cartchild.objects.filter(CARTMAST_id=q.CARTMAST_id)
    return render(request,'customer_pages/cust_view_bill.html',{'q':q,'qi':qi,'qt':qt})






def customer_cart_customization(request, id):
    request.session["item_id"]=id
    var = tbl_Itemmaster.objects.filter(id=id)
    var2=tbl_Itemchild.objects.filter(ITEM_id=id)



    if 'submit' in request.POST:
        item_id=request.session['item_id']
        item_ids = request.POST.getlist('id')
        description = request.POST.getlist('description')

        if 'image' in request.FILES:
            image = request.FILES['image']
            fs = FileSystemStorage()
            date = datetime.now().strftime("%H-%M-%S") + '.jpg'
            fs.save(date, image)
            myimage = date
        else:
            myimage=""



        item = tbl_Itemmaster.objects.get(id=id)
        amount = item.Item_Cost

        if tbl_Cartmaster.objects.filter(CUSTOMER__USERNAME_id=request.session['lid'], Cart_Status='pending').exists():
            cart_master = tbl_Cartmaster.objects.get(CUSTOMER__USERNAME_id=request.session['lid'],
                                                     Cart_Status='pending')
            cart_item = tbl_Cartchild.objects.create(Cart_Quantity=1, CARTMAST_id=cart_master.pk, ITEM_id=id,Image=myimage)
            cart_master.Tot_Amount = str(int(cart_master.Tot_Amount) + int(amount))

            cart_master.save()

            for i in range(len(item_ids)):
                c1 = cart_child_customization()
                c1.CART_CHILD_id=cart_item.id
                c1.description=description[i]
                c1.ITEM_CHILD_id=item_ids[i]
                c1.save()


            return HttpResponse("<script>alert('Item added to cart');window.location='/customer_cart';</script>")
        else:
            cart_master = tbl_Cartmaster.objects.create(Tot_Amount=amount, Cart_Status='pending',
                                                        CUSTOMER_id=request.session['lid'])
            cart_item = tbl_Cartchild.objects.create(Cart_Quantity=1, CARTMAST_id=cart_master.pk, ITEM_id=id,Image=myimage)
            for i in range(len(item_ids)):
                c1 = cart_child_customization()
                c1.CART_CHILD_id = cart_item.id
                c1.description = description[i]
                c1.ITEM_CHILD_id = item_ids[i]
                c1.save()
            return HttpResponse("<script>alert('Item added to cart');window.location='/customer_cart';</script>")
    return render(request, 'customer_pages/cart_child_customization.html', {'data': var,'data2':var2})



def view_customization(request,id):
    var=cart_child_customization.objects.filter(CART_CHILD_id=id)
    if var.exists():

        return render(request, 'customer_pages/view customization.html', {'data': var})
    else:
        return HttpResponse("<script>alert('Item not in  cart');window.location='/customer_cart';</script>")



def increase_quantity_cust(request,id):
    var=cart_child_customization.objects.get(id=id)
    var.CART_CHILD.Cart_Quantity=var.CART_CHILD.Cart_Quantity+1
    # cart_item = tbl_Cartchild.objects.get(pk=cart_item_id)
    #
    # cart_item.quantity += 1
    #
    var.save()

    return redirect('customer_view_orders')


from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.http import HttpResponse
from .models import tbl_Staff, tbl_Order, tbl_Delivery


def assign_dellivery(request, id):
    staff_list = tbl_Staff.objects.filter(Type='delivery')
    order = get_object_or_404(tbl_Order, id=id)

    if request.method == 'POST':
        selected_staff_id = request.POST.get('select')
        selected_staff = get_object_or_404(tbl_Staff, id=selected_staff_id)

        delivery_date = datetime.now().date() + timedelta(days=7)

        delivery = tbl_Delivery()
        delivery.ORDER = order
        delivery.STAFF = selected_staff
        delivery.Assign_Date = datetime.now().date()
        delivery.Delivery_Status = 'Assigned'
        delivery.Del_Date = delivery_date
        delivery.save()

        order.Order_Status = 'Delivered'
        order.save()

        return HttpResponse("<script>alert('Delivered');window.location='/admin_view_order';</script>")

    return render(request, 'admin_pages/assign.html', {'data': staff_list})


def staff_assign_dellivery(request, id):
    staff_list = tbl_Staff.objects.filter(Type='delivery')
    order = get_object_or_404(tbl_Order, id=id)

    if request.method == 'POST':
        selected_staff_id = request.POST.get('select')
        selected_staff = get_object_or_404(tbl_Staff, id=selected_staff_id)

        # Calculate delivery date as one week after today
        delivery_date = datetime.now().date() + timedelta(days=7)

        # Create a new delivery instance and assign values
        delivery = tbl_Delivery()
        delivery.ORDER = order
        delivery.STAFF = selected_staff
        delivery.Assign_Date = datetime.now().date()
        delivery.Delivery_Status = 'Delivered'
        delivery.Del_Date = delivery_date
        delivery.save()

        # Update order status to 'Delivered'
        order.Order_Status = 'Delivered'
        order.save()

        return HttpResponse("<script>alert('Delivered');window.location='/staff_view_order';</script>")

    return render(request, 'staff_pages/assign.html', {'data': staff_list})

# def add_purchase(request,id):
#     var=tbl_Itemmaster.objects.all()
#
#     # q = tbl_Itemmaster.objects.(id=id)
#     # amount = var.Item_Cost
#     if 'submit' in request.POST:
#         item=request.POST['item']
#         Purch_Quantity=request.POST['Purch_Quantity']
#         Selling_Price=request.POST['Selling_Price']
#
#         # staff_id=tbl_Login.objects.get(id=request.session['lid'])
#
#         if tbl_Purmaster.objects.filter( Purch_Status='pending',VENDOR_id=id,LOGIN_id=tbl_Login.objects.get(id=request.session['lid'])).exists():
#
#             purchase_master = tbl_Purmaster.objects.get(Purch_Status='pending',VENDOR_id=id,LOGIN_id=tbl_Login.objects.get(id=request.session['lid']))
#
#
#             if tbl_Purchild.objects.filter(PM_id=purchase_master.pk, ITEM_id=id).exists():
#                 # If the item already exists in the cart, update its quantity
#                 booking_child = tbl_Purchild.objects.get(PM_id=purchase_master.pk, ITEM_id=id)
#                 booking_child.Purch_Quantity = str(int(booking_child.Purch_Quantity) + 1)
#                 booking_child.save()
#
#
#             else:
#                 # If the item is not in the cart, create a new entry
#                 booking_child = tbl_Purchild(Purch_Quantity=Purch_Quantity, PM_id=purchase_master.pk, ITEM_id=item)
#                 booking_child.save()
#
#             # Update the total amount in the cart master
#                 purchase_master.Tot_Amt = float(purchase_master.Tot_Amt) + float(Selling_Price)
#                 purchase_master.save()
#
#             return HttpResponse("<script>alert('SUCCESSFULLY');window.location='/customer_view_products';</script>")
#         else:
#             # If there's no existing cart, create a new cart and add the item to it
#             booking_master = tbl_Purmaster(Tot_Amt=0, Purch_Status='pending',Pm_Date='pending')
#             booking_master.save()
#             booking_child = tbl_Purchild(Purch_Quantity=Purch_Quantity, PM_id=booking_master.pk, ITEM=id,Cpurch_Status='pending')
#             booking_child.save()
#
#
#
#
#     return render(request,'admin_pages/add_purchase.html',{'data':var})



def staff_add_purchase(request, id):
    var = tbl_Itemmaster.objects.all()

    if 'submit' in request.POST:
        item = request.POST['item']
        Purch_Quantity = request.POST['Purch_Quantity']
        Selling_Price = request.POST['Selling_Price']
        Cost = request.POST['Cost']
        print(Selling_Price)

        # Retrieve the LOGIN_id from the session
        login_id = request.session.get('lid')

        if login_id:
            # Check if a Purmaster with the given conditions exists
            purchase_master = tbl_Purmaster.objects.filter(Purch_Status='pending', VENDOR_id=id, LOGIN_id=login_id).first()

            if purchase_master:
                # If the purchase master exists, update it
                purchase_master.Tot_Amt = int(purchase_master.Tot_Amt)+ float(Selling_Price)

                purchase_master.save()

                # Check if the item already exists in the cart
                booking_child = tbl_Purchild.objects.filter(PM_id=purchase_master.pk, ITEM_id=id).first()

                if booking_child:
                    # If the item already exists in the cart, update its quantity
                    booking_child.Purch_Quantity = str(int(booking_child.Purch_Quantity) + int(Purch_Quantity))
                    booking_child.Selling_Price=Selling_Price
                    booking_child.Cost_Price=Cost
                    booking_child.save()
                else:
                    # If the item is not in the cart, create a new entry
                    booking_child = tbl_Purchild(Purch_Quantity=Purch_Quantity, PM=purchase_master, ITEM_id=item)
                    booking_child.Selling_Price = Selling_Price
                    booking_child.Cost_Price=Cost
                    booking_child.save()

            else:
                # If there's no existing cart, create a new cart and add the item to it
                purchase_master = tbl_Purmaster.objects.create(Tot_Amt=float(Selling_Price), Purch_Status='pending', Pm_Date='pending', VENDOR_id=id, LOGIN_id=login_id)
                booking_child = tbl_Purchild.objects.filter(Purch_Quantity=Purch_Quantity, PM=purchase_master, ITEM_id=item, Cpurch_Status='pending')
                booking_child.save()

            return HttpResponse("<script>alert('SUCCESSFULLY');window.location='/staff_manage_vendor';</script>")
        else:
            # Handle the case where the login_id is not available in the session
            return HttpResponse("<script>alert(' not found.');window.location='/';</script>")

    return render(request, 'staff_pages/add_purchase.html', {'data': var})







from django.shortcuts import render, HttpResponse
from .models import tbl_Itemmaster, tbl_Purmaster, tbl_Purchild, tbl_Login

from django.shortcuts import render, HttpResponse
from .models import tbl_Itemmaster, tbl_Purmaster, tbl_Purchild
from django.shortcuts import get_object_or_404

def add_purchase(request, id):
    var = tbl_Itemmaster.objects.all()

    if 'submit' in request.POST:
        item = request.POST['item']
        Purch_Quantity = request.POST['Purch_Quantity']
        Selling_Price = request.POST['Selling_Price']
        Cost = request.POST['Cost']
        print(Selling_Price)

        # Retrieve the LOGIN_id from the session
        login_id = request.session.get('lid')

        if login_id:
            # Check if a Purmaster with the given conditions exists
            purchase_master = tbl_Purmaster.objects.filter(Purch_Status='pending', VENDOR_id=id, LOGIN_id=login_id).first()

            if purchase_master:
                # If the purchase master exists, update it
                purchase_master.Tot_Amt = int(purchase_master.Tot_Amt)+ float(Selling_Price)

                purchase_master.save()

                # Check if the item already exists in the cart
                booking_child = tbl_Purchild.objects.filter(PM_id=purchase_master.pk, ITEM_id=id).first()

                if booking_child:
                    # If the item already exists in the cart, update its quantity
                    booking_child.Purch_Quantity = str(int(booking_child.Purch_Quantity) + int(Purch_Quantity))
                    booking_child.Selling_Price=Selling_Price
                    booking_child.Cost_Price=Cost
                    booking_child.save()
                else:
                    # If the item is not in the cart, create a new entry
                    booking_child = tbl_Purchild(Purch_Quantity=Purch_Quantity, PM=purchase_master, ITEM_id=item)
                    booking_child.Selling_Price = Selling_Price
                    booking_child.Cost_Price=Cost
                    booking_child.save()

            else:
                # If there's no existing cart, create a new cart and add the item to it
                purchase_master = tbl_Purmaster.objects.create(Tot_Amt=float(Selling_Price), Purch_Status='pending', Pm_Date='pending', VENDOR_id=id, LOGIN_id=login_id)
                booking_child = tbl_Purchild.objects.filter(Purch_Quantity=Purch_Quantity, PM=purchase_master, ITEM_id=item, Cpurch_Status='pending')
                booking_child.save()

            return HttpResponse("<script>alert('SUCCESSFULLY');window.location='/admin_manage_vendor';</script>")
        else:
            # Handle the case where the login_id is not available in the session
            return HttpResponse("<script>alert(' not found.');window.location='/';</script>")

    return render(request, 'admin_pages/add_purchase.html', {'data': var})






#
# def view_customization_page(request):
#     return render(request,'customer_pages/view_customization.html')


