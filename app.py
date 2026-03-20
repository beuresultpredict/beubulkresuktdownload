import streamlit as st

st.set_page_config(page_title="BEU Result Tool", page_icon="🎓")

st.title("🎓 BEU Universal Result Linker")
st.write("भविष्य के किसी भी सेमेस्टर का रिजल्ट यहाँ से बल्क में निकालें।")

# 1. यूज़र से पूरा URL मांगना
raw_url = st.text_input(
    "रिजल्ट का URL यहाँ पेस्ट करें (किसी भी एक बच्चे का):", 
    placeholder="https://beu-bih.ac.in/result-three?name=...&regNo=23153125001&..."
)

st.info("नोट: ऊपर वाले URL में जहाँ रजिस्ट्रेशन नंबर है, उसे यह ऐप अपने आप बदल देगी।")

# 2. रजिस्ट्रेशन रेंज
col1, col2 = st.columns(2)
with col1:
    start_reg = st.number_input("शुरुआती Reg No:", value=23153125001, step=1)
with col2:
    end_reg = st.number_input("आखिरी Reg No:", value=23153125010, step=1)

if st.button("Generate All Links"):
    if not raw_url:
        st.error("कृपया पहले एक सैंपल URL डालें।")
    else:
        # यहाँ हम URL में से पुराने RegNo को ढूंढ कर उसे बदलने का लॉजिक लगा रहे हैं
        import re
        
        # URL में 'regNo=' के बाद वाले नंबर को ढूंढना
        pattern = r"(regNo=)(\d+)"
        
        st.success(f"कुल {int(end_reg) - int(start_reg) + 1} लिंक तैयार किए जा रहे हैं...")
        st.divider()

        for reg in range(int(start_reg), int(end_reg) + 1):
            # URL में रजिस्ट्रेशन नंबर को नए नंबर से बदल देना
            new_url = re.sub(pattern, rf"\1{reg}", raw_url)
            
            # डिस्प्ले करना
            st.markdown(f"**Reg No: {reg}**")
            st.markdown(f"[यहाँ क्लिक करें और PDF सेव करें]({new_url})")
            st.divider()

st.caption("Custom Built for BEU Students - No Code Change Needed in Future")
