import streamlit as st
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide",
)

API_URL = "https://car-price-prediction-lsgu.onrender.com/predict"

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

.main-title{
text-align:center;
font-size:45px;
font-weight:bold;
color:white;
margin-bottom:5px;
}

.sub-title{
text-align:center;
font-size:18px;
color:#dddddd;
margin-bottom:30px;
}

.card{
background:rgba(255,255,255,0.12);
padding:25px;
border-radius:20px;
backdrop-filter:blur(15px);
box-shadow:0px 8px 30px rgba(0,0,0,0.35);
margin-bottom:20px;
}

.result{
background:linear-gradient(135deg,#00c853,#64dd17);
padding:30px;
border-radius:18px;
text-align:center;
font-size:30px;
font-weight:bold;
color:white;
box-shadow:0px 8px 25px rgba(0,0,0,0.3);
}

.footer{
text-align:center;
color:#cccccc;
margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------

st.markdown(
"""
<div class="main-title">
🚗 AI Car Price Prediction
</div>

<div class="sub-title">
Predict the resale value of your car using Machine Learning
</div>
""",
unsafe_allow_html=True
)

# -------------------- LAYOUT --------------------

left,right=st.columns([2,1])

with left:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    car_name=st.text_input("Car Name",value="Swift")

    year=st.number_input(
        "Manufacturing Year",
        1990,
        2026,
        2016
    )

    present_price=st.number_input(
        "Current Ex-showroom Price (Lakhs)",
        0.0,
        100.0,
        5.5
    )

    kms_driven=st.number_input(
        "Kilometers Driven",
        0,
        500000,
        35000
    )

    fuel_type=st.selectbox(
        "Fuel Type",
        ["Petrol","Diesel","CNG"]
    )

    seller_type=st.selectbox(
        "Seller Type",
        ["Dealer","Individual"]
    )

    transmission=st.selectbox(
        "Transmission",
        ["Manual","Automatic"]
    )

    owner=st.selectbox(
        "Number of Previous Owners",
        [0,1,2,3]
    )

    st.markdown("</div>",unsafe_allow_html=True)

with right:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    st.metric("Fuel Type",fuel_type)
    st.metric("Transmission",transmission)
    st.metric("Year",year)
    st.metric("KM Driven",f"{kms_driven:,}")

    st.markdown("</div>",unsafe_allow_html=True)

# -------------------- PAYLOAD --------------------

payload={
    "Car_Name":car_name,
    "Year":year,
    "Present_Price":present_price,
    "Kms_Driven":kms_driven,
    "Fuel_Type":fuel_type,
    "Seller_Type":seller_type,
    "Transmission":transmission,
    "Owner":owner
}

# -------------------- BUTTON --------------------

col1,col2,col3=st.columns([1,2,1])

with col2:

    predict=st.button(
        "🚀 Predict Car Price",
        use_container_width=True
    )

# -------------------- PREDICTION --------------------

if predict:

    with st.spinner("🤖 AI is predicting..."):

        try:

            response=requests.post(
                API_URL,
                json=payload,
                timeout=20
            )

            if response.status_code==200:

                result=response.json()

                prediction=result.get(
                    "prediction",
                    result.get(
                        "predicted_price"
                    )
                )

                if prediction is not None:

                    st.markdown(
                    f"""
                    <div class="result">
                    💰 Estimated Selling Price<br><br>
                    ₹ {prediction:.2f} Lakhs
                    </div>
                    """,
                    unsafe_allow_html=True
                    )

                    st.balloons()

                else:

                    st.warning("Prediction key not found.")

                    st.json(result)

            else:

                st.error(f"API Error : {response.status_code}")

                st.code(response.text)

        except Exception as e:

            st.error("Unable to connect to FastAPI Server")

            st.code(str(e))

# -------------------- EXPANDER --------------------

with st.expander("📦 JSON Payload"):

    st.json(payload)

# -------------------- FOOTER --------------------

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit • FastAPI • Scikit-Learn

</div>
""",unsafe_allow_html=True)