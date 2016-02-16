from django.contrib import admin
from stock.models import Stock, StockAdmin, StockCell, StockCellAdmin

admin.site.register(Stock, StockAdmin)
admin.site.register(StockCell, StockCellAdmin)
