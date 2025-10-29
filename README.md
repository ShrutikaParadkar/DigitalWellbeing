# 📱 Digital Wellbeing Pattern Analyzer — Detecting Digital Burnout Using Machine Learning

**Python | Streamlit | Machine Learning | Data Preprocessing | Model Deployment**

---

## 👩‍💻 Author
**Shrutika Paradkar**  
📍 Data Scientist | Python | Machine Learning | Power BI | SQL  

##### 🔗 [LinkedIn Profile](https://www.linkedin.com/in/shrutika-paradkar-778a02219/)  
##### 💻 [GitHub Profile](https://github.com/ShrutikaParadkar)

---

## 📘 Project Overview
The **Digital Wellbeing Pattern Analyzer** helps users assess their **risk of digital burnout** by analyzing smartphone usage behavior.  
The model predicts burnout likelihood and provides **personalized recommendations** to improve digital health and productivity.

This project demonstrates:  
- **Data preprocessing & feature engineering** for behavioral datasets  
- **Classification model development and evaluation**  
- **Interactive Streamlit app deployment** for real-time predictions  

---

## 📂 Dataset Description

| **Column Name** | **Description** |
|------------------|------------------|
| `age` | User’s age |
| `gender` | Male / Female / Other |
| `profession` | Occupation type |
| `city_tier` | User’s city category (Tier 1–3) |
| `daily_screen_time_min` | Total daily screen time (minutes) |
| `sleep_hours` | Average sleep duration per day |
| `social_media_time_min` | Social media usage time (minutes) |
| `anxiety_level`, `focus_score`, `mood_score` | Self-assessment scores (0–10) |
| `social_media_ratio` | Derived feature: social_media_time / screen_time |
| `burnout_label` | Target variable (0 = No Burnout, 1 = High Risk) |

---

## 🧩 Project Workflow

### **1️⃣ Data Preprocessing**
- Managed missing values and categorical encoding  
- Engineered features such as `social_media_ratio`  
- Scaled numeric attributes for balanced model performance  

### **2️⃣ Model Development**
- Trained and evaluated models using **Scikit-learn**  
- Tuned hyperparameters using `GridSearchCV()`  
- Selected the best-performing model and serialized it as `burnout_model.pkl`  

### **3️⃣ Streamlit App Development**
- Built an **interactive web app** to take user inputs (age, screen time, mood, etc.)  
- Loaded the trained model using `joblib`  
- Displayed **prediction results, confidence score, and tailored recommendations**  

---

## 🧠 Features
- Real-time **burnout risk prediction**  
- Dynamic **recommendation engine** based on user habits  
- Deployed as a **Streamlit web application**

---

## 🛠️ Tools & Technologies

| **Category** | **Tools Used** |
|---------------|----------------|
| **Programming** | Python 3.12 |
| **Libraries** | pandas, numpy, scikit-learn, joblib, streamlit |
| **Environment** | Jupyter Notebook, VS Code |
| **Version Control** | Git, GitHub |

---

## 💻 How to Run the Project

```bash
# Step 1 — Clone the Repository
git clone https://github.com/YourUsername/Digital_Wellbeing_Analyzer.git
cd Digital_Wellbeing_Analyzer

# Step 2 — Install Required Libraries
pip install streamlit pandas numpy scikit-learn joblib matplotlib seaborn

# Step 3 — Run the Streamlit App
streamlit run Digital_Wellbeing_Analyzer.py

