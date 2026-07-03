import streamlit as st
import requests
import time
import pandas as pd

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Car Price Prediction",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_URL = "https://car-price-prediction-lsgu.onrender.com/predict"

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
font-family:'Poppins',sans-serif;
}

/* Hide Streamlit */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Background */

.stApp{

background:
linear-gradient(135deg,#0f172a,#1e293b,#334155,#0f766e);

color:white;

}

/* Sidebar */

[data-testid="stSidebar"]{

background:#111827;

border-right:1px solid rgba(255,255,255,.08);

}

/* Hero */

.hero{

padding:35px;

border-radius:25px;

background:rgba(255,255,255,.08);

backdrop-filter:blur(18px);

box-shadow:0 10px 40px rgba(0,0,0,.4);

text-align:center;

margin-bottom:25px;

}

.hero h1{

font-size:50px;

font-weight:700;

margin-bottom:10px;

}

.hero p{

font-size:19px;

color:#dddddd;

}

/* Glass Card */

.card{

background:rgba(255,255,255,.08);

padding:28px;

border-radius:22px;

backdrop-filter:blur(18px);

box-shadow:0 12px 30px rgba(0,0,0,.3);

transition:.4s;

}

.card:hover{

transform:translateY(-8px);

}

/* Metrics */

[data-testid="metric-container"]{

background:rgba(255,255,255,.08);

padding:18px;

border-radius:16px;

box-shadow:0 6px 20px rgba(0,0,0,.25);

}

/* Inputs */

.stTextInput input{

background:#1e293b;

color:white;

border-radius:12px;

}

.stNumberInput input{

background:#1e293b;

color:white;

border-radius:12px;

}

.stSelectbox div[data-baseweb="select"]{

background:#1e293b;

border-radius:12px;

}

/* Button */

.stButton>button{

width:100%;

height:65px;

border:none;

border-radius:18px;

background:linear-gradient(90deg,#00C853,#64DD17);

font-size:24px;

font-weight:bold;

color:white;

transition:.4s;

}

.stButton>button:hover{

transform:scale(1.03);

box-shadow:0 0 30px #00C853;

}

/* Result */

.result{

padding:35px;

border-radius:22px;

background:linear-gradient(135deg,#00b09b,#96c93d);

font-size:35px;

font-weight:bold;

text-align:center;

box-shadow:0 15px 35px rgba(0,0,0,.4);

animation:fade .8s;

}

@keyframes fade{

from{

opacity:0;

transform:translateY(20px);

}

to{

opacity:1;

transform:translateY(0);

}

}

.footer{

text-align:center;

color:#cccccc;

margin-top:40px;

}

</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/744/744465.png",
        width=130
    )

    st.title("🚗 AI Car Price")

    st.write("---")

    st.success("✔ Machine Learning")

    st.success("✔ FastAPI Backend")

    st.success("✔ Streamlit UI")

    st.success("✔ Instant Prediction")

    st.write("---")

    st.info(
        """
        Predict the resale value of any car
        using an AI-powered regression model.
        """
    )

    st.write("---")

    st.caption("Made with ❤️ by Santosh Mahanta")

# ==========================
# HERO SECTION
# ==========================

st.markdown("""

<div class="hero">

<h1>🚗 AI Car Price Prediction</h1>

<p>

Predict your vehicle's resale price instantly using Machine Learning.

</p>

</div>

""", unsafe_allow_html=True)
# ==========================================================
# VEHICLE INFORMATION
# ==========================================================

st.markdown("## 🚘 Vehicle Information")

left, right = st.columns([2.2, 1])

# ---------------- LEFT PANEL ---------------- #

with left:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        car_name = st.text_input(
            "🚗 Car Name",
            value="Swift"
        )

        year = st.number_input(
            "📅 Manufacturing Year",
            min_value=1990,
            max_value=2026,
            value=2018,
            step=1
        )

        present_price = st.number_input(
            "💰 Ex-showroom Price (Lakhs)",
            min_value=0.0,
            max_value=100.0,
            value=6.50,
            step=0.10
        )

        kms_driven = st.number_input(
            "🛣️ Kilometers Driven",
            min_value=0,
            max_value=500000,
            value=35000,
            step=1000
        )

    with col2:

        fuel_type = st.selectbox(
            "⛽ Fuel Type",
            ["Petrol", "Diesel", "CNG"]
        )

        seller_type = st.selectbox(
            "🏪 Seller Type",
            ["Dealer", "Individual"]
        )

        transmission = st.selectbox(
            "⚙️ Transmission",
            ["Manual", "Automatic"]
        )

        owner = st.selectbox(
            "👤 Previous Owners",
            [0, 1, 2, 3]
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RIGHT PANEL ---------------- #

with right:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    current_year = 2026
    car_age = current_year - year

    st.subheader("📊 Vehicle Summary")

    st.metric(
        "🚘 Car",
        car_name
    )

    st.metric(
        "📅 Age",
        f"{car_age} Years"
    )

    st.metric(
        "⛽ Fuel",
        fuel_type
    )

    st.metric(
        "⚙️ Gearbox",
        transmission
    )

    st.metric(
        "👤 Owner",
        owner
    )

    st.metric(
        "🛣️ KM Driven",
        f"{kms_driven:,}"
    )

    st.metric(
        "💰 Showroom Price",
        f"₹ {present_price:.2f} L"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# QUICK INSIGHTS
# ==========================================================

st.markdown("### 📈 Vehicle Insights")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.info(f"🚘 **Model:** {car_name}")

with c2:
    st.info(f"📅 **Age:** {car_age} Years")

with c3:
    st.info(f"🛣️ **Distance:** {kms_driven:,} KM")

with c4:
    st.info(f"⛽ **Fuel:** {fuel_type}")

    # ==========================================================
# CREATE API PAYLOAD
# ==========================================================

payload = {
    "Car_Name": car_name,
    "Year": year,
    "Present_Price": present_price,
    "Kms_Driven": kms_driven,
    "Fuel_Type": fuel_type,
    "Seller_Type": seller_type,
    "Transmission": transmission,
    "Owner": owner
}

st.write("")

# ==========================================================
# PREDICT BUTTON
# ==========================================================

c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    predict = st.button(
        "🚀 Predict Selling Price",
        use_container_width=True
    )

st.write("")

# ==========================================================
# PREDICTION
# ==========================================================

if predict:

    progress = st.progress(0)

    status = st.empty()

    for i in range(100):
        progress.progress(i + 1)
        status.text(f"🤖 AI is analyzing your vehicle... {i+1}%")
        time.sleep(0.01)

    progress.empty()
    status.empty()

    try:

        response = requests.post(
            API_URL,
            json=payload,
            timeout=20
        )

        if response.status_code == 200:

            result = response.json()

            prediction = result.get(
                "prediction",
                result.get("predicted_price")
            )

            if prediction is not None:

                st.success("✅ Prediction Completed Successfully")

                st.balloons()

                # -------------------------------
                # RESULT CARD
                # -------------------------------

                st.markdown(
                    f"""
                    <div class="result">

                    💰 Estimated Selling Price

                    <br><br>

                    ₹ {prediction:.2f} Lakhs

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.write("")

                # -------------------------------
                # PRICE ANALYSIS
                # -------------------------------

                st.subheader("📊 Price Analysis")

                a, b, c = st.columns(3)

                with a:
                    st.metric(
                        "Current Showroom Price",
                        f"₹ {present_price:.2f} L"
                    )

                with b:

                    depreciation = max(
                        present_price - prediction,
                        0
                    )

                    st.metric(
                        "Depreciation",
                        f"₹ {depreciation:.2f} L"
                    )

                with c:

                    resale = (prediction / present_price) * 100 if present_price else 0

                    st.metric(
                        "Resale Value",
                        f"{resale:.1f}%"
                    )

                st.write("")

                # -------------------------------
                # VEHICLE DETAILS
                # -------------------------------

                st.subheader("🚘 Vehicle Details")

                d1, d2, d3, d4 = st.columns(4)

                with d1:
                    st.info(f"**Car**\n\n{car_name}")

                with d2:
                    st.info(f"**Age**\n\n{car_age} Years")

                with d3:
                    st.info(f"**Fuel**\n\n{fuel_type}")

                with d4:
                    st.info(f"**Transmission**\n\n{transmission}")

            else:

                st.error("Prediction key not found in API response.")

                st.json(result)

        else:

            st.error(f"API Error : {response.status_code}")

            st.code(response.text)

    except Exception as e:

        st.error("❌ Unable to connect to FastAPI Server")

        st.code(str(e))
        # ==========================================================
# PRICE COMPARISON
# ==========================================================

st.write("")
st.subheader("📊 Price Comparison")

chart_df = pd.DataFrame({
    "Category": [
        "Current Price",
        "Predicted Price"
    ],
    "Price": [
        present_price,
        prediction
    ]
})

st.bar_chart(
    chart_df.set_index("Category")
)

# ==========================================================
# DEPRECIATION
# ==========================================================

st.write("")
st.subheader("📉 Depreciation")

depreciation_percent = (
    (present_price - prediction) / present_price * 100
    if present_price > 0 else 0
)

st.progress(
    min(max(depreciation_percent / 100, 0), 1)
)

st.write(
    f"**Vehicle has depreciated by {depreciation_percent:.1f}%**"
)

# ==========================================================
# AI INSIGHTS
# ==========================================================

st.write("")
st.subheader("🤖 AI Insights")

if car_age <= 3:
    st.success("✅ This is a relatively new vehicle.")

elif car_age <= 7:
    st.info("ℹ️ The vehicle is moderately used.")

else:
    st.warning("⚠️ Older vehicle. Maintenance history becomes more important.")

if kms_driven < 30000:
    st.success("🚗 Low mileage generally supports a higher resale value.")

elif kms_driven < 80000:
    st.info("🛣️ Average mileage for the vehicle's age.")

else:
    st.warning("⚠️ High mileage may reduce resale value.")

if owner == 0:
    st.success("👤 First-owner vehicles are often more attractive to buyers.")

elif owner == 1:
    st.info("👍 Second-owner vehicle.")

else:
    st.warning("⚠️ Multiple previous owners may lower resale value.")

if transmission == "Automatic":
    st.info("⚙️ Automatic transmission may command a premium in many markets.")

if fuel_type == "Diesel":
    st.info("⛽ Diesel vehicles often retain value well for high-mileage usage.")

elif fuel_type == "CNG":
    st.success("🌱 CNG vehicles can appeal to buyers looking for lower fuel costs.")

# ==========================================================
# VEHICLE SCORE
# ==========================================================

st.write("")
st.subheader("🏆 Vehicle Score")

score = 100

score -= car_age * 3
score -= kms_driven / 10000
score -= owner * 5

if score < 0:
    score = 0

if score > 100:
    score = 100

st.progress(score / 100)

st.metric(
    "Overall Score",
    f"{score:.0f}/100"
)

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

report = pd.DataFrame({
    "Field": [
        "Car Name",
        "Manufacturing Year",
        "Fuel Type",
        "Seller Type",
        "Transmission",
        "Owner",
        "KM Driven",
        "Current Price",
        "Predicted Price"
    ],
    "Value": [
        car_name,
        year,
        fuel_type,
        seller_type,
        transmission,
        owner,
        kms_driven,
        present_price,
        prediction
    ]
})

csv = report.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Prediction Report",
    data=csv,
    file_name="car_price_prediction_report.csv",
    mime="text/csv"
)

# ==========================================================
# API RESPONSE
# ==========================================================

with st.expander("📦 View API Response"):
    st.json(result)
    # ==========================================================
# TIPS SECTION
# ==========================================================

st.write("")
st.divider()

st.subheader("💡 Tips for Better Predictions")

tip1, tip2, tip3 = st.columns(3)

with tip1:
    st.info("""
🚘 **Vehicle Age**

Newer vehicles usually have a higher resale value.
""")

with tip2:
    st.info("""
🛣️ **Mileage**

Lower mileage generally increases resale value.
""")

with tip3:
    st.info("""
📑 **Ownership**

First-owner cars are typically more valuable.
""")

# ==========================================================
# FEATURES
# ==========================================================

st.write("")
st.subheader("⭐ Features")

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.success("⚡ Fast Prediction")

with f2:
    st.success("🤖 Machine Learning")

with f3:
    st.success("🌐 FastAPI Backend")

with f4:
    st.success("📊 Interactive Dashboard")

# ==========================================================
# JSON PAYLOAD
# ==========================================================

with st.expander("📦 JSON Payload Sent to API"):
    st.json(payload)

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

st.write("")
st.divider()

left, center, right = st.columns(3)

with left:

    st.markdown("""
### 🧠 Machine Learning

- Linear Regression
- Feature Engineering
- Model Serialization
- Scikit-Learn
""")

with center:

    st.markdown("""
### ⚙ Backend

- FastAPI
- REST API
- JSON Request
- Uvicorn
""")

with right:

    st.markdown("""
### 🎨 Frontend

- Streamlit
- Glassmorphism UI
- Interactive Charts
- Responsive Layout
""")

# ==========================================================
# FOOTER
# ==========================================================

st.write("")
st.divider()

st.markdown(
"""
<div style='text-align:center;padding:20px;'>

<h3>🚗 AI Car Price Prediction</h3>

<p>
Predict your vehicle's resale value instantly using Machine Learning.
</p>

<p>
Developed with ❤️ by <b>Santosh Mahanta</b>
</p>

<p>
Python • Streamlit • FastAPI • Scikit-Learn • Machine Learning
</p>

</div>
""",
unsafe_allow_html=True
)