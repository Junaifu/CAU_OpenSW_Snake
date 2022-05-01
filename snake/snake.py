from app import App
from scenes.menuScene import MenuScene

if __name__ == "__main__":
    app = App(1080, 720, MenuScene())
    app.run()
