from pathlib import Path
from pypdf import PdfReader, PdfWriter
import csv
import json

def main() -> None:
    # Leer el archivo JSON
    with open('vars.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    pdf_path=(data["rutaEscaneados"])


    destino="PDFS/" + data["nombreArchivoExamen"]

    input_pdf = PdfReader(pdf_path)


    with open (data["rutaArchivoCSVAlumando"], newline='') as csvfile:
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


if __name__ == "__main__":
    main()