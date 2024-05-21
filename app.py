import streamlit as st 
import numpy as np 
import pickle

def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()


st.title("HeartSync :two_hearts:")
st.subheader("Analyzing Compatibility for Romantic Connections :revolving_hearts:")
st.image(r"C:\Users\ali\Downloads\images\close-up-cartoon-character-couple (1).png",width=300, use_column_width=True)


st.sidebar.image(r"C:\Users\ali\Downloads\images\3d-cartoon-character.png", use_column_width=True)
st.sidebar.subheader('Welcome to HeartSync :revolving_hearts:')
st.sidebar.write('Explore our Streamlit app designed to analyze compatibility and predict romantic connections. Developed with passion by Mohammad Ali, this tool combines data science with a touch of romance.')
st.sidebar.title(':memo: Author')
st.sidebar.subheader('Mohammad Ali')
st.sidebar.title('Connect :link:')
st.sidebar.link_button('Linkdin :large_blue_diamond:', url='https://www.linkedin.com/in/mohdali02/')
st.sidebar.link_button('Git-hub :black_large_square:', url='github.com/Mohd-Ali2')



# Select gender using Streamlit's selectbox
gender_str = st.selectbox("Select gender :male_sign: :female_sign:", ('Male', 'Female'))

# Convert selected gender to numerical representation
if gender_str == 'male':
    gender = 1
else:
    gender = 0

# Collect other inputs
age = st.number_input('Enter your Age', min_value=0, max_value=100)
income = st.number_input("What's your income (in USD) ? :moneybag:", min_value=0, max_value=900000)
goal = st.number_input('How many goals do you have?', min_value=0, max_value=10)
career = st.selectbox('Select career', ('Student', 'Hacker', 'Engineer', 'Doctor', 'busniessman', 'Professor'))
attractiveness = st.number_input("Rate your attractiveness on a scale of 1 to 10 ? :grinning_face_with_star_eyes:", min_value=0, max_value=10)
sincerity = st.number_input("Rate your sincerity on a scale of 1 to 10 ? :moyai:", min_value=0, max_value=10)
intelligence = st.number_input("Rate your intelligence on a scale of 1 to 10 ? :bulb:", min_value=0, max_value=10)
fun = st.number_input("Rate how funny you are on a scale of 1 to 10 ? :laughing:", min_value=0, max_value=10)
ambition = st.number_input("Rate your ambition level on a scale of 1 to 10 ? :brain:", min_value=0, max_value=10)
shared_interests = st.number_input("Rate your shared interests on a scale of 1 to 10 ? :thinking_face:", min_value=0, max_value=10)
like = st.number_input("Rate how much you are liked by others on a scale of 1 to 10 ? :thumbsup:", min_value=0, max_value=10)
probability = st.number_input("Rate the probability of success on a scale of 1 to 10 ? :gloves:", min_value=0, max_value=10)

met = st.selectbox("Have you met before or not ? :part_alternation_mark:", ('Yes', 'No')) 
if met == 'Yes':
    met_value = 1
else:
    met_value = 0

# Create the input data array
input_data = [gender, age, income, goal, attractiveness, sincerity, intelligence, fun, ambition, shared_interests, like, probability, met_value]

# Ensure the career input is not missing if it is required by your model
#if 'career' in input_data:
    #input_data.append(career)

# Ensure input_data has the correct number of features expected by the model
if st.button('Predict'):
    try:
        np_arr = np.asarray(input_data)
        reshape = np_arr.reshape(1, -1)  # Reshape for a single sample
        prediction = model.predict(reshape)

        if prediction == 1:
            st.image(r"C:\Users\ali\Downloads\_3bdc59b5-39e6-4785-9802-0bde1ba9db4a.png", width=180)
            st.success("Congratulations! You have a high compatibility score.")
        else:
            st.image(r"C:\Users\ali\Downloads\_b9453bf1-8f52-4063-96bd-d05ef8c1146e-removebg.png", width=180)
            st.warning("Unfortunately, your compatibility score is low.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

