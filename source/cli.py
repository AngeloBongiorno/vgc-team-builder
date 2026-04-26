from agent import client


while True:
    try:
        command = input("Enter a command (or 'exit' to quit): ")
        if command.lower() == 'exit':
            print("Exiting the CLI. Goodbye!")
            break
        else:
            print(f"You entered: {command}")
    except KeyboardInterrupt:
        print("\nExiting the CLI. Goodbye!")
        break
