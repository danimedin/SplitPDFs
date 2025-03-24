from pathlib import Path
from pypdf import PdfReader, PdfWriter
import csv


pdf_path=(Path.home()
          / "Proxectos-Python"
          / "Divide-Escaneo"
          / "CA1.10 - Con Internet - Escaneados.pdf")

destino="PDFS/" + "CA1.10 - Con Internet - "

input_pdf = PdfReader(pdf_path)

#with open ("Alumnado-Escaneo.csv", newline='') as csvfile:
with open ("Alumnado-Escaneo-FH.csv", newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        arquivo=row['Apelidos'] + ", " + row['Nome'] + ".pdf"
        output_pdf = PdfWriter()
        comienzo=int(row['Primera'])-1
        fin=int(row['Última'])
        indice = 0
        for page in input_pdf.pages[comienzo:fin]:
            if row['Rotar'] == "Non":
                output_pdf.add_page(page)
            else:
                rotacion=row['Grados'].split(';')[indice]

                output_pdf.add_page(page.rotate(int(rotacion)))
            indice+=1


        output_pdf.write(destino  +  arquivo)
