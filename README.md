
# Weatherapp built in Django

This project is a simple weather application built using Django, which allows users to check the current weather conditions for a location.

## Features

- Display current weather information based on user input (city, zip code, etc.).
- Use of OpenWeatherMap API for fetching weather data.
- Basic frontend to display weather information.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd weatherapp-django
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   
   Create a `.env` file in the root directory with the following:

   ```plaintext
   OPENWEATHERMAP_API_KEY=<your-api-key>
   ```

   Replace `<your-api-key>` with your OpenWeatherMap API key.

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000` in your web browser.

## Usage

- Enter a city name  in the provided form and click 'Submit'.
- The application will fetch and display the current weather information for the entered location.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.


### Notes:
- Replace `<repository-url>` with the actual URL of your Git repository.
- Make sure to update the installation instructions and other details based on the specific setup and features of your Weatherapp built in Django.
