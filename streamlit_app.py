import streamlit as st
import datetime


# --- Page Config ---
st.set_page_config(page_title="Golf Tracker", layout="centered")

# --- Style and Theme ---
PRIMARY_COLOR = "#004d00"
TEXT_COLOR = "#ffffff"
HIGHLIGHT_COLOR = "#ffcc00"
ACCENT_COLOR = "#eeeeee"

st.markdown(
    f"""
    <style>
        .stButton>button {{
            background-color: {PRIMARY_COLOR};
            color: {TEXT_COLOR};
            border-radius: 10px;
            height: 3em;
            width: 100%;
            margin: 0.2em 0;
            font-weight: bold;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Session state init ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- Navigation ---
def nav_buttons():
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ New Round"):
            st.session_state.page = "new_round"
        if st.button("📁 My Rounds"):
            st.session_state.page = "my_rounds"
    with col2:
        if st.button("📊 Analysis"):
            st.session_state.page = "analysis"
        if st.button("⚙️ Settings"):
            st.session_state.page = "settings"

# --- Page: Home ---
if st.session_state.page == "home":
    st.title("🏌️ Golf Tracker App")
    st.subheader("Track your rounds, analyse your trends, and improve your game.")
    nav_buttons()

# --- Page: New Round ---
elif st.session_state.page == "new_round":
    st.title("➕ New Round")
    nav_buttons()

    st.subheader("Round Information")
    course_name = st.text_input("Course Name")
    handicap = st.number_input("Handicap", 0, 54, value=18)
    tee_type = st.selectbox("Tee Type", ["Back", "Regular", "Front"])
    weather = st.selectbox("Weather Conditions", ["Sunny", "Cloudy", "Windy", "Rainy", "Other"])
    playing_partners = st.text_input("Playing Partners (optional)")
    date_played = st.date_input("Date Played", datetime.date.today())

    st.subheader("Hole-by-Hole Data")
    hole_data = []
    for i in range(1, 19):
        with st.expander(f"Hole {i}"):
            par = st.selectbox(f"Par", [3, 4, 5], key=f"par_{i}")
            yardage = st.number_input("Yardage", 50, 800, key=f"yard_{i}")
            score = st.number_input("Score", 1, 20, key=f"score_{i}")
            putts = st.number_input("Putts", 0, 5, key=f"putts_{i}")
            penalty = st.number_input("Penalty Strokes", 0, 5, key=f"penalty_{i}")
            notes = st.text_input("Hole Notes (optional)", key=f"notes_{i}")

            hole_data.append({
                "hole": i,
                "par": par,
                "yardage": yardage,
                "score": score,
                "putts": putts,
                "penalty": penalty,
                "notes": notes
            })

    if st.button("📥 Submit Round"):
        st.success("✅ Round submitted! (Data storage coming soon)")
        st.session_state.page = "home"

# --- Page: My Rounds ---
elif st.session_state.page == "my_rounds":
    st.title("📁 My Rounds")
    nav_buttons()
    st.info("This page will show a history of your rounds with filters and breakdowns. (Coming soon)")

# --- Page: Analysis ---
elif st.session_state.page == "analysis":
    st.title("📊 Game Analysis")
    nav_buttons()
    st.info("Visual stats will appear here: fairways hit, GIR %, putting avg, and more. (Coming soon)")

# --- Page: Settings ---
elif st.session_state.page == "settings":
    st.title("⚙️ Settings")
    nav_buttons()

    st.subheader("Preferences")
    distance_unit = st.radio("Distance Unit", ["Yards", "Metres"])
    preferred_shape = st.text_input("Preferred Shot Shape (e.g., Draw, Fade, Straight)")
    handicap_set = st.number_input("Update Handicap", 0, 54)

    st.subheader("Your Bag")
    bag = st.multiselect(
        "Select Your Clubs",
        ["Driver", "3 Wood", "5 Wood", "3 Hybrid", "4 Hybrid",
         "Irons 3–9", "PW", "AW", "SW", "LW", "Putter"],
        default=["Driver", "3 Wood", "5 Wood", "Irons 3–9", "PW", "SW", "Putter"]
    )

    st.subheader("Course Management")
    st.text("Course saving/editing features coming soon.")

    st.success("✅ Settings saved! (Placeholder)")
