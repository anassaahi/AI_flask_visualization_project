# 🚗 AI Car Price Visualization Project

An interactive Flask-based AI visualization tool that allows users to analyze car pricing trends using dynamic graphs. This project empowers users to explore car data by selecting specific columns from a dropdown menu, automatically updating the visual output accordingly.

---

## 📌 Project Objective

To help users and data enthusiasts visually analyze relationships between different car attributes (such as engine size, fuel type, seller type) and car prices. Users can gain insights through bar charts, pie charts, and scatter plots that are generated based on selected features — all without needing to write code.

---

## 📊 Features

- ✅ Dropdown menu for column selection
- 📈 Dynamic graphs (Bar Chart, Pie Chart, Scatter Plot)
- 🔄 Real-time data rendering using Flask and Jinja2
- 📊 Clean and beginner-friendly UI for interacting with data

---

## 📁 Project Structure

```
car_price_app/
│
├── app.py                # Flask backend logic
├── car_data.csv          # Main dataset
│
├── templates/            # HTML templates
│   └── index.html        # Home page with dropdown and plot
│
├── static/               # Static files like CSS
│   └── styles.css        # Optional CSS styling
│
├── screenshots/          # Screenshots used in documentation
│   ├── dropdown.png
│   ├── bar_plot.png
│   ├── pie_chart.png
│   └── scatter_plot.png
│
├── requirements.txt      # Python package dependencies
└── README.md             # Project documentation

yaml
Copy
Edit

```

---

## 🧠 Technologies Used

- Python 3.x
- Flask (Web Framework)
- Pandas (Data Processing)
- Matplotlib (Data Visualization)
- Jinja2 (Template Rendering)
- HTML/CSS (User Interface)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI_flask_visualization_project.git
cd AI_flask_visualization_project/car_price_app
2. Install the dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the application
bash
Copy
Edit
python app.py
4. Open in browser
Visit: http://127.0.0.1:5000

🗂️ Dataset Description
The dataset was self-scraped from PakWheels.com using our own Python web scraping tool. It includes the following columns:
•	Title
•	Model
•	City
•	Distance
•	Engine
•	Fuel Type
•	Price
•	Transmission Type
These features were cleaned and prepared for analysis using regular expressions and string manipulation techniques.


🔍 Learning Outcomes
Understanding of EDA (Exploratory Data Analysis)

Hands-on experience with Flask app development

Working with user input to generate live data visualizations

Plotting and labeling graphs dynamically using Pandas + Matplotlib

Bridging frontend and backend in a Python web app

🔧 Future Improvements
Support for multiple column selections

Integration with seaborn or plotly for advanced visuals

Responsive design for mobile devices

Export charts as images or PDFs

Add statistical summaries next to graphs

🎓 Academic Use
This project was created as part of the Artificial Intelligence Lab Project for the university course. It demonstrates practical use of data visualization, user interaction, and backend rendering — all important for foundational AI applications.

🤝 Contributing
Pull requests and forks are welcome. For any suggestions or feature requests, feel free to open an issue.

📜 License
This project is open-source and free to use under the UET License
