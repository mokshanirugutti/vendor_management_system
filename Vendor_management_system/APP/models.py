import uuid
from django.db import models
from datetime import datetime, timedelta
from django.db.models import F, Count

class Vendor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Vendor's name")
    contact_details = models.TextField(verbose_name="Contact information of the vendor")
    address = models.TextField(verbose_name="Physical address of the vendor")
    vendor_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="A unique identifier for the vendor")
    on_time_delivery_rate = models.FloatField(default=0, verbose_name="Tracks the percentage of on-time deliveries")
    quality_rating_avg = models.FloatField(default=0,verbose_name="Average rating of quality based on purchase orders")
    average_response_time = models.FloatField(default=0,verbose_name="Average time taken to acknowledge purchase orders")
    fulfillment_rate = models.FloatField(default=0,verbose_name="Percentage of purchase orders fulfilled successfully")

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:  # If the purchase order is being created for the first time
            if self.status == 'completed' and self.quality_rating is not None:
                # Only consider quality rating if order is completed and rating provided
                total_ratings = self.vendor.purchaseorder_set.filter(quality_rating__isnull=False).count()
                sum_ratings = self.vendor.purchaseorder_set.filter(quality_rating__isnull=False).aggregate(sum=models.Sum('quality_rating'))['sum']
                if total_ratings > 0:  # Avoid division by zero
                    self.vendor.quality_rating_avg = round(sum_ratings / total_ratings, 1)

            # Calculate fulfillment rate and average response time using aggregation
            completed_orders = self.vendor.purchaseorder_set.filter(status='completed').count()
            total_orders = self.vendor.purchaseorder_set.all().count()
            if total_orders > 0:  # Avoid division by zero
                self.vendor.fulfillment_rate = round((completed_orders / total_orders) * 1.0, 1)
                
            total_orders = self.vendor.purchaseorder_set.filter(status='completed').count()
            on_time_orders = self.vendor.purchaseorder_set.filter(status='completed', delivery_date=F('issue_date') + timedelta(days=1)).count()
            if total_orders > 0:  # Avoid division by zero
                self.vendor.on_time_delivery_rate = round((on_time_orders / total_orders) * 100, 1)


            # Calculate average response time 
            if self.order_date and self.delivery_date:
                total_response_time_days = 0
                order_set = self.vendor.purchaseorder_set.filter(status='completed')
                for order in order_set:
                    response_time_days = (order.delivery_date - order.order_date).days
                    total_response_time_days += response_time_days
                if order_set.count() > 0:
                    average_response_time_days = total_response_time_days / order_set.count()
                    self.vendor.average_response_time =  round((average_response_time_days),1)
                    if self.issue_date and self.delivery_date:
                        print(f'got these {self.issue_date} and { self.delivery_date}')
                        diff =  (self.delivery_date - self.issue_date).days
                        prev  = self.vendor.on_time_delivery_rate
                        
                        # print(f'order set = {order_set.count()}')
                        self.vendor.on_time_delivery_rate = (prev+diff)/order_set.count()
            # Save the vendor instance
            self.vendor.save()  
        super().save(*args, **kwargs)



    def __str__(self):
        return self.po_number


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
