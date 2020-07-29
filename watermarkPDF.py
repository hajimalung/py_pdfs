import PyPDF2
import sys
from os import path

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("please provide <pdf_to_water_mark> <empty_watermark_page>")
		exit()
	
	pdf_path,water_mark_path = sys.argv[1:]

	writer = PyPDF2.PdfFileWriter()
	with open(water_mark_path,'rb') as water_mark_fle:
		pdf_watermark_reader = PyPDF2.PdfFileReader(water_mark_fle)
		water_mark_page = pdf_watermark_reader.getPage(0)

		with open(pdf_path,'rb') as pdf_file:
			pdf_file_reader = PyPDF2.PdfFileReader(pdf_file)

			for page_num in range(0,pdf_file_reader.numPages):
				pdf_file_page = pdf_file_reader.getPage(page_num)
				pdf_file_page.mergePage(water_mark_page)
				writer.addPage(pdf_file_page)
			with open('water_marked_pdfs.pdf','wb') as output_pdf:
				writer.write(output_pdf)
