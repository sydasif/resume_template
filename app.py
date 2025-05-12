"""
Generates a PDF resume from a JSON data file and an HTML template.

This script reads resume data from 'resume.json', renders it into an HTML
template ('template.html'), and then converts the HTML to a PDF file
named 'output.pdf' using pdfkit.
"""

import json

import pdfkit
from jinja2 import Template

with open("resume.json") as file:
    resume = json.load(file)

with open("template.html", "r", encoding="utf-8") as f:
    template = Template(f.read())

html_content = template.render(resume=resume)
pdfkit.from_string(html_content, "output.pdf")
print("PDF generated successfully!")
