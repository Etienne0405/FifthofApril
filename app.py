from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message 

# Initialize the Flask application
app = Flask(__name__)

# ==================================
#  FLASK-MAIL CONFIGURATION 
# ==================================
app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False  
app.config('MAIL_USE_SSL') = True

app.config['MAIL_USERNAME'] = 'maria.etienne.official@gmail.com'
app.config['MAIL_PASSWORD'] = 'vpmwiyissaaaphuc' 
app.config['MAIL_DEFAULT_SENDER'] = 'maria.etienne.official@gmail.com'

mail = Mail(app) # Initialize the mail object
# ==================================

# ==================================
#          ENGLISH ROUTES
# ==================================

@app.route('/')
@app.route('/index')
def index():
    """Renders the English homepage."""
    return render_template('index.html')

@app.route('/gigs')
def gigs():
    """Renders the English gigs page."""
    return render_template('gigs.html')

@app.route('/aboutus')
def aboutus():
    """Renders the English About Us page."""
    return render_template('aboutus.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handles the English contact form submission and displays the form."""
    if request.method == 'POST':
        # 1. Capture English form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message_body = request.form.get('message')

        # 2. 📧 EMAIL SENDING LOGIC 📧
        # This will be the email I receive
        msg = Message(
            f"NEW MESSAGE: {subject} (from {name})",
            # Fifth of april's receiving email
            recipients=['maria.etienne.official@gmail.com'] 
        )
        
        # Construct the body of the email
        msg.body = f"""
        Name: {name}
        Sender Email: {email}
        Subject: {subject}
        ---------------------------
        Message:
        {message_body}
        """

        try:
            mail.send(msg)
            print("\n--- SUCCESSFULLY SENT EMAIL ---")
        except Exception as e:
            # If the mail fails, the error will be printed in the terminal
            print(f"\n--- FAILED TO SEND EMAIL: {e} ---")
            
        # 3. Redirect to the English success page
        return redirect(url_for('success'))

    # If GET, render the form
    return render_template('contact.html')

@app.route('/success')
def success():
    """Renders the English success confirmation page."""
    return render_template('success.html')


# ==================================
#           DUTCH ROUTES
# ==================================

@app.route('/index_nl')
def index_nl():
    """Renders the Dutch homepage."""
    return render_template('index_nl.html')

@app.route('/gigs_nl')
def gigs_nl():
    """Renders the Dutch gigs page."""
    return render_template('gigs_nl.html')

@app.route('/aboutus_nl')
def aboutus_nl():
    """Renders the Dutch About Us page."""
    return render_template('aboutus_nl.html')

@app.route('/contact_nl', methods=['GET', 'POST'])
def contact_nl():
    """Handles the Dutch contact form submission and displays the form."""
    if request.method == 'POST':
        # 1. Capture Dutch form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message_body = request.form.get('message') # Renamed variable
        
        # 2. 📧 EMAIL SENDING LOGIC 📧
        msg = Message(
            f"NIEUW BERICHT: {subject} (van {name})",
            recipients=['maria.etienne.official@gmail.com'] # Our email
        )
        
        msg.body = f"""
        Naam: {name}
        E-mail afzender: {email}
        Onderwerp: {subject}
        ---------------------------
        Bericht:
        {message_body}
        """

        try:
            mail.send(msg)
            print("\n--- E-MAIL SUCCESVOL VERZONDEN ---")
        except Exception as e:
            print(f"\n--- E-MAIL IS NIET VERZONDEN: {e} ---")
        
        # 3. Redirect to the Dutch success page
        return redirect(url_for('success_nl'))

    # If GET, render the Dutch form
    return render_template('contact_nl.html')

@app.route('/success_nl')
def success_nl():
    """Renders the Dutch success confirmation page."""
    return render_template('success_nl.html')


if __name__ == '__main__':
    # Run the application
    app.run(debug=True)