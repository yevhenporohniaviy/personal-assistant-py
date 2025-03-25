#!/usr/bin/env python3

from src.assistant import Assistant

def main():
    """
    Entry point of the Personal Assistant application.
    Initializes the assistant and starts the main loop.
    """
    assistant = Assistant()
    assistant.run()

if __name__ == "__main__":
    main()