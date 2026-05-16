from pypdf import PdfReader

reader = PdfReader("invoice_sample.pdf")

meta = reader.metadata
CreationDate = meta.creation_date.date().strftime("%d-%m-%Y")
CreationTime = meta.creation_date.time().strftime("%H:%M:%S")
CreatedDate =  [CreationDate, CreationTime]
print(CreatedDate)

#MVP
#wybór strony 1,2,3, wszystkie 1-2, itd.
#Wybieranie tekstów

