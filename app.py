import streamlit as st
import requests
from xhtml2pdf import pisa
from io import BytesIO

st.set_page_config(page_title="Result Downloader", page_icon="🎓")

st.title("🎓 Bulk Result PDF Downloader")
st.write("URL और रोल नंबर डालकर रिजल्ट डाउनलोड करें।")

def convert_html_to_pdf(url):
    try:
        # वेबसाइट से डेटा लाना
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None
        
        # PDF बनाने की प्रक्रिया
        pdf_buffer = BytesIO()
        pisa_status = pisa.CreatePDF(response.text, dest=pdf_buffer)
        
        if pisa_status.err:
            return None
        return pdf_buffer.getvalue()
    except Exception as e:
        return None

# User Input
base_url = st.text_input("URL यहाँ डालें:", placeholder="https://example.com/result?id=")
roll_input = st.text_area("रोल नंबर्स (कोमा लगाकर):", placeholder="101, 102, 103")

if st.button("Generate PDFs"):
    if not base_url or not roll_input:
        st.warning("कृपया सारी जानकारी भरें।")
    else:
        rolls = [r.strip() for r in roll_input.split(",")]
        
        for roll in rolls:
            target_url = f"{base_url}{roll}"
            st.write(f"Processing Roll: {roll}...")
            
            pdf_data = convert_html_to_pdf(target_url)
            
            if pdf_data:
                st.download_button(
                    label=f"📥 Download Result {roll}",
                    data=pdf_data,
                    file_name=f"Result_{roll}.pdf",
                    mime="application/pdf",
                    key=roll
                )
            else:
                st.error(f"Roll {roll} का डेटा नहीं मिल पाया।")

st.markdown("---")
st.caption("Made with ❤️ by your Coding Partner")
