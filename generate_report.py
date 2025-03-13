from fpdf import FPDF
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--log", required=True, help="Log file path")
parser.add_argument("--output", required=True, help="PDF report output path")
args = parser.parse_args()

# Read log file
with open(args.log, "r") as log_file:
    logs = log_file.readlines()

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Model Training Report", ln=True, align="C")

# Add logs
for log in logs:
    pdf.cell(200, 10, log, ln=True, align="L")

# Save PDF
pdf.output(args.output)
print(f"Report saved to {args.output}")
