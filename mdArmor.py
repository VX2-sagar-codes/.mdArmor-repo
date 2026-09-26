import streamlit as st
st.set_page_config(
   page_title=".mdArmor"
)
st.title("🛡 .mdArmor")
st.divider()
a1, a2 = st.columns(2)
with a1:
    with st.container(border=True):
      style = st.pills(label="Choose your style", options=["for-the-badge", "plastic"], help="for-the-badge means flat look")
      col1, col2 = st.columns(2)
      with col1:
        name = st.text_input("Label")
        label = name.replace(" ", "_")
        logo = st.text_input("Logo")
      with col2:
        name_2 = st.text_input("message")
        message = name_2.replace(" ", "_")
        colour = st.selectbox(label="Colour", options=["blue", "black", "white", "red", "green", "yellow", "pink", "purple", "orange", "indigo"])
if len(label) > 0 and len(message) > 0:
  with a2:
    st.markdown(f"""
    # Requirements

    1. **Colour**: {colour}
    
    2. **Label**: {name}

    3. **Message**: {name_2}
 
    4. **Style**: {style}
    
    5. **Logo**: {logo}

    """)
  script = f"https://img.shields.io/badge/{label}-{message}-{colour}?style={style}&logo={logo}"
  st.code(f"![{label}]({script})")
  st.header("Wanna see how the badge looks like? 😏")
  st.link_button("Check now", script)