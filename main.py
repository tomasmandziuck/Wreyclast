from json.tool import main
from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True) # emmpieza el webserver y el debug true es que cada vez que hacemos un cambio lo arranca de nuevo
