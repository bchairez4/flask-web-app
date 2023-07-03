# Brian Chairez
# Flask Pet Adoption Landing Page

from flask import Flask, render_template

app = Flask(__name__)

navbarList = ['Home', 'Adopt', 'About']

@app.route('/')
def index():
    return render_template('index.html', navbarList=navbarList)

@app.route('/adopt')
def adopt():
    adoptionList = [{'img_src': 'static/images/adopt-animal-1.jpg', 'animal': 'dog', 'breed': 'doggy', 'name': 'Fluffy', 'age': 1},
                    {'img_src': 'static/images/adopt-animal-2.jpg', 'animal': 'dog', 'breed': 'doggy', 'name': 'Softy', 'age': 2},
                    {'img_src': 'static/images/adopt-animal-3.jpg', 'animal': 'dog', 'breed': 'doggy', 'name': 'Bruce', 'age': 4},
                    {'img_src': 'static/images/adopt-animal-4.jpg', 'animal': 'cat', 'breed': 'kitty', 'name': 'Nightfall', 'age': 3},
                    {'img_src': 'static/images/adopt-animal-5.jpg', 'animal': 'cat', 'breed': 'kitty', 'name': 'Bucky', 'age': 5},
                    {'img_src': 'static/images/adopt-animal-6.jpg', 'animal': 'cat', 'breed': 'kitty', 'name': 'Mao-San', 'age': 3}]
    return render_template('adopt.html', navbarList=navbarList, adoptionList=adoptionList)

@app.route('/about')
def about():
    return render_template('about.html', navbarList=navbarList)

def main():
    app.run()

if __name__ == '__main__':
    main()
