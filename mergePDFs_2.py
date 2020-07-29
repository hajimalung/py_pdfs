import PyPDF2
import sys

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("please provide atleast 2 pdf files for merging!!")
		exit()
	pdf_files_list = sys.argv[1:]

	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_files_list:
		print(pdf)
		merger.append(pdf)
	merger.write('mereger_generated.pdf')