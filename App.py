from json import JSONDecodeError
from logging import exception

import customtkinter
import requests
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image
from io import BytesIO


def weather_gui():
    def get_weather(city):
        api_key = " "  # Your API Key goes here
        base_url = "https://api.openweathermap.org/data/2.5/weather"

        params = {"q": city, "appid": api_key, "units": "metric"}

        try:
            response = requests.get(base_url, params)
            data = response.json()

            if response.status_code == 200:
                temperature = round(data["main"]["temp"])
                feels_like = round(data["main"]["feels_like"])
                descr = data["weather"][0]["description"]
                wind = data["wind"]["speed"]
                humid = data["main"]["humidity"]
                visible = data["visibility"]
                country = data["sys"]["country"]
                pressure = data["main"]["pressure"]
                icon = data["weather"][0]["icon"]
                tempMin = round(data["main"]["temp_min"])
                tempMax = round(data["main"]["temp_max"])
                return {"temperature": temperature,"feelsLike": feels_like,"description": descr,"windSpeed": wind,"humidity": humid,"visibility": visible,"country": country,"pressure": pressure, "icon": icon, "temp_min": tempMin, "temp_max": tempMax}
            else:
                return f"Error Code: {response.status_code}"
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error Occurred: {e}")
        except JSONDecodeError as e:
            print(f"JSON Error Occurred: {e}")
        except exception as e:
            print(f"Error Occurred: {e}")

    def show_weather():
        city = main_entry.get()
        if not city:
            CTkMessagebox(title="Error", message="City Name is required", icon="cancel")

        display_values = get_weather(city)
        url_icon = display_values["icon"]
        url = f"https://openweathermap.org/img/wn/{url_icon}@2x.png"
        response_icon = requests.get(url)
        icon_data = BytesIO(response_icon.content)
        icon_img = Image.open(icon_data)

        icon_image = customtkinter.CTkImage(light_image=icon_img, dark_image=icon_img, size= (80, 80))
        image_label = customtkinter.CTkLabel(master=weather_frame, image=icon_image, text="")
        image_label.grid(row=2, column=0, sticky= "nsew")

        city_label.configure(text=f"{city}, {display_values["country"]}")
        temp_label.configure(text=f"{display_values["temperature"]}°C")
        feel_label.configure(text=f"Feels like {display_values["feelsLike"]}°C")
        descr_label.configure(text=f"{display_values["description"]}")
        wind_label.configure(text=f"Wind Speed: {display_values["windSpeed"]} km/h")
        humid_label.configure(text=f"Humidity: {display_values["humidity"]}%")
        visible_label.configure(text=f"Visibility: {display_values["visibility"]} km")
        pressure_label.configure(text=f"Pressure: {display_values["pressure"]} mb")
        minimum_label.configure(text=f"Min. Temperature: {display_values["temp_min"]}°C")
        maximum_label.configure(text=f"Max. Temperature: {display_values["temp_max"]}°C")

        main_entry.delete(0, "end")

    root = CTk()
    root.title("Weather App")
    root.resizable(width=False, height=False)
    root.geometry("600x300")
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("Themes/violet.json")


    weather_frame = customtkinter.CTkFrame(master=root, width=300, height=200)
    weather_frame.grid(row=0, column=0, padx=20, pady=20)

    weather_frame.grid_propagate(False)

    temp_frame = customtkinter.CTkFrame(master=root, width=230, height=200)
    temp_frame.grid(row=0, column=4, padx=10, pady=10)

    temp_frame.grid_propagate(False)

    city_label = customtkinter.CTkLabel(master=weather_frame, font=("Roboto", 20), text="--, --")
    city_label.grid(padx=10, pady=3)

    temp_label = customtkinter.CTkLabel(master=weather_frame, font=("Roboto", 60), text="--°C")
    temp_label.grid(padx=10)

    feel_label = customtkinter.CTkLabel(master=weather_frame, font=("Roboto", 18), text="Feels like --°C")
    feel_label.grid(row=1, column=1, padx=10)

    descr_label = customtkinter.CTkLabel(master=weather_frame, font=("Roboto", 18), text="--")
    descr_label.grid(row=2, column=1, padx=10)

    wind_label = customtkinter.CTkLabel(master=temp_frame, font=("Roboto", 18), text="Wind Speed: --")
    wind_label.place(relx=0.5, rely=0.1, anchor="center")

    humid_label = customtkinter.CTkLabel(master=temp_frame, font=("Roboto", 18), text="Humidity: --")
    humid_label.place(relx=0.5, rely=0.25, anchor="center")

    visible_label = customtkinter.CTkLabel(master=temp_frame, font=("Roboto", 18), text="Visibility: --")
    visible_label.place(relx=0.5, rely=0.4, anchor="center")

    pressure_label = customtkinter.CTkLabel(master=temp_frame, font=("Roboto", 18), text="Pressure: --")
    pressure_label.place(relx=0.5, rely=0.55, anchor="center")

    minimum_label = customtkinter.CTkLabel(master=temp_frame, font=("Roboto", 18), text="Min. Temperature: --")
    minimum_label.place(relx=0.5, rely=0.7, anchor="center")

    maximum_label = customtkinter.CTkLabel(master=temp_frame, font=("Roboto", 18), text="Max. Temperature: --")
    maximum_label.place(relx=0.5, rely=0.85, anchor="center")

    main_entry = customtkinter.CTkEntry(root, font=("Roboto", 20), placeholder_text="Enter City Name")
    main_entry.grid(row=1, column=0, padx=20, sticky="nsew")

    enter_button = customtkinter.CTkButton(master=root, text="Search", font=("Roboto", 20), command=show_weather, fg_color="transparent",border_width=1, border_color="grey", corner_radius=25, hover_color="#5b469e")
    enter_button.grid(row=1, column=4, padx=20, sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    weather_gui()