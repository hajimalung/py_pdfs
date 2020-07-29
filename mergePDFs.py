import PyPDF2
import sys
from os import path

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("please provide atleast 2 pdf files for merging!!")
		exit()
	prog_name,*list_pdf_files = sys.argv
	print(prog_name, list_pdf_files)

	pdf_writer = PyPDF2.PdfFileWriter()

	for file_path in list_pdf_files:
		if not path.exists(file_path):
			print(f'{file_path} doesn\'t exist')
		else: 
			if '.pdf' not in file_path:
				print(f'## ignoring {file_path} as it is not a PDF file!!')
				continue
			else: 
				print(f'{file_path} is a PDF file!!')
				print(f'opening {file_path}')
				with open(file_path,"rb") as pdf_file_to_read:
					pdf_reader = PyPDF2.PdfFileReader(pdf_file_to_read)
					print(f'there are total {pdf_reader.numPages} pages found to read')
					for page_num in range(0,pdf_reader.numPages):
						print(f"reading page {page_num} of {file_path}")
						pdf_page = pdf_reader.getPage(page_num)
						#
						# manipulate the PDF page here
						#
						print('adding it to new file...')
						pdf_writer.addPage(pdf_page)
					print("writing all PDFs to merged_pdf_file.pdf..")
					with open('merged_pdf_file.pdf','wb') as merged_pdf_file:
						pdf_writer.write(merged_pdf_file)
						print('done!\nHappy Merging :)')