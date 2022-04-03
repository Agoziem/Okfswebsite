from django.shortcuts import render,get_object_or_404, redirect
from .models import Payment,Amount
from .forms import PaymentForm
from home.models import School
import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

def initiate_payment(request):
	if request.method=='POST':
		Payment_form=PaymentForm(request.POST)
		if Payment_form.is_valid():
			Payment=Payment_form.save()
			amount=Amount.objects.get(description =Payment.Payment_type)
			context={
			'payment': Payment,
			'paymentamount': amount,
			'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY
			}
			return render(request,'Make_payment.html',context)
	else:
		payment_form=PaymentForm()
		return render(request,'Initiate_payment.html', { 'form':payment_form })
		
def verify_payment(request , ref : str) -> HttpResponse:
	payment=get_object_or_404(Payment,ref=ref)
	amount=get_object_or_404(Amount,description=payment.Payment_type)
	verified=payment.verify_payment()
	if verified:
		messages.success(request,"payment successful")
		return render(request, 'Online_receipt.html', { "receipt": payment , "paidamount": amount })
	else:
		messages.error(request,"verification failed, check your inputs and try again") 
		return redirect('Initiate_payment.html')
		
		
def receipt_pdf_view(request , ref : str) -> HttpResponse:
	payment=get_object_or_404(Payment,ref=ref)
	amount=get_object_or_404(Amount,description=payment.Payment_type)
	school=School.objects.all()
	template_path ='Online_receipt_pdf.html'
	context = {
				'receipt':payment,
				'paidamount': amount,
				'schoollogo': school,
				}
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment'; filename="Receipt.pdf"
	template = get_template(template_path)
	html = template.render(context)
	pisa_status = pisa.CreatePDF(
		html, dest=response)
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response

