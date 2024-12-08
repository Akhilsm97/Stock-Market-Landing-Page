# from flask import Flask, render_template,request, jsonify

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Render the initial form page (index.html)
#     return render_template('index2.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     # Access form data
#     name = request.form.get('name')
#     email = request.form.get('email')
#     messages = request.form.get('messages')
#     print(f"Name: {name}, Email: {email}, Message: {messages}")

    
#     if name and email and messages:
#         # Pass data to index2.html for rendering
#         return render_template('index2.html', name=name, email=email)
#     else:
#         return jsonify({"error": "Missing name or email"}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)