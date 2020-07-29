import PyPDF2
with open('./resources/dummy.pdf', mode='rb') as dummy_pdf_file:
	pdf_reader = PyPDF2.PdfFileReader(dummy_pdf_file)
	print(pdf_reader.documentInfo)
	print(pdf_reader.numPages)
	# print(pdf_reader.getFormTextFields())
	print(pdf_reader.getPage(0))
	pdf_page_0 = pdf_reader.getPage(0)
	print(pdf_page_0.rotateClockwise(90))

	writer =PyPDF2.PdfFileWriter()
	writer.addPage(pdf_page_0)

	with open("tilted_dummy.pdf",mode="wb") as tilted_dummy_pdf_file:
		writer.write(tilted_dummy_pdf_file)