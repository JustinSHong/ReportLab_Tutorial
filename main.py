from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image

import csv

data_file = 'data.csv' # hold a reference to data file

# import and parse data from data.csv
def import_data(data_file):
	attendee_data = csv.reader(open(data_file, newline=''))
	for row in attendee_data:
		# pertinent data points for pdf file
		last_name = row[0]
		first_name = row[1]
		course_name = row[2]
		# generate a certificate
		pdf_file_name = course_name + '_' + last_name + first_name + '.pdf'
		generate_certificate(first_name, last_name, course_name, pdf_file_name)

def generate_certificate(first_name, last_name, course_name, pdf_file_name):
	attendee_name = first_name + ' ' + last_name
	# define canvas to draw pdf
	c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))
	# header
	c.setFont('Helvetica', 48, leading=None) # fonts must be on your machine
	c.drawCentredString(415, 500, "Certificate of Completion") # define a center point (x, y) and draw text there
	# sub-header
	c.setFont('Helvetica', 24, leading=None)
	c.drawCentredString(415, 450, "This certificate is presented to:")
	# attendee_name
	c.setFont('Helvetica-Bold', 34, leading=None)
	c.drawCentredString(415, 395, attendee_name)
	# body
	c.setFont('Helvetica', 24, leading=None)
	c.drawCentredString(415, 350, "for completing the following course:")
	# course
	c.setFont('Helvetica', 20, leading=None)
	c.drawCentredString(415, 310, course_name)
	# seal image
	seal = 'lambda_logo.jpg'
	c.drawImage(seal, 300, 50, width=None, height=None)

	c.showPage() # creates, renders, and closes a page one time

	c.save() # save pdf(s)

import_data(data_file)






