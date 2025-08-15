import PyPDF2

pdf = PyPDF2.PdfReader("E:\git-v1.pdf")
print(len(pdf.pages))
first_page = pdf.pages[0]
print(first_page)
print(first_page.extract_text())