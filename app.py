from pdf_mail import sendpdf

k = sendpdf(
    "231501045@rajalakshmi.edu.in", #sender email id
    "ezhiladhithyap@gmail.com", #receiver email
    "9841632080", #pwd
    "Report from RadiX", #Subject
    "Respected Sir/Ma'am, please find the attached document", #message
    "MyDoc", #FileName
    "C:\Users\pugal\OneDrive\Documents\1_General\Mail_Send\pdf_mail" #file_path
)

k.email_send()