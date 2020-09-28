import pyttsx3  # import pyttsx3 for read text
import PyPDF2  # PyPDF2 module used to convert pdf text document into string

# include the pdf document into program
book = open('automatetheboringstuffwithpython.pdf', 'rb')
# get pdf document in PyPDF2
pdfReader = PyPDF2.PdfFileReader(book)
# count the number of pages in the pdf document
pages = pdfReader.numPages
print(pages)
# select the specific page which we want to read
page = pdfReader.getPage(25)
# extract the text from specific page of the pdf document
text = page.extractText()
print(text)

# initialize the pyttsx3
speaker = pyttsx3.init()
# get the extracted text from pdf document
speaker.say(text)
# run text to speech
speaker.runAndWait()
