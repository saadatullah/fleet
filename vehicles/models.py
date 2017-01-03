from __future__ import unicode_literals

from django.db import models

# Create your models here.


class VehMaster(models.Model):
    Veh_Reg_No = models.CharField("Registration No", max_length=8, primary_key=True)
    Veh_Make = models.CharField("Vehicle's Make", max_length=15)
    Veh_Model = models.CharField("Vehicle's Model", max_length=15)
    Veh_Year = models.IntegerField("Year Manufactured", blank=True, null=True)
    Veh_Pur_date = models.DateField('Purchase Date', blank=True, null=True)
    Veh_Pur_price = models.IntegerField('Purchase Price', blank=True, null=True)
    Veh_Sale_date = models.DateField('Sales Date', blank=True, null=True)
    Veh_Sale_price = models.IntegerField('Sales Price', blank=True, null=True)
    Veh_Seats = models.IntegerField('No of Seats', blank=True, null=True)
    Veh_Horsepower = models.IntegerField('Power CC', blank=True, null=True)
    Veh_Colour = models.CharField('Colour',max_length=20, blank=True, null=True)
    Veh_Fuel_Type = models.CharField('Fuel Type', max_length=10, blank=True, null=True)
    Veh_Engine_No = models.CharField('Engine No', max_length=20, blank=True, null=True)
    Veh_Chassis_No = models.CharField('Chassis No', max_length=20, blank=True, null=True)
    Veh_Status = models.CharField('Status', max_length=10)

    def __str__(self):
        return self.Veh_Reg_No

class VehWorkOrder(models.Model):

    Work_Order_No  = models.CharField(max_length=25, primary_key=True, blank=False, null=False)
    Work_Reg_No = models.ForeignKey(VehMaster, verbose_name='Registration No', on_delete=models.CASCADE)
    Work_Type  = models.CharField("Tyep of Work", max_length=25)
    Work_Invoice_Ref  = models.CharField("Work Invoice No", max_length=25)
    Work_Odometer = models.IntegerField("Odometer Reading", blank=True, null=True)
    Work_Man_Name = models.CharField("Expert's Name", max_length=25, blank=True, null=True)
    Work_Details = models.CharField(max_length=200)
    Work_Date = models.DateField('Work Order Date', blank=True, null=True)
    Work_Price = models.DecimalField(max_digits=5, decimal_places=2)
    Work_Remaks = models.CharField("Remarks", max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.Work_Reg_No)



class VehWorkInvoice(models.Model):

    Inv_Order_No = models.ForeignKey(VehWorkOrder, verbose_name='Work Order No', on_delete=models.CASCADE)
    Inv_No  = models.CharField("Invoice No", max_length=25)
    Inv_Date  = models.DateField("Invoice Date")
    Inv_Customer_Name  = models.CharField("Customer Name", max_length=30)
    Inv_Customer_Address1 = models.CharField("Address Line 1", max_length=40, blank=True, null=True)
    Inv_Customer_Address2 = models.CharField("Address Line 2", max_length=40, blank=True, null=True)
    Inv_Customer_City = models.CharField("City", max_length=30, blank=True, null=True)
    Inv_Customer_Contact = models.CharField("Contact No", max_length=15, blank=True, null=True)
    Inv_Charge_Type = models.CharField('Charge Type', max_length=35, blank=True, null=True)
    Inv_Price = models.DecimalField(max_digits=5, decimal_places=2)
    Inv_VAT_Persent = models.IntegerField("VAT Persentage", blank=True, null=True)

    def __str__(self):
        return self.Inv_Order_No





class VehInvoice(models.Model):

    Work_Order_No = models.ForeignKey(VehWorkOrder, to_field='Work_Order_No', verbose_name='Registration No', on_delete=models.CASCADE)
    Inv_No  = models.CharField("Invoice No", max_length=25)
    Inv_Date  = models.DateField("Invoice Date")
    Inv_Customer_Name  = models.CharField("Customer Name", max_length=30)
    Inv_Customer_Contact = models.CharField("Contact No", max_length=15, blank=True, null=True)
    Inv_Price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.Work_Order_No) 


class VehTyres(models.Model):

    Tyre_Reg_No = models.ForeignKey(VehMaster, verbose_name='Registration No', on_delete=models.CASCADE)
    Tyre_Tracking  = models.CharField("Tyre No", max_length=25)
    Tyre_Date  = models.DateField("Tyre Date")
    Tyre_Shop  = models.CharField("Tyre Shop", max_length=30)
    Inv_Customer_Contact = models.CharField("Contact No", max_length=15, blank=True, null=True)
    Tyre_Price = models.DecimalField(max_digits=5, decimal_places=2)
    Tyre_OSF = models.IntegerField("OSF", blank=True, null=True)
    Tyre_NSF = models.IntegerField("NSF", blank=True, null=True)
    Tyre_OSR = models.IntegerField("OSR", blank=True, null=True)
    Tyre_NSR = models.IntegerField("NSR", blank=True, null=True)

    def __str__(self):
        return self.Tyre_Reg_No 
    

   




# , on_delete=models.CASCADE      
