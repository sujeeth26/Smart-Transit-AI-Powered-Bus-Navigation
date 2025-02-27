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

## **⚙️ Installation & Setup**

### **🔹 1. Clone the Repository**
```bash
git clone https://github.com/sujeeth26/Smart-Transit-AI-Powered-Bus-Navigation.git
cd Smart-Transit-AI-Powered-Bus-Navigation

