import pyttsx3
import PyPDF2
book = open('python file.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
engine = pyttsx3.init()
page = pdfReader.getPage(7)
text = page.extractText()
engine.say(text)
engine.runAndWait()
