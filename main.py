from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesize import landscape
from reportlab.platypus import Image

import csv

data_file = 'data.csv' # hold a reference to data file

# import and parse data from data.csv
def import_data(data_file):
	attendee_data = csv.reader(open(data_file, "rb"))
	for row in attendee_data:
		# pertinent data points for pdf file
		last_name = row[0]
		first_name = row[1]
		course_name = row[2]
		# generate a certificate
		pdf_file_name = course_name + '_' + last_name + first_name + '.pdf'
		generate_certificate(first_name, last_name, pdf_file_name)