from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView
from django.contrib import messages
from .models import JobOrder
from .forms import JobOrderForm
from django.urls import reverse_lazy  # Add this import for reverse_lazy
from django.utils import timezone  # Add this import for timezone.now()

@login_required
def job_order_list(request):
    # You might want to filter based on user role or other criteria
    job_orders = JobOrder.objects.all()
    return render(request, 'job_orders/job_order_list.html', {'job_orders': job_orders})

class JobOrderCreateView(CreateView):
    model = JobOrder
    form_class = JobOrderForm
    template_name = 'job_orders/job_order_form.html'
    success_url = reverse_lazy('job_orders:job_order_list')

    def form_valid(self, form):
        job_order = form.save(commit=False)
        job_order.created_by = self.request.user
        job_order.save()

        # Handle initial status based on user role
        if self.request.user.department == 'MD':
            job_order.status = 'PENDING_FM'
            job_order.md_approved_at = timezone.now()
            job_order.md_approved_by = self.request.user
            job_order.save()
            messages.success(self.request, 'Job Order created and sent to FM for approval.')
        elif self.request.user.department == 'FM':
            job_order.status = 'APPROVED'
            job_order.fm_approved_at = timezone.now()
            job_order.fm_approved_by = self.request.user
            job_order.save()
            messages.success(self.request, 'Job Order approved.')
        else:
            job_order.status = 'PENDING_MD'  # Default status if not MD or FM
            job_order.save()
            messages.success(self.request, 'Job Order created successfully.')

        return super().form_valid(form)

@login_required
def md_approve_job_order(request, pk):
    job_order = JobOrder.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST.get('approve') == 'approve':
            job_order.status = 'PENDING_FM'
            job_order.md_approved_at = timezone.now()
            job_order.md_approved_by = request.user
            job_order.save()
            messages.success(request, 'Job Order approved by MD.')
            return redirect('job_orders:job_order_list')
        elif request.POST.get('reject') == 'reject':
            job_order.status = 'REJECTED'
            job_order.md_approved_at = timezone.now()
            job_order.md_approved_by = request.user
            job_order.save()
            messages.error(request, 'Job Order rejected by MD.')
            return redirect('job_orders:job_order_list')
    return render(request, 'job_orders/md_approve_job_order.html', {'job_order': job_order})

@login_required
def fm_approve_job_order(request, pk):
    job_order = JobOrder.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST.get('approve') == 'approve':
            job_order.status = 'APPROVED'
            job_order.fm_approved_at = timezone.now()
            job_order.fm_approved_by = request.user
            job_order.save()
            messages.success(request, 'Job Order approved by FM.')
            return redirect('job_orders:job_order_list')
        elif request.POST.get('reject') == 'reject':
            job_order.status = 'REJECTED'
            job_order.fm_approved_at = timezone.now()
            job_order.fm_approved_by = request.user
            job_order.save()
            messages.error(request, 'Job Order rejected by FM.')
            return redirect('job_orders:job_order_list')
    return render(request, 'job_orders/fm_approve_job_order.html', {'job_order': job_order})

def job_order_detail(request, pk):
    job_order = JobOrder.objects.get(pk=pk)
    return render(request, 'job_orders/job_order_detail.html', {'job_order': job_order})