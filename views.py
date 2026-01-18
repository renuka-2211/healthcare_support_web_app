from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'form.html')


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        issue = request.POST.get('issue')

        # Automation / AI idea (Rule-based)
        if issue == "Emergency":
            response = "⚠️ Please contact emergency services immediately."
        elif issue == "Insurance":
            response = "📄 Our insurance support team will contact you shortly."
        else:
            response = "📅 Your appointment request has been received."

        return HttpResponse(f"Thank you {name}!<br>{response}")
