from django.template.loader import render_to_string

from django.http import HttpResponse

from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
from main.models import Persona



def export_pdf2(request):


    clientes = Persona.objects.all().values()
    mujeres = Persona.objects.filter(tipo_sexo=10).values()
    hombres = Persona.objects.filter(tipo_sexo=11).values()

    context = {
        "clientes_totales": len(clientes),
        "data": [
           {
            "titulo": "Clientes mujeres",
            "cantidad": len(mujeres),
            "data": list(mujeres),
           },
           {
            "titulo": "Clientes hombres",
            "cantidad": len(hombres),
            "data": list(hombres),
           } 
        ]
    }

    html_template = render_to_string("consulta2.html", context)
    pdf_file = HTML(string=html_template).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response