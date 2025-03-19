from django.shortcuts import render
from decouple import config
from google import genai

def response(request):
    if request.method == 'POST':
        feeling = request.POST.get('feeling')
        print(feeling)

        apikey=config('GOOGLE_API_KEY')

        client = genai.Client(api_key=apikey)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f" I Am Feeling {feeling} Give Me Ayat According To The Feeling I Have Told You Only 2 Ayat Just Give Me AYAT And There Translation Don't Give Any Sympathy And only Give Accorfing To The Feeling Nothing Else Jst According To The Feeling  If There Is No Ayat Related To The Felling Then Say No Ayat Related To The Feeling Then Only Say No Ayat Found For You'r Following Feeling",
        )
        print(response.text)
        context = {
            'data':response.text
        }
        return render (request,'response.html',context)
    return render (request,'response.html')