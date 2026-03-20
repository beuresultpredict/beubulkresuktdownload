import streamlit as st
import requests
from xhtml2pdf import pisa
from io import BytesIO

st.title("🎓 Bulk Result PDF Downloader")

base_url = st.text_input("Base URL (जैसे: https://example.com/result?id=)")
roll_input = st.text_area("रोल नंबर्स (कोमा ',' लगाकर लिखें)")

def convert_url_to_pdf(url):
    # वेबसाइट से डेटा लाना
    response = requests.get(url)
    result_html = response.text
    
    # PDF बनाने के लिए मेमोरी बफर का इस्तेमाल
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(result_html, dest=pdf_buffer)
    
    return pdf_buffer.getvalue() if not pisa_status.err else None

if st.button("Generate PDFs"):
    if base_url and roll_input:
        rolls = [r.strip() for r in roll_input.split(",")]
        for roll in rolls:
            target_url = f"{base_url}{roll}"
            pdf_data = convert_url_to_pdf(target_url)
            
            if pdf_data:
                st.download_button(
                    label=f"📥 Download Result: {roll}",
                    data=pdf_data,
                    file_name=f"Result_{roll}.pdf",
                    mime="application/pdf"
                )
                st.success(f"Roll {roll} तैयार है!")
            else:
                st.error(f"Roll {roll} बनाने में दिक्कत आई।")
