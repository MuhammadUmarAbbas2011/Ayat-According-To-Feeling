
# Ayat According to Feeling (Django Project)

This is a Django web application that allows users to input their feelings and receive Ayat (verses) from the Quran related to their feeling. The application uses Google's Gemini AI model to generate content based on the user's input.

## Features

- **User Input**: The user can input their current feeling.
- **Ayat Generation**: The application uses Google's Gemini AI model to generate Quranic verses (Ayat) related to the user's feeling.
- **No Sympathy, Just Ayat**: The app focuses solely on providing Ayat and their translations, according to the specified feeling.
- **Error Handling**: If no related Ayat are found for a given feeling, it will inform the user.

## Requirements

- **Python 3.8+**
- **Django**
- **Decouple** (to manage environment variables like the Google API key)
- **Google GenAI SDK** (for content generation using Google's Gemini model)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/MuhammadUmarAbbas2011/Ayat-According-To-Feeling.git
   cd Ayat-According-To-Feeling
   ```

2. **Set up a Virtual Environment:**

   If you don't have `virtualenv` installed, install it first:

   ```bash
   pip install virtualenv
   ```

   Then create a virtual environment:

   ```bash
   virtualenv venv
   ```

3. **Activate the Virtual Environment:**

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   Install all the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure you have a `requirements.txt` file with the necessary dependencies:

   ```
   Django>=3.0
   python-decouple
   google-genai
   ```

5. **Set up Environment Variables:**

   - Create a `.env` file in the root of your project directory and add your Google API key as follows:

     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

6. **Run the Development Server:**

   Finally, run the Django development server:

   ```bash
   python manage.py runserver
   ```

   You can now access the application in your browser at `http://127.0.0.1:8000`.

## Code Overview

### `views.py`

The main functionality of the application is implemented in the `response` view:

```python
from django.shortcuts import render
from decouple import config
from google import genai

def response(request):
    if request.method == 'POST':
        feeling = request.POST.get('feeling')
        print(feeling)

        apikey = config('GOOGLE_API_KEY')

        client = genai.Client(api_key=apikey)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f" I Am Feeling {feeling} Give Me Ayat According To The Feeling I Have Told You Only 2 Ayat Just Give Me AYAT And There Translation Don't Give Any Sympathy And only Give Accorfing To The Feeling Nothing Else Jst According To The Feeling  If There Is No Ayat Related To The Felling Then Say No Ayat Related To The Feeling Then Only Say No Ayat Found For You'r Following Feeling",
        )
        print(response.text)
        context = {
            'data': response.text
        }
        return render(request, 'response.html', context)
    return render(request, 'response.html')
```

### Explanation:

- **POST Request Handling**: When the user submits their feeling, the application takes the input and generates a request to Google's Gemini AI model.
- **Google API Client**: The API key is fetched from the environment variable (`GOOGLE_API_KEY`) using the `python-decouple` library. The Gemini AI client is then initialized.
- **Model Interaction**: The content is sent to the Gemini model with a custom prompt to generate two Ayat and their translations based on the feeling provided by the user.
- **Rendering the Response**: The AI response is rendered on the `response.html` page.

### `response.html`

This is the HTML file where the generated Ayat (verses) will be displayed. The data is passed from the view context and is rendered as the content.

### Dependencies

- **django**: A high-level Python Web framework.
- **decouple**: Helps in managing environment variables (like the API key).
- **google-genai**: Google's Gemini AI client to interact with the model.

## Usage

1. **Visit the Home Page**: Go to the local server, and you will see a form asking you for your feeling.
2. **Submit Your Feeling**: Type in your feeling (e.g., happy, sad, anxious) and click submit.
3. **View the Response**: The application will generate 2 Ayat based on your input feeling and display them along with their translation.

## Example:

### Input:

- **Feeling**: "happy"

### Output:

- **Ayat 1**: (Generated Ayat based on "happy")
- **Ayat 2**: (Generated Ayat based on "happy")

If no Ayat is found for the given feeling, the app will display:

- "No Ayat found for your following feeling."

## Contributing

Feel free to fork the repository and submit issues or pull requests for improvements. All contributions are welcome!

## License

This project is licensed under the MIT License 


### Explanation of the README:

1. **Project Overview**: A description of the purpose of the application, its features, and how it works.
2. **Requirements**: Lists the dependencies needed for the project to run.
3. **Installation Instructions**: Step-by-step guide on how to set up the environment and get the project running.
4. **Code Explanation**: Provides an overview of the code, mainly focusing on the `views.py` file.
5. **Usage**: Describes how users can interact with the app.
6. **Contributing & License**: Encourages contributions and mentions licensing.

Let me know if you need any more adjustments or additional sections!
