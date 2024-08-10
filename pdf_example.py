#create docuement
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def drawMyRuler(pdf):
    pdf.drawString(100, 810, 'x100')
    pdf.drawString(200, 810, 'x200')
    pdf.drawString(300, 810, 'x300')
    pdf.drawString(400, 810, 'x400')
    pdf.drawString(500, 810, 'x500')

    pdf.drawString(10, 100, 'y100')
    pdf.drawString(10, 200, 'y200')
    pdf.drawString(10, 300, 'y300')
    pdf.drawString(10, 400, 'y400')
    pdf.drawString(10, 500, 'y500')
    pdf.drawString(10, 600, 'y600')
    pdf.drawString(10, 700, 'y700')
    pdf.drawString(10, 800, 'y800')
####
fileName = "MyDoc.pdf"
documentTitle = "Patient X-Ray Report"
title = "RadiX Medical Image (X-RAY) Report"
subtitle = "By Team PENTAGON"
image = 'IMG0003341.jpg'
textLines = [
    'Patient ID: 1101',
    'Patient Name: Alex',
    'Date of X-Ray Taken: 05/08/2024'
]

####


pdf = canvas.Canvas(fileName) #file_name
pdf.setTitle(documentTitle) #file_title
###
#Available fonts
'''for font in pdf.getAvailableFonts():
    print(font)'''
####
drawMyRuler(pdf) #Ruler
####
pdf.setFont("Times-Bold", 25)
pdf.drawCentredString(300,770, title) #Title
####
#pdf.setFillColorRGB(0,0,255) #fontColor
pdf.setFont("Times-Italic", 12)
pdf.drawCentredString(270,750, subtitle) #SubTitle
#####
pdf.line(40, 730, 550, 730) #Horizontal Rule
#####
#Para Text
text = pdf.beginText(80, 680)
text.setFont("Times-Roman", 15)
text.setFillColor(colors.black)
for line in textLines:
    text.textLine(line)

pdf.drawText(text)
#######
'''
pdf.drawInlineImage(image, 130, 400)##Doubt?
'''
pdf.save()