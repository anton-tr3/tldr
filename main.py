import openai
import os
from flask import Flask, request, render_template

openai.api_key = os.environ.get('OPENAI_KEY')

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Hello</h1>"

@app.route("/tldr/", methods=['POST', 'GET'])
def tldr():
    if request.method == 'POST':
        message = request.form.get('input')
        openaiQuery = message

        response = openai.Completion.create(
            engine = "curie",
            prompt = openaiQuery + '\ntl;dr:',
            temperature = 0.3,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.2,
            presence_penalty=0.0,
        )
        prompt=openaiQuery + '\n\n tl;dr: \n'
        print(prompt)
        answer = response.choices[0]["text"]
        
        return render_template('tldr-output.html').format(answer)

    return render_template('tldr-landing.html')
        
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)