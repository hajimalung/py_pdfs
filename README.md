# py_pdfs
this python project has scripts helpful while working with PDFs

### dependencies
###### PyPDF2
	the scripts in this project uses PyPDF2 module 
	please make sure it is installed before running these scripts

### usage
###### mergePDFs_2
	this script will merge all the listed pdf files
	ex:  python mergePDFs_2.py file1.pdf file2.pdf file3.pdf file4.pdf ...

###### mergePDFs
	this script will merge all the listed pdf files while it has handle to individual pages of listed files
	using you can manipulate the PDF pages before merging to one file1
	
	update the manipulation login in script at the placeholder using pdf_page object
	
	ex:  python mergePDFs_2.py file1.pdf file2.pdf file3.pdf file4.pdf ...

###### watermarkPDF
	this script will add watermark to the provided pdf file.
	
	ex: python watermark.py pdf_file_path.pdf watermark_file.pdf
	
	
	
