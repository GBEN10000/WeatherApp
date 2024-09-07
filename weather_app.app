WeatherApp:
    orientation: 'vertical'
    Label:
        text: 'Enter city name:'
    TextInput:
        id: city_input
        hint_text: 'City Name'
    Label:
        id: result_label
        text: 'Weather will be displayed here'
    Button:
        text: 'Fetch Weather'
        on_release: root.fetch_weather()
