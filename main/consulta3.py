from django.template.loader import render_to_string

from django.http import HttpResponse

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from main.models import Servicio


def export_pdf3(request):


    fecha1 = request.GET.get("fecha1")

    servicios = Servicio.objects.filter(fecha_ingreso=fecha1)

    context = {
        "cantidad": len(servicios),
        "data": servicios,
        "fecha1": fecha1,
    }

    html_template = render_to_string("consulta3.html", context)
    pdf_file = HTML(string=html_template).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response
