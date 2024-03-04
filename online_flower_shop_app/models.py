from django.db import models

# Create your models here.
class tbl_Login(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    User_Type=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)
    
class tbl_Staff(models.Model):
    USERNAME=models.ForeignKey(tbl_Login, on_delete=models.CASCADE)
    Staff_Fname=models.CharField(max_length=100)
    Staff_Lname=models.CharField(max_length=100)
    Staff_City=models.CharField(max_length=100)
    Staff_House=models.CharField(max_length=100)
    Staff_Dist=models.CharField(max_length=100)
    Staff_Pin=models.CharField(max_length=100)
    Staff_Place=models.CharField(max_length=100)
    Staff_Phone=models.CharField(max_length=100)
    Staff_Gender=models.CharField(max_length=100)
    Staff_Photo=models.ImageField(upload_to='static/staff')
    Staff_DOB=models.CharField(max_length=100)
    Staff_Status=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)

class tbl_Customer(models.Model):
     USERNAME=models.ForeignKey(tbl_Login, on_delete=models.CASCADE)
     C_Fname=models.CharField(max_length=100)
     C_Lname=models.CharField(max_length=100)
     C_House=models.CharField(max_length=100)
     C_City=models.CharField(max_length=100)
     C_Dist=models.CharField(max_length=100)
     C_Pin=models.CharField(max_length=100)
     C_Place=models.CharField(max_length=100)
     C_Phone=models.CharField(max_length=100)
     C_Gender=models.CharField(max_length=100)
     C_DOB=models.CharField(max_length=100)
     C_Status=models.CharField(max_length=100)

class tbl_Vendor(models.Model):
     LOGIN=models.ForeignKey(tbl_Login, on_delete=models.CASCADE)
     V_name=models.CharField(max_length=100)
     V_Email=models.CharField(max_length=100)
     V_Dist=models.CharField(max_length=100)
     V_Pin=models.CharField(max_length=100)
     V_Place=models.CharField(max_length=100)
     V_Phone=models.CharField(max_length=100)
     V_Status=models.CharField(max_length=100)
     
class tbl_Purmaster(models.Model):
     LOGIN=models.ForeignKey(tbl_Login, on_delete=models.CASCADE)
     VENDOR=models.ForeignKey(tbl_Vendor, on_delete=models.CASCADE)
     Pm_Date=models.CharField(max_length=100)
     Tot_Amt=models.FloatField()
     Purch_Status=models.CharField(max_length=100)

class tbl_Category(models.Model):
    Cat_Name=models.CharField(max_length=100)
    Cat_Desc=models.CharField(max_length=255)
    
class tbl_Flower(models.Model):
    Flower_Name=models.CharField(max_length=100)
    Color=models.CharField(max_length=100)
    Img=models.ImageField(upload_to='static/flower')
    Type=models.CharField(max_length=100)
    Flower_Status=models.CharField(max_length=100)
    
class tbl_Itemmaster(models.Model):
    CAT=models.ForeignKey(tbl_Category, on_delete=models.CASCADE)
    Item_Name=models.CharField(max_length=100)
    Item_Desc=models.CharField(max_length=100)
    Item_Cost=models.FloatField()
    Item_Img=models.ImageField(upload_to='static/item')
    Stock=models.CharField(max_length=100)
    Profit_Per=models.CharField(max_length=100)
    Item_Status=models.CharField(max_length=100)
    
class tbl_Itemchild(models.Model):
    ITEM=models.ForeignKey(tbl_Itemmaster, on_delete=models.CASCADE)
    FLOWER=models.ForeignKey(tbl_Flower, on_delete=models.CASCADE)
    
class tbl_Purchild(models.Model):
    PM=models.ForeignKey(tbl_Purmaster, on_delete=models.CASCADE)
    ITEM=models.ForeignKey(tbl_Itemmaster, on_delete=models.CASCADE)
    Purch_Quantity=models.CharField(max_length=100)
    Cost_Price=models.CharField(max_length=100)
    Selling_Price=models.CharField(max_length=100)
    Cpurch_Status=models.CharField(max_length=100)
    
class tbl_Cartmaster(models.Model):
    CUSTOMER=models.ForeignKey(tbl_Customer,on_delete=models.CASCADE)
    Tot_Amount=models.FloatField()
    Cart_Status=models.CharField(max_length=100)
    
class tbl_Cartchild(models.Model):
    CARTMAST=models.ForeignKey(tbl_Cartmaster,on_delete=models.CASCADE)
    ITEM=models.ForeignKey(tbl_Itemmaster,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='static')
    Cart_Quantity=models.IntegerField()
    
class tbl_Card(models.Model):
      CUSTOMER=models.ForeignKey(tbl_Customer,on_delete=models.CASCADE)
      Card_No=models.CharField(max_length=100)
      Card_Holdername=models.CharField(max_length=100)
      Expiry_Date=models.CharField(max_length=100)
      
class tbl_Order(models.Model):
      CARTMAST=models.ForeignKey(tbl_Cartmaster,on_delete=models.CASCADE)
      Bill_No=models.CharField(max_length=100)
      A_Fname=models.CharField(max_length=100)
      A_Lname=models.CharField(max_length=100)
      A_City=models.CharField(max_length=100)
      A_House=models.CharField(max_length=100)
      A_Dist=models.CharField(max_length=100)
      A_Pin=models.CharField(max_length=100)
      A_Place=models.CharField(max_length=100)
      A_Phone=models.CharField(max_length=100)
      Order_Date=models.CharField(max_length=100)
      Order_Total=models.CharField(max_length=100)
      Order_Status=models.CharField(max_length=100)
      
class tbl_Payment(models.Model):
      CARD=models.ForeignKey(tbl_Card,on_delete=models.CASCADE)
      ORDER=models.ForeignKey(tbl_Order,on_delete=models.CASCADE)
      Payment_Date=models.CharField(max_length=100)
      Payment_Status=models.CharField(max_length=100)
      
class tbl_Review(models.Model):
      CUSTOMER=models.ForeignKey(tbl_Customer,on_delete=models.CASCADE)
      # ITEM=models.ForeignKey(tbl_Itemmaster,on_delete=models.CASCADE)
      ORDER=models.ForeignKey(tbl_Order,on_delete=models.CASCADE)
      Review_Desc=models.CharField(max_length=100)
      
class tbl_Delivery(models.Model):
      ORDER=models.ForeignKey(tbl_Order,on_delete=models.CASCADE)
      STAFF=models.ForeignKey(tbl_Staff,on_delete=models.CASCADE)
      Assign_Date=models.CharField(max_length=100)
      Del_Date=models.CharField(max_length=100) 
      Delivery_Status=models.CharField(max_length=100)
      # delivery_boy=models.CharField(max_length=100)


class cart_child_customization(models.Model):
      ITEM_CHILD = models.ForeignKey(tbl_Itemchild, on_delete=models.CASCADE,default=1)
      CART_CHILD=models.ForeignKey(tbl_Cartchild,on_delete=models.CASCADE)
      description=models.CharField(max_length=500)
      Add_Amt=models.CharField(max_length=100)




      

    
    
     
    
    
     

    
    