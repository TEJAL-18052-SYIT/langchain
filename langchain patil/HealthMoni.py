import cohere
import streamlit as st

# Initialize the Cohere client with your API key
cohere_client = cohere.Client('UHow6dUYsAuRHawURFV1AYQFigbbd5odqemqnYWD')  # Replace with your API key

# Streamlit UI
st.title('Health Monitoring and Recommendation System')

st.header("Enter Your Daily Health Data:")

# Input fields for health data
steps = st.number_input('Steps Walked:', min_value=0, max_value=100000, step=500, value=8000)
sleep_hours = st.number_input('Hours of Sleep:', min_value=0.0, max_value=24.0, step=0.5, value=7.0)  # Float values for consistency
water_intake = st.number_input('Water Intake (in liters):', min_value=0.0, max_value=10.0, step=0.1, value=2.5)
calories = st.number_input('Calories Consumed:', min_value=0, max_value=5000, step=50, value=2200)

# Button to generate recommendations
if st.button('Generate Health Recommendations'):
    # Creating a prompt based on user input
    prompt = f"""
    You are a health advisor. Based on the user's health data, provide personalized recommendations for improving their health in areas such as exercise, hydration, diet, and sleep.
    
    Health Data:
    - Steps walked: {steps} steps
    - Hours of sleep: {sleep_hours} hours
    - Water intake: {water_intake} liters
    - Calories consumed: {calories} kcal

    Provide the recommendations:
    """
    
    try:
        # Use Cohere's Language Model to generate recommendations
        response = cohere_client.generate(
            model='command-nightly',  # You can choose other models based on your needs
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )

        # Extracting the generated recommendation
        recommendations = response.generations[0].text.strip()

        # Display the generated health recommendations
        st.subheader("Personalized Health Recommendations:")
        st.write(recommendations)

    except Exception as e:
        # Display an error message if the API call fails
        st.error(f"An error occurred while generating recommendations: {str(e)}")
