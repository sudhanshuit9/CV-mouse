import pyttsx3
import PyPDF2

book = open('python file.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
engine = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
    break
