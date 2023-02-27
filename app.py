import streamlit as st
import streamlit as st

# find more emoji's here (https://www.webfx.com/tools/emoji-cheat-sheet/)

st.set_page_config(page_title = "Calculate Your BMI - Standard BMI Calculator", layout = "wide")


# ----- HEADER SECTION -----



st.header("""Calculate Your Body Mass Index""")
page_names = ["STANDARD", "METRIC"] # we can do this with st.tabs also

page = st.sidebar.radio("BMI", page_names)
st.sidebar.header(page)

st.write("""
Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women.
View the BMI tables or use the tool below to compute yours.
""")
st.write("""
                * Enter your weight and height using standard or metric measures.
                * Select "Compute BMI" and your BMI will appear below.
""")


# ----- WHAT I DO -----

if page == "STANDARD":
    st.subheader("STANDARD")

    st.subheader("Enter your age") 
    with st.container():
        column1, column2 = st.columns([1,3])
        with column1:
            Age = st.text_input("AGE")

    st.subheader("Please enter your height in feet and inches")

    with st.container():      
        column1, column2, column3 = st.columns([1,1,2]) 
                    
        with column1:
            FEET = st.number_input("FEET", step = 1.0, value = 5.0)
        with column2:
            INCHES = st.number_input("INCHES", step = 1.0, value = 3.0)
        
                

    with st.container():
    
        left_column, right_column = st.columns(2)        
        
        st.subheader("Enter your weight in pounds")
        
        left_column, right_column = st.columns(2)
        with left_column:
           POUNDS = st.number_input("POUNDS", step = 1.0, value = 125.0)
            


    INCHES, POUNDS  = int(INCHES), int(POUNDS)
    
    HEIGHT = (FEET * 12) + INCHES
    Your_BMI = round((POUNDS * 703) / (HEIGHT * HEIGHT), 2)
    
    BMI = Your_BMI

    
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:    
            st.subheader("Body Mass Index")
            result = st.button("CHECK BMI")
        
            
            if result:
                st.write("Your BMI is : " + str(BMI))
                
            else:
                st.write(str(0))

    with st.container():
            left_column,right_column = st.columns(2)
            with left_column:
                st.subheader("""BMI Classification :smile: """)
            with left_column:
                st.markdown("*Under 18.5*")

            with left_column:
                st.markdown("*18.5 - 24.9*")

            with left_column:
                st.markdown("*25 - 29.9*")
            
            with left_column:
                st.markdown("*30 or greater*")
            
            with right_column:
                st.subheader("""Health Risk :exclamation:""")

            with right_column:
                st.markdown("Under Weight - Minimal")

            with right_column:
                st.markdown("Normal weight - Normal")

            with right_column:
                st.markdown("Over Weight - Increased")
            with right_column:
                st.markdown("Obeese - :red[High]")             
                    

else:
    st.subheader("METRIC")
    st.subheader("Enter your age") 
    with st.container():
        column1, column2 = st.columns([1,3])
        with column1:
            Age = st.text_input("AGE")
    st.subheader("Please enter your height in metres")
    with st.container():      
        left_column, right_column = st.columns(2)
    
    with left_column:
        HEIGHT = st.number_input("METRES", step = 0.01, value = 1.80)
            

    with st.container():
    
        left_column, right_column = st.columns(2)        
        
        st.subheader("Enter your weight in kilograms")
        
        left_column, right_column = st.columns(2)
        with left_column:
           KGS = st.number_input("KGS", step = 1.0, value = 65.0)

    
    Your_BMI = round( KGS / (HEIGHT * HEIGHT), 2)
    
    BMI = Your_BMI

    
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:    
            st.subheader("Body Mass Index")
            result = st.button("CHECK BMI")

            
            
            if result:
                st.write("Your BMI Is : " + str(BMI))
                
            else:
                st.write(str(0))

    with st.container():
            left_column,right_column = st.columns(2)
            with left_column:
                st.subheader("""BMI Classification :smile: """)
            with left_column:
                st.markdown("*Under 18.5*")
            
            with left_column:
                st.markdown("*18.5 - 24.9*")

            with left_column:
                st.markdown("*25 - 29.9*")
            
            with left_column:
                st.markdown("*30 or greater*")
            
            with right_column:
                st.subheader("""Health Risk :exclamation:""")

            with right_column:
                st.markdown("Under Weight - Minimal")

            with right_column:
                st.markdown("Normal weight - Normal")

            with right_column:
                st.markdown("Over Weight - Increased")
            with right_column:
                st.markdown("Obeese - :red[High]")

