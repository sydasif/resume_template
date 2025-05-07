# Resume Generator

A professional resume generator that converts JSON data into a beautifully formatted HTML and PDF resume. The project uses Jinja2 templates for HTML generation and pdfkit for PDF conversion.

## Features

- Clean and professional resume layout
- Customizable HTML template with modern styling
- JSON-based data structure
- Sections for education, experience, skills, projects, and more
- Automatic PDF generation
- Responsive design using Bootstrap
- Print-friendly formatting
- Support for technical and soft skills categorization

## Prerequisites

1. Python 3.x installed
2. wkhtmltopdf installed (required for PDF generation)

## Installation

1. Clone this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install wkhtmltopdf:
   - Windows: Download and install from [wkhtmltopdf downloads](https://wkhtmltopdf.org/downloads.html)
   - Linux: `sudo apt-get install wkhtmltopdf`
   - macOS: `brew install wkhtmltopdf`

## Usage

1. Edit the `resume.json` file with your personal information
2. Customize the `template.html` if you want to modify the design
3. Run the generator:
   ```bash
   python app.py
   ```
4. Find your generated resume in `output.pdf`

## Styling Customization

The template includes modern styling with a clean, professional look. You can customize the appearance by modifying the CSS in the `template.html` file:

- **Colors**: The template uses a blue color scheme (primary: #3498db, secondary: #2980b9). Change these values to match your preferred color palette.
- **Typography**: The template uses 'Open Sans' and system fonts. You can change the font-family to any web-safe font or add custom web fonts.
- **Layout**: The template uses a two-column grid layout (30% left, 70% right). Adjust the grid-template-columns property to change this ratio.
- **Spacing**: Margins and paddings can be adjusted to create more or less whitespace.
- **Print Settings**: The template includes print-specific styles that optimize the resume for PDF output.

The template automatically handles both technical and soft skills categories if they are present in your JSON data.
