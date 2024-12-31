from django.urls import path
from .views import job_order_list, JobOrderCreateView, job_order_detail, md_approve_job_order, fm_approve_job_order
from django.urls import reverse_lazy  # Add this import for reverse_lazy

app_name = 'job_orders'

urlpatterns = [
    path('', job_order_list, name='job_order_list'),
    path('create/', JobOrderCreateView.as_view(), name='job_order_create'),
    path('<int:pk>/', job_order_detail, name='job_order_detail'),
    path('md-approve/<int:pk>/', md_approve_job_order, name='md_approve_job_order'),
    path('fm-approve/<int:pk>/', fm_approve_job_order, name='fm_approve_job_order'),
]