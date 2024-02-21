import random

from flask import session, request, redirect, url_for

from app.api import bp


@bp.route('/verify_truth', methods=['POST'])
def verify_truth():
    """Function to check if the user predicts the next random number correctly"""

    # Get the guess from the user
    guess = request.form.get('guess', None)
    if guess is None:
        return redirect(url_for('main.index', error="No Onepass found!"))

    # Convert the guess to an integer
    try:
        guess = int(guess)
    except:
        return redirect(url_for('main.index', error="Onepass must be a integer!"))

    # Generate a random seed if one is not provided
    seed = random.randint(9897, 109313)
    if "seed" in session:
        try:
            seed = int(session["seed"])
        except:
            print("WARNING: Secret key breached!")  # TODO: Implement logging
            return redirect(url_for('main.index', error="What how did you find the secret key?"))
    else:
        session["seed"] = seed

    # Generate a random number from seed
    seededRandom = random.Random(seed)
    generated = seededRandom.randint(0, 100000)
    
    # Set and return the generated number
    session["seed"] = generated

    # Check if the guess is correct
    if guess == generated:
        session["instate"] = True
        return redirect(url_for('main.list_ministries'))
    else:
        return redirect(url_for('main.index', error="Incorrect Onepass entered!"))
