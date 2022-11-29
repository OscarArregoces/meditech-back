from django.template.loader import render_to_string

from django.http import HttpResponse

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from main.models import Servicio


def export_pdf(request):

    serviciosTotales = Servicio.objects.all()
    computadores = Servicio.objects.filter(tipo_productoId=13)
    monitores = Servicio.objects.filter(tipo_productoId=14)
    televisores = Servicio.objects.filter(tipo_productoId=15)
    video_beams = Servicio.objects.filter(tipo_productoId=16)

    context = {
        "servicios_totales": len(serviciosTotales),
        "data": [
            {
                "titulo": "Computadores",
                "cantidad": len(computadores),
                "data": computadores
            },
            {
                "titulo": "Monitores",
                "cantidad": len(monitores),
                "data": monitores
            },
            {
                "titulo": "Televisores",
                "cantidad": len(televisores),
                "data": televisores
            },
            {
                "titulo": "Video Beams",
                "cantidad": len(video_beams),
                "data": video_beams
            }
        ]
    }

    html_template = render_to_string("consulta1.html", context)
    pdf_file = HTML(string=html_template).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response

    # "computadores": {
    #     "cantidad": len(computadores),
    #     "data": computadores
    # },
    # "monitores": {
    #     "cantidad": len(monitores),
    #     "data": monitores
    # },
    # "televisores": {
    #     "cantidad": len(televisores),
    #     "data": televisores
    # },
    # "video_beams": {
    #     "cantidad": len(video_beams),
    #     "data": video_beams
    # },

    # html = render_to_string("consulta1.html", context)

    # response = HttpResponse(content_type="application/pdf")
    # response["Content-Disposition"] = "inline; report.pdf"

    # font_config = FontConfiguration()
    # HTML(string=html).write_pdf(response, font_config=font_config)

    # return response
