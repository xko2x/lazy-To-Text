from PIL import Image
from pytesseract import pytesseract
import PyPDF2
# install packages using pip:
# pip install pytesseract
# pip install PyPDF2
# pip install image
# download this and setup: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.1.20220118.exe

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

# function pdf to text pytesseract
def pdf_to_text(pdf_file):
	try:
		pdf_reader = PyPDF2.PdfFileReader(pdf_file)
		for page in range(pdf_reader.numPages):
			page_obj = pdf_reader.getPage(page)
			print(page_obj.extractText())
			# save the text to a file
			with open(path.split(".")[0] + ".txt", "w") as f:
				f.write(page_obj.extractText())
			
	except Exception as e:
		print(e)

# function image to text
def image_to_text(path):
	try:
		text = pytesseract.image_to_string(Image.open(path))
		print(text)
		# save the text to a file and the name is the name of the image
		with open(path.split(".")[0] + ".txt", "w") as f:
			f.write(text)
	except Exception as e:
		print(e)
# main but file path is from user input
def main():
	path = input("Enter the path of the file: ")
	if path.endswith(".pdf"):
		pdf_to_text(path)
	elif path.endswith(".png") or path.endswith(".jpg"):
		image_to_text(path)
	else:
		print("Invalid file type") 
main()