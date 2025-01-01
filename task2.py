import csv
from fpdf import FPDF

# Define a function to read and analyze data from a file
def read_and_analyze_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:  # Add encoding
        reader = csv.DictReader(file)
        data = [row for row in reader]
    
    total_rows = len(data)
    summary = {}
    for row in data:
        for key, value in row.items():
            if key not in summary:
                summary[key] = []
            summary[key].append(value)
    
    return data, total_rows, summary

# Define a function to generate a formatted PDF report
def generate_pdf_report(data, total_rows, summary, output_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Automated Report", ln=True, align="C")
    pdf.ln(10)

    # Add Summary
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Total Rows: {total_rows}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt="Summary of Data:", ln=True)
    pdf.set_font("Arial", size=12)
    for key, values in summary.items():
        unique_values = set(values)
        pdf.cell(200, 10, txt=f"- {key}: {len(unique_values)} unique values", ln=True)
    pdf.ln(10)

    # Add Table Data
    pdf.set_font("Arial", style="B", size=12)
    headers = data[0].keys()
    for header in headers:
        pdf.cell(40, 10, header, border=1)
    pdf.ln()
    
    pdf.set_font("Arial", size=12)
    for row in data:
        for header in headers:
            pdf.cell(40, 10, row[header], border=1)
        pdf.ln()
    
    # Save PDF
    pdf.output(output_file)
    print(f"Report generated: {output_file}")

# File paths
input_file = r"c:/Users/Lenovo/Downloads/sample_data.csv"  # Update with your file path
output_file = "report.pdf"

# Execute the script
data, total_rows, summary = read_and_analyze_data(input_file)
generate_pdf_report(data, total_rows, summary, output_file)

output_file = r"c:/Users/Lenovo/Downloads/report.pdf"
print(f"PDF Successfully generated at: {output_file}")

import os
pdf_file = "file:///G:/Python/report.pdf"
os.startfile(pdf_file)