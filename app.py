import streamlit as st
import pandas as pd
from bluetooth_scanner import get_devices

# ---------------- PAGE ---------------- #

st.set_page_config(
    page_title="Bluetooth Device Finder",
    page_icon="📡",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.title{
    text-align:center;
    font-size:34px;
    font-weight:bold;
    color:#4EA1FF;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:25px;
}

.device-card{
    background:#1f1f1f;
    border:1px solid #333333;
    border-radius:15px;
    padding:18px;
    margin-bottom:12px;
}

.device-name{
    font-size:22px;
    font-weight:600;
    color:white;
}

.status{
    color:#A0A0A0;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown(
    '<div class="title">📡 Bluetooth Device Finder</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Windows Bluetooth Scanner</div>',
    unsafe_allow_html=True
)

# ---------------- SESSION ---------------- #

if "devices" not in st.session_state:
    st.session_state.devices = []

# ---------------- BUTTON ---------------- #

if st.button("🔄 Scan Devices", use_container_width=True):

    with st.spinner("Scanning Bluetooth Devices..."):

        st.session_state.devices = get_devices()

devices = st.session_state.devices

# ---------------- SEARCH ---------------- #

search = st.text_input(
    "🔍 Search Device",
    placeholder="Type device name..."
)

if search:

    devices = [
        d for d in devices
        if search.lower() in d["Name"].lower()
    ]

st.write("")

# ---------------- DEVICE LIST ---------------- #

for i, device in enumerate(devices):

    with st.container(border=True):

        left, middle, right = st.columns([1,8,2])

        with left:

            st.markdown(
                f"<div style='font-size:40px;text-align:center'>{device['Icon']}</div>",
                unsafe_allow_html=True
            )

        with middle:

            st.markdown(
                f"<div class='device-name'>{device['Name']}</div>",
                unsafe_allow_html=True
            )

            st.markdown(
                "<div class='status'>⚪ Not Connected</div>",
                unsafe_allow_html=True
            )

        with right:

            st.button(
                "Connect",
                key=f"btn{i}",
                use_container_width=True
            )

st.write("")

# ---------------- FOOTER ---------------- #

st.info(f"📊 Total Devices Found : {len(devices)}")

# ---------------- CSV ---------------- #

if len(devices) > 0:

    df = pd.DataFrame(devices)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "💾 Export CSV",
        csv,
        file_name="Bluetooth_Devices.csv",
        mime="text/csv",
        use_container_width=True
    )