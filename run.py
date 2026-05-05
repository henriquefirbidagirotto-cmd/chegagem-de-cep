from flask import Flask
from app import creater_app

app = creater_app()


if __name__ == '__main__':
    app.run(debug=True)