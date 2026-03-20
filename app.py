import streamlit as st
import pdfkit
import time

st.set_page_config(page_title="Bulk Result Downloader", layout="centered")

st.title("🎓 Bulk Result PDF Downloader")
st.write("अपना URL और रोल नंबर्स की लिस्ट डालें।")

# User Inputs
base_url = st.text_input("Base URL (जैसे: https://example.com/result?id=)", placeholder="यहाँ URL पेस्ट करें...")
roll_input = st.text_area("रोल नंबर्स (कोमा ',' लगाकर लिखें)", placeholder="20101, 20102, 20103...")

if st.button("Generate PDFs"):
    if not base_url or not roll_input:
        st.warning("कृपया URL और कम से कम एक रोल नंबर ज़रूर डालें।")
    else:
        rolls = [r.strip() for r in roll_input.split(",")]
        st.divider()
        
        for roll in rolls:
            target_url = f"{base_url}{roll}"
            try:
                # PDF Generation Logic
                pdf_bytes = pdfkit.from_url(target_url, False)
                
                # Download Button for each roll
                st.download_button(
                    label=f"📥 Download Result: {roll}",
                    data=pdf_bytes,
                    file_name=f"Result_{roll}.pdf",
                    mime="application/pdf",
                    key=roll
                )
                st.success(f"रोल नंबर {roll} का PDF तैयार है!")
            except Exception as e:
                st.error(f"रोल नंबर {roll} में दिक्कत आई: वेबसाइट PDF बनाने की अनुमति नहीं दे रही।")

st.info("नोट: यह टूल उन वेबसाइट्स पर सबसे अच्छा काम करता है जिन्हें लॉगिन की ज़रूरत नहीं होती।")
