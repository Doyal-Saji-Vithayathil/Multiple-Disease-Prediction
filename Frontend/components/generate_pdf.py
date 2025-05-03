from fpdf import FPDF
import base64
import datetime
def generate_pdf_report(name, disease, result, doctor_details):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Disease Diagnosis Report", ln=True, align="C")
    pdf.ln(10)

    # Patient Info
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Patient Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Predicted Disease: {disease}", ln=True)
    pdf.cell(200, 10, txt=f"Diagnosis Result: {result}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Recommended Doctor Info:", ln=True)

    pdf.set_font("Arial", size=12)
    for line in doctor_details.split('\n'):
        pdf.cell(200, 10, txt=line.strip(), ln=True)

    # Save to memory
    pdf_output = pdf.output(dest='S').encode('latin1')
    b64 = base64.b64encode(pdf_output).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="diagnosis_report.pdf">📄 Download Report as PDF</a>'
    return href