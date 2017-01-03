from django.contrib import admin

# Register your models here.
from .models import VehMaster, VehWorkOrder, VehWorkInvoice, VehInvoice, VehTyres
from django.forms import TextInput, Textarea, ModelForm
from django.forms.models import inlineformset_factory
from django.db import models


class VehWorkOrderInline(admin.TabularInline):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'23'})},
        models.DecimalField: {'widget': TextInput(attrs={'size':'7'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':25})},
    }    
    model = VehWorkOrder
    extra = 1

class VehMasterAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20', 'padding-left':'1px'})},
    }
    
    list_display = ('Veh_Reg_No', 'Veh_Make', 'Veh_Model', 'Veh_Year', 'Veh_Status',
                    'Veh_Seats', 'Veh_Horsepower',
                    'Veh_Fuel_Type', 'Veh_Pur_date', 'Veh_Pur_price',
                    )
    fields = [('Veh_Reg_No', 'Veh_Make', 'Veh_Model', 'Veh_Status', 'Veh_Year'),
              ('Veh_Engine_No', 'Veh_Chassis_No', 'Veh_Seats', 'Veh_Fuel_Type',
               'Veh_Horsepower', 'Veh_Colour'),
              ('Veh_Sale_price', 'Veh_Pur_price', 'Veh_Sale_date', 'Veh_Pur_date')
              ]
    inlines = [VehWorkOrderInline]


#-------------------------------------------------

class VehWorkInvoiceInline(admin.TabularInline):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'23'})},
        models.DecimalField: {'widget': TextInput(attrs={'size':'7'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':25})},
    }    
    model = VehWorkInvoice
    extra = 1

class VehWorkOrderAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.DecimalField: {'widget': TextInput(attrs={'size':'7'})},
    }
    
    list_display = ('Work_Reg_No', 'Work_Order_No', 'Work_Date', 'Work_Man_Name',
                    'Work_Price',  'Work_Type', 'Work_Invoice_Ref', 'Work_Odometer',
                    'Work_Date','Work_Remaks', 'Work_Details',

                    )
    fields = [('Work_Reg_No', 'Work_Order_No', 'Work_Man_Name'),
              ('Work_Date', 'Work_Invoice_Ref', 'Work_Type'),
              ('Work_Remaks', 'Work_Details', 'Work_Odometer', 'Work_Price' )
              ]
    inlines = [VehWorkInvoiceInline] 


#-------------------------------------------------
'''

class VehInvoiceInline(admin.TabularInline):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'23'})},
        models.DecimalField: {'widget': TextInput(attrs={'size':'7'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':25})},
    }    
    model = VehInvoice
    extra = 1

class VehWorkOrderAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.DecimalField: {'widget': TextInput(attrs={'size':'7'})},
    }
    
    list_display = ('Work_Reg_No', 'Work_Order_No', 'Work_Date', 'Work_Man_Name',
                    'Work_Price',  'Work_Type', 'Work_Invoice_Ref', 'Work_Odometer',
                    'Work_Date','Work_Remaks', 'Work_Details',

                    )
    fields = [('Work_Reg_No', 'Work_Order_No', 'Work_Man_Name'),
              ('Work_Date', 'Work_Invoice_Ref', 'Work_Type'),
              ('Work_Remaks', 'Work_Details', 'Work_Odometer', 'Work_Price' )
              ]
    inlines = [VehInvoiceInline]    
'''


admin.site.register(VehMaster, VehMasterAdmin)
admin.site.register(VehWorkOrder, VehWorkOrderAdmin)
#admin.site.register(VehInvoice)
admin.site.register(VehTyres)

# 'Veh_Engine_No', 'Veh_Chassis_No', VehWorkInvoice, VehTyres

