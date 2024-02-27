from flask import render_template, request, session, redirect, url_for, render_template_string
import random

from app.main import bp


BLACKLIST = ['\'', '\"', ' ', '[', ']']

ministries = {
    'minitrue': {
        'name': 'Ministry of Truth (Minitrue)',
        'description': 'Responsible for propaganda and revisionism. Adjusts historical records to match the Party\'s official narratives.',
        'icon': 'fa-file-alt'
    },
    'miniluv': {
        'name': 'Ministry of Love (Miniluv)',
        'description': 'Oversees torture and brainwashing. Ensures loyalty to Big Brother through fear.',
        'icon': 'fa-heart-broken'
    },
    'miniplenty': {
        'name': 'Ministry of Plenty (Miniplenty)',
        'description': 'Controls the economy, rationing and distributing goods, and often creating artificial scarcities.',
        'icon': 'fa-cogs'
    },
    'minipax': {
        'name': 'Ministry of Peace (Minipax)',
        'description': 'In charge of war and defense. Constantly engages in wars to keep society in a state of fear and dependence.',
        'icon': 'fa-shield-alt'
    }
}

with open("app/templates/ministry.html") as f:
    TEMPLATE = f.read()

@bp.route('/')
def index():
    # Redirect user to minis if logged in
    if "instate" in session:
        if session["instate"] == True:
            return redirect(url_for('main.list_ministries'))

    # Set seed if it doesn't exist
    if "seed" not in session:
        session["seed"] = random.randint(9897, 109313)

    # Get any error message from the URL
    error = request.args.get('error', None)
    return render_template('index.html', error=error)


@bp.route('/minis')
def list_ministries():
    # Check if user is logged in
    if "instate" not in session:
        return redirect(url_for('main.index', error="You are not logged in!"))

    if session["instate"] != True:
        return redirect(url_for('main.index', error="You are not logged in!"))

    return render_template('ministries.html', ministries=ministries)


@bp.route('/mini')
def get_ministry():
    # Check if user is logged in
    if "instate" not in session:
        return redirect(url_for('main.index', error="You are not logged in!"))

    if session["instate"] != True:
        return redirect(url_for('main.index', error="You are not logged in!"))

    # Get ministry name from URL
    ministry = request.args.get('ministry', None)
    if ministry is None:
        return "No 'ministry' argument provided.", 400

    # Find ministry
    if ministry not in ministries:
        ministry_obj = {
            'name': 'The ministry of ' + ministry + ' does not exist!',
            'description': 'None found.',
            'icon': 'fa-exclamation-triangle'
        }
    else:
        ministry_obj = ministries[ministry]

    # Check & warn if name contains blacklisted characters
    for char in BLACKLIST:
        if char in ministry:
            ministry_obj = {
                'name': 'Your use of unauthorized terms violates Newspeak standards.',
                'description': 'Correct immediately or face consequences.',
                'icon': 'fa-exclamation-triangle'
            }
            break

    # Render template
    template = TEMPLATE.replace("NAME", ministry_obj['name'])
    template = template.replace("DESC", ministry_obj['description'])
    template = template.replace("ICON", ministry_obj['icon'])

    return render_template_string(template)
