from django.template.loader import render_to_string

from django.http import HttpResponse

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from main.models import Servicio


def export_pdf4(request):


    fecha1 = request.GET.get("fecha1")
    fecha2 = request.GET.get("fecha2")

    servicios = Servicio.objects.filter(fecha_ingreso__range=[fecha1, fecha2])

    context = {
        "cantidad": len(servicios),
        "data": servicios,
        "fecha1": fecha1,
        "fecha2": fecha2,
    }

    html_template = render_to_string("consulta4.html", context)
    pdf_file = HTML(string=html_template).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response
