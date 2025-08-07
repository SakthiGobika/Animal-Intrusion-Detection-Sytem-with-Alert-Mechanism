
from transformers import pipeline

# Load the conversational pipeline with DialoGPT-medium model
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def get_response(user_input):
    responses = chatbot(user_input)         # Pass user input directly
    return responses[0]['generated_text']  # Extract the generated response text

app = Flask(__name__)       # Create Flask app

@app.route("/")             # Home page route
def home():
    return render_template("index.html")  # Load frontend

@app.route("/get", methods=["GET"])       # API to handle messages
def get_bot_response():
    user_input = request.args.get('msg')  # Get input from browser
    bot_reply = get_response(user_input)  # Get chatbot reply
    return jsonify({"reply": bot_reply})  # Return reply as JSON

if __name__ == "__main__":
    app.run(debug=True)
