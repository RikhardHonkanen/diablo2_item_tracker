import ui.main_window as main_window
from context import AppContext

def main():  # Main entry point
    AppContext.initialize()
    main_window.start()
    return 0
    
if __name__ == "__main__":    
    main()
    