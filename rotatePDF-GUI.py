import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

open_title = "Select a PDF to rotate..."
file_type = "*.pdf"
input_path = gui.fileopenbox(title=open_title, default=file_type)
if input_path is None:
    exit()


choices = ("90", "180", "270")
message = "Rotate the PDF clockwise by how many degrees?"
degrees = None
while degrees is None:
    degrees = gui.buttonbox(message, "Choose rotation...", choices)

degrees = int(degrees)

save_title = "Save the rotated PDF as..."
output_path = gui.filesavebox(title=save_title, default=file_type)

warn_title = "Warning!"
warn_message = "Cannot overwrite original file!"
while input_path == output_path:
    gui.msgbox(warn_message, warn_title)
    output_path = gui.filesavebox(title=save_title, default=file_type)

if output_path is None:
    exit()

input_file = PdfFileReader(input_path)
output_pdf = PdfFileWriter()

for page in input_file.pages:
    page = page.rotateClockwise(degrees)
    output_pdf.addPage(page)

with open(output_path, "wb")as output_file:
    output_pdf.write(output_file)
