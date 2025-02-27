# **Smart Transit: AI-Powered Bus Navigation System** 🚌🚀

### **An interactive AI-powered bus tracking system with smart routing and delay alerts.**

## **📌 Overview**
The **Smart Transit AI-Powered Bus Navigation System** is designed to help users **track Baltimore bus routes, find stops, and get AI-powered route suggestions**. The project integrates:
- **🚏 Real-time Bus Stop Visualization** using **Folium**
- **💬 AI Chatbot for Smart Routing** using **OpenAI GPT-4 & LangChain**
- **📊 Efficient Data Handling** with **SQLite**
- **⚠️ Live Delay Alerts** via **simulated real-time updates**
- **🌐 Web App Interface** built with **Streamlit**

This project serves as a **proof of concept** for real-time transit solutions.

---

### 🚀 Features

### 🔹 1. AI-Powered Smart Routing
- Users can ask for the best bus route between two stops  
- Powered by GPT-4 via LangChain  

### 🔹 2. Interactive Map
- Visualizes bus stops on a **Folium-based map**  
- Helps users explore available routes  

### 🔹 3. Delay Alerts
- Simulates real-time bus delays  
- Alerts users about estimated wait times  

### 🔹 4. User-Friendly Interface
- Built using **Streamlit**  
- Runs locally with minimal setup  


## **🛠️ Tech Stack**
| Category                | Technologies Used |
|-------------------------|------------------|
| **Programming**         | Python |
| **Frameworks & APIs**   | Streamlit, OpenAI API, LangChain |
| **Database**            | SQLite |
| **Visualization**       | Folium, Pandas |
| **Machine Learning**    | GPT-4 (LLM) |
| **Deployment**          | Streamlit Cloud (Optional) |

---

##⚙️ Installation & Setup

### 🔹 1. Clone the Repository

git clone https://github.com/sujeeth26/Smart-Transit-AI-Powered-Bus-Navigation.git
cd Smart-Transit-AI-Powered-Bus-Navigation

### 2. Install Dependencies

pip install -r requirements.txt

### 3.Set Up API Key (Securely)

Create a .env file and add your OpenAI API Key:OPENAI_API_KEY=your_openai_api_key_here

### 4.Run the Application

streamlit run app.py



## **📂 Project Structure**
```plaintext
📦 Smart-Transit-AI-Powered-Bus-Navigation
│-- 📜 app.py                 # Main Streamlit app
│-- 📜 bus_routes.db           # SQLite database
│-- 📜 Bus_Routes_file.csv     # Raw bus routes data
│-- 📜 Bus_Stops_file.csv      # Raw bus stops data
│-- 📜 .env                    # Environment file (not pushed to GitHub)
│-- 📜 requirements.txt        # Required dependencies
│-- 📜 README.md               # Project documentation (this file)











