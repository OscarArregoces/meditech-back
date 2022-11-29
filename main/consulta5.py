from django.template.loader import render_to_string

from django.http import HttpResponse

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from main.models import Servicio, Persona


def export_pdf5(request):

    serviciosTotales = Servicio.objects.all()
    computadores = Servicio.objects.filter(tipo_productoId=13)
    monitores = Servicio.objects.filter(tipo_productoId=14)
    televisores = Servicio.objects.filter(tipo_productoId=15)
    video_beams = Servicio.objects.filter(tipo_productoId=16)

    clientes = Persona.objects.all()
    mujeres = Persona.objects.filter(tipo_sexo=10)
    hombres = Persona.objects.filter(tipo_sexo=11)

    context = {
        "consulta1": {
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
            ],
        },
        "consulta2": {
            "clientes_totales": len(clientes),
            "data": [
                {
                    "titulo": "Clientes mujeres",
                    "cantidad": len(mujeres),
                    "data": mujeres,
                },
                {
                    "titulo": "Clientes hombres",
                    "cantidad": len(hombres),
                    "data": hombres,
                }
            ]
        }

    }

    html_template = render_to_string("consulta5.html", context)
    pdf_file = HTML(string=html_template).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response
