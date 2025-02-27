# 📦 Core Libraries
import os
import sqlite3
import random
from datetime import datetime, timedelta

# 🔑 Secure API Key Loading
from dotenv import load_dotenv

# 🗺️ Visualization Libraries
import streamlit as st
import folium
from streamlit_folium import st_folium

# 📊 Data Handling
import pandas as pd

# 🤖 OpenAI Integration for Chatbot
import openai
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# =======================
# 📥 Load and Verify CSV Data (Database Creation)
# =======================

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('bus_routes.db')

# Load CSV files into Pandas DataFrames
routes_df = pd.read_csv('Bus_Routes_file.csv')
stops_df = pd.read_csv('Bus_Stops_file.csv')

# Show first few records to verify
print("Routes Data:")
print(routes_df.head())
print("\nStops Data:")
print(stops_df.head())

# Insert data into SQLite tables
routes_df.to_sql('routes', conn, if_exists='replace', index=False)
stops_df.to_sql('stops', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

# =======================
# 🔑 Load the OpenAI API Key
# =======================

# Load the .env file
load_dotenv()

# Check if the key was loaded
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    print("✅ API Key loaded successfully!")
else:
    print("❌ API Key not found.")

# =======================
# 🗺️ Simulate Real-Time Bus Arrivals and Create a Map
# =======================

# Connect to SQLite database
conn = sqlite3.connect('bus_routes.db')
cursor = conn.cursor()

# Enable foreign key constraints
conn.execute('PRAGMA foreign_keys = ON;')

# Fetch bus stops from the database using correct column names (X for longitude, Y for latitude)
cursor.execute('SELECT stop_id, stop_name, Y, X FROM stops LIMIT 100')
stops = cursor.fetchall()

# Simulate estimated arrival time for a bus stop
def get_estimated_arrival(stop_name):
    delay = random.randint(0, 15)  # Random delay in minutes
    estimated_time = datetime.now() + timedelta(minutes=delay)
    formatted_time = estimated_time.strftime("%I:%M %p")
    return f"The bus at {stop_name} is expected to arrive around {formatted_time}."

# Initialize Folium map centered on Baltimore
m = folium.Map(location=[39.2904, -76.6122], zoom_start=13)

# Add bus stops to the map using X and Y as coordinates
for stop in stops:
    folium.Marker(
        location=[stop[2], stop[3]],  # Y (latitude), X (longitude)
        popup=stop[1],
        icon=folium.Icon(icon='bus', prefix='fa')
    ).add_to(m)

# Display map in Streamlit
st.title('🚌 Baltimore Bus Route Tracker')
st_folium(m, width=700, height=500)

# =======================
# 🚨 Simulate Random Delay Alerts
# =======================

# Simulate random bus delays
# Simulate random bus delays
def simulate_delay():
    delayed_stop = random.choice(stops)
    delay_time = random.randint(0, 20)  # Random delay from 0 to 20 minutes
    return delayed_stop[1], delay_time

# Trigger delay alerts
delayed_stop, delay_time = simulate_delay()

# Display warning for major delays
if delay_time >= 5:
    st.warning(f'⚠️ Delay Alert: Bus at {delayed_stop} delayed by {delay_time} minutes.')

# Add user-friendly notification (toast message)
if delay_time == 0:
    st.toast(f"🟢 The bus at {delayed_stop} is arriving on time.", icon="✅")
elif delay_time < 5:
    st.toast(f"🕒 The bus at {delayed_stop} is arriving on time (Minor delay of {delay_time} minutes).", icon="🟡")
else:
    st.toast(f"⏳ Heads up! The bus at {delayed_stop} is delayed by {delay_time} minutes.", icon="🚍")


# =======================
# 🤖 Initialize OpenAI GPT-4 Chatbot
# =======================

# Initialize OpenAI GPT-4 using the correct method
openai.api_key = openai_api_key
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

# Initialize memory for conversation context
memory = ConversationBufferMemory()

# Initialize conversation chain for LLM-based interaction
conversation = ConversationChain(llm=llm, memory=memory)

# Define a function for smart route suggestions using LLM
def smart_route_suggestion(from_stop, to_stop):
    prompt = f"Find the best bus route from {from_stop} to {to_stop} considering any delays."
    response = conversation.run(prompt)
    return response

# =======================
# 💬 Chatbot Interface for User Interaction
# =======================

# Smart Routing Chatbot with Simulated Real-Time Bus Arrival Times
# 💬 Enhanced Smart Routing Chatbot with Simulated Real-Time Bus Arrival Times
st.title("💬 Smart Routing Chatbot")
user_query = st.text_input(
    'Ask for a route or bus arrival time'
)

if user_query:
    # 🚏 Improved logic for checking bus stop arrival queries
    found_stop = None
    for stop in stops:
        if stop[1].lower() in user_query.lower():  # Check if stop name is mentioned
            found_stop = stop[1]
            break

    # If the user asks about a bus arrival time
    if found_stop:
        estimated_arrival = get_estimated_arrival(found_stop)
        st.success(f"🕒 {estimated_arrival}")

    # 🛣️ If the user asks for a route suggestion
    elif 'from' in user_query.lower() and 'to' in user_query.lower():
        parts = user_query.lower().split('from')[1].split('to')
        from_stop = parts[0].strip()
        to_stop = parts[1].strip()
        route_response = smart_route_suggestion(from_stop, to_stop)
        st.success(f'🧭 Suggested Route: {route_response}')

    # 🤖 General queries
    else:
        response = conversation.run(user_query)
        st.write('🤖 Chatbot Response:', response)
