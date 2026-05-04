# 📝 Weather Search Program (Python + Tkinter + API Handling)

A simple **Weather searching application with a graphical user interface (GUI)** built using Python, Tkinter and free API.
This app allows users to search the weather of a city in any country by names, showing from the temperature to pressure and humidity.


![alt text](<Weather App Intial Screenshot (632).png>)   

![alt text](<Weather app Working Screenshot (633).png>)

---

## 🚀 Features

* ➕ Search a city by name
* ✏️ Display temperature and description of weather with icon
* 🖥️ User-friendly GUI built with Tkinter

---

## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI)
* requests (API handling)
* Pillow (Image displaying)

---

## 📂 Project Structure

```
.
├── Themes          #Theme used for GUI  
    └──violet.json
├── App.py          # Main application file                 
└── Readme.md       # Project documentation
```

---

## ▶️ How to Run

1. **Clone the repository**

```
git clone https://github.com/GishanPulindu/Weather-App.git
cd weather-application
```

2. **Run requirnment.txt in terminal**

```
pip install -r requirnment.txt
```


3. **Run the application**

```
python App.py
```

---

## 🧠 How It Works

* Use your Openweather API key in the code to gather information from API

* Type name of the desired city in the entry box and press search

* The gathered information will be filtered and displayed as below

  ```
    tkinter Frame 1 - Temperature, weather description, icon, country and city
    tkinter Frame 2 - Wind speed, pressure, humidity, visibility, min and max temperature
    ```

---

## ⚠️ Notes

* Make sure to put your Openweather API key first in api_key variable, **if not the app wont work!!**
* If you have no API Key https://openweathermap.org/guide#openweather_api_overview, create it from this website.

* If you dont have the theme used here download it from here, https://github.com/a13xe/CTkThemesPack (Violet theme)

---

## 🔥 Future Improvements

* Add search functionality
* Add task filtering (Completed / Pending)
* Improve UI design
* Use checkboxes instead of text for completion
* Add due dates and priorities

---

## 💡 What I Learned

* Building GUI applications using Tkinter
* Handling API and Python libraries
* Handling user input and events
* Structuring a real-world Python project

---

## 📌 Version

**v1.0** – Basic GUI Wather applocation with simple display feature of temperature

---

## 🤝 Contributing

This is a personal learning project, but suggestions and improvements are welcome!

Used Assets
Custom Tkinter Theme - https://github.com/a13xe/CTkThemesPack
API                  - https://openweathermap.org/guide#openweather_api_overview

---

## 📜 License

This project is open-source and free to use.
