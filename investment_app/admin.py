from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import *

# Register your models here.

class InvestmentTypeResource(resources.ModelResource):
    class Meta:
        model = InvestmentType
        exclude = ('max_limit', 'risk_score', 'value', 'status')
class InvestmentTypeAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'max_limit', 'risk_score', 'value', 'portfolio_weight', 
        'risk_contribution', 'is_overlimit','status')
    class_resources = InvestmentTypeResource

admin.site.register(InvestmentType, InvestmentTypeAdmin)
@admin.register(Principal)
class PrincipalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'status')

# @admin.register(Investment)
# class InvestmentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'investment_type', 'principal', 'status')

class InvestmentResource(resources.ModelResource):
    pass

class InvestmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'investment_type', 'principal', 'status')

admin.site.register(Investment, InvestmentAdmin)

@admin.register(Transaction)
class TransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def trx_inv(self, obj):
        return obj.investment.name

    def trx_inv_type(self, obj):
        return obj.investment.investment_type.name

    list_display = ('trx_date', 'investment', 'trx_inv_type', 'buysell', 'price', 'volume', 'amount')
    list_filter = ['trx_date']
    search_fields = ('trx_date', 'investment__name')
    
class InvestmentTypeBalanceResource(resources.ModelResource):
    investment_type = fields.Field(
        column_name='investment_type',
        attribute='investment_type',
        widget = ForeignKeyWidget(InvestmentType, 'name')
    )

    class Meta:
        model = InvestmentTypeBalance

        fields = ('investment_type', 'value')
        # skip_unchanged = True
        # report_skipped = True
        # exclude = ('id')
        # # import_id_fields = ('investment_type', 'value') 
        # import_id_fields = ['investment_type']

class InvestmentTypeBalanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #list_display = ('investment_type', 'value')
    resource_class = InvestmentTypeBalanceResource

admin.site.register(InvestmentTypeBalance, InvestmentTypeBalanceAdmin)