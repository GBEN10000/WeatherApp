from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class WeatherApp(App):

    def build(self):
        self.title = 'Weather App'
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Enter city name:")
        self.city_input = TextInput(hint_text="City Name")
        self.result_label = Label(text="Weather will be displayed here")
        self.fetch_button = Button(text="Fetch Weather")
        self.fetch_button.bind(on_press=self.fetch_weather)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.city_input)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.fetch_button)
        return self.layout

    def fetch_weather(self, instance):
        city_name = self.city_input.text
        if city_name:
            # Construct the URL for weather data based on user input
            url = f'https://wttr.in/{city_name}?format=%C+%t+%w'

            # Send an HTTP GET request to the weather URL
            res = requests.get(url)

            # Check if the request was successful
            if res.status_code == 200:
                # Print the weather data
                self.result_label.text = res.text
            else:
                self.result_label.text = f"Unable to fetch weather data for {city_name}. Please check the city name and try again."
        else:
            self.result_label.text = "Please enter a city name."

if __name__ == "__main__":
    WeatherApp().run()
