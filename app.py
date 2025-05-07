import json

import pdfkit
from jinja2 import Template

with open("resume.json") as file:  # Changed back to resume.json
    resume = json.load(file)

with open("template.html") as file:
    template = Template(file.read())

html_content = template.render(resume=resume)
pdfkit.from_string(html_content, "output.pdf")
print("PDF generated successfully!")
