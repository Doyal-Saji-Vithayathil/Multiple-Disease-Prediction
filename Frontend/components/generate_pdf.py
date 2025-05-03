from fpdf import FPDF
import base64
import datetime
import os

def get_font_path():
    # Assumes fonts/ is in your project root, adjust if needed
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'fonts', 'DejaVuSans.ttf'))

def generate_pdf_report(name, disease, result, doctor_details):
    pdf = FPDF()
    pdf.add_page()
    
    font_path = get_font_path()
    if not os.path.exists(font_path):
        raise RuntimeError(f"Font file not found: {font_path}")
    pdf.add_font("DejaVuSans", "", font_path, uni=True)
    pdf.add_font("DejaVuSans", "B", font_path, uni=True) # Add bold style
    pdf.set_font("DejaVuSans", size=12)

    # Title
    pdf.set_font("DejaVuSans", 'B', 16)
    pdf.cell(200, 10, txt="Disease Diagnosis Report", ln=True, align="C")
    pdf.ln(10)

    # Patient Info
    pdf.set_font("DejaVuSans", size=12)
    pdf.cell(200, 10, txt=f"Patient Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Predicted Disease: {disease}", ln=True)
    pdf.cell(200, 10, txt=f"Diagnosis Result: {result}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.ln(10)
    pdf.set_font("DejaVuSans", 'B', 14)
    pdf.cell(200, 10, txt="Recommended Doctor Info:", ln=True)

    pdf.set_font("DejaVuSans", size=12)
    for line in doctor_details.split('\n'):
        pdf.multi_cell(0, 10, txt=line.strip())

    # Save to memory and create download link
    pdf_output = pdf.output(dest='S').encode('latin-1', errors='replace')
    b64 = base64.b64encode(pdf_output).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="diagnosis_report.pdf">Download Report as PDF</a>'
    return href

def create_pdf(patient, prediction, prob, description, precautions, doctor_info):
    pdf = FPDF()
    pdf.add_page()
    
    font_path = get_font_path()
    if not os.path.exists(font_path):
        raise RuntimeError(f"Font file not found: {font_path}")
    pdf.add_font("DejaVuSans", "", font_path, uni=True)
    pdf.add_font("DejaVuSans", "B", font_path, uni=True) # Add bold style
    pdf.set_font("DejaVuSans", size=12)

    pdf.cell(0, 10, "Disease Prediction Report", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("DejaVuSans", "B", 12)
    pdf.cell(0, 10, "Patient Details:", ln=True)
    pdf.set_font("DejaVuSans", size=12)
    pdf.cell(0, 10, f"Name: {patient['name']}", ln=True)
    pdf.cell(0, 10, f"Age: {patient['age']}", ln=True)
    pdf.cell(0, 10, f"Gender: {patient['gender']}", ln=True)
    pdf.multi_cell(0, 10, f"Symptoms: {', '.join(patient['symptoms'])}")
    pdf.ln(5)
    pdf.set_font("DejaVuSans", "B", 12)
    pdf.cell(0, 10, "Prediction:", ln=True)
    pdf.set_font("DejaVuSans", size=12)
    pdf.cell(0, 10, f"Disease: {prediction}", ln=True)
    pdf.cell(0, 10, f"Probability: {prob*100:.2f}%", ln=True)
    pdf.ln(5)
    pdf.set_font("DejaVuSans", "B", 12)
    pdf.cell(0, 10, "Description:", ln=True)
    pdf.set_font("DejaVuSans", size=12)
    pdf.multi_cell(0, 10, description)
    pdf.ln(5)
    pdf.set_font("DejaVuSans", "B", 12)
    pdf.cell(0, 10, "Precautions:", ln=True)
    pdf.set_font("DejaVuSans", size=12)
    for i, p in enumerate(precautions, 1):
        pdf.cell(0, 10, f"{i}. {p}", ln=True)
    pdf.ln(5)
    pdf.set_font("DejaVuSans", "B", 12)
    pdf.cell(0, 10, "Doctor Recommendation:", ln=True)
    pdf.set_font("DejaVuSans", size=12)
    pdf.multi_cell(0, 10, doctor_info)
    return pdf.output(dest="S").encode("latin-1", errors='replace')
