from ui.widgets import StreamlitUi
from config import JSON_DIR

if __name__ == "__main__":
    ui = StreamlitUi(dir_with_jsons=JSON_DIR)
    ui.run()