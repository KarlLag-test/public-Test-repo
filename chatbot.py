import sys
import datetime
import requests

class Chatbot:
    def __init__(self):
        self.user_name = None
        self.last_intent = None
        self.weather_api_key = "c0f388bcde9d8478b3f4ed3ada4210c7"


    def detect_intent(self, user_input):
        user_input = user_input.lower().strip()
        if any(greet in user_input for greet in ["hello", "hi", "hey"]):
            return "greet"
        elif any(bye in user_input for bye in ["bye", "exit", "goodbye"]):
            return "bye"
        elif "help" in user_input:
            return "help"
        elif "weather" in user_input:
            return "weather"
        elif "time" in user_input:
            return "time"
        elif "my name is" in user_input:
            return "set_name"
        elif "name" in user_input:
            return "ask_name"
        else:
            return "unknown"
        

    def get_weather(self, location: str):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.weather_api_key}&units=metric"

        try:
            response = requests.get(url, timeout=5)
            data = response.json()
            if data.get("cod") != 200:
                return "I couldn't retrieve the weather information. Please check the city name."
            weather = data["weather"][0]["description"]
            temp    = data["main"]["temp"]
            return f"The weather in {location} is currently '{weather}' with a temperature of {temp}°C."
        
        except Exception as e:
            return "There was an error retrieving the weather information."
                
    def respond(self, user_input):
        intent = self.detect_intent(user_input)
        self.last_intent = intent

        if intent == "greet":
            return "Hello! How can I assist you today?"
        
        elif intent == "bye":
            return "Goodbye! Have a wonderful day!"

        elif intent == "help":
            return ("I'm a more advanced chatbot. You can greet me, ask about the weather, "
                    "ask for the current time, tell me your name, or say 'bye' to exit.")

        elif intent == "weather":
            city = user_input.split("in")[-1].strip()
            if city and len(user_input.split()) > 1:
                return self.get_weather(city)
            else:
                return "Please specify a city to get the weather information. You can tell me by saying 'Weather in <city>'"

        elif intent == "time":
            now = datetime.datetime.now().strftime("%H:%M:%S")
            return f"The current time is {now}."

        elif intent == "ask_name":
            if self.user_name:
                return f"Your name is {self.user_name}."
            else:
                return "I don't know your name yet. You can tell me by saying 'My name is ...'"

        elif intent == "set_name":
            name = user_input.lower().split("my name is")[-1].strip()
            if name:
                self.user_name = name.capitalize()
                return f"Nice to meet you, {self.user_name}!"
            else:
                return "Please tell me your name after 'My name is ...'."

        else:
            return "I'm not sure how to respond to that. Type 'help' for options."


def main():
    bot = Chatbot()
    print("Welcome to the Advanced Rule-Based Chatbot! Type 'bye' or 'exit' to quit.")
    while True:
        user_input = input("You: ")
        response = bot.respond(user_input)
        print("Bot:", response)
        if bot.last_intent == "bye":
            break


if __name__ == "__main__":
    main()
