from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

###
#table data
data = [
    ['Dedicated Hosting', 'VPS Hosting', 'Sharing Hosting', 'Reseller Hosting'],
    ['200/Month', '100/Month', '20/Month', '50/Month'],
    ['Free Domain', 'Free Domain', 'Free Domain', 'Free Domain'],
    ['2GB DDR2', '20GB Disc Space', 'Unlimited Email', 'Unlimited Email']
]
###
fileName = 'pdfTable.pdf' #fileName
###
#setting up the doc
pdf = SimpleDocTemplate(
    fileName,
    pagesize= letter
)
###
#setting the table and thereby incorporate in doc
table = Table(data)

##Add Style
style = TableStyle([
    ('BACKGROUND', (0,0), (3,0), colors.green),
    ('TEXTCOLOR', (0,0), (3,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 13),
    ('BOTTOMPADDING', (0,0), (-1, 0), 10),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige)
])

table.setStyle(style)

#Alternate Background Color

rowNumb = len(data)
for i in range(1, rowNumb):
    if i%2 == 0:
        bc = colors.burlywood
    else:
        bc = colors.beige
    
    ts = TableStyle(
        [('BACKGROUND', (0,i), (-1,i), bc)]
    )
    table.setStyle(ts)
#####
#Grid Setting
ts = TableStyle(
    [
        ('GRID', (0,0), (-1,-1), 2, colors.black)
    ]
)
table.setStyle(ts)

#####
#add values to table
elems =[]
elems.append(table)


pdf.build(elems)