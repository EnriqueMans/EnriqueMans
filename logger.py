import logging

# Create a custom logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Set the logging level

# Create handlers
file_handler = logging.FileHandler('app.log')  # Log to a file
console_handler = logging.StreamHandler()      # Log to the console

# Set level for each handler
file_handler.setLevel(logging.DEBUG)
console_handler.setLevel(logging.ERROR)  # Only log errors and above to console

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Sample function to demonstrate logging
def divide_numbers(a, b):
    try:
        logger.info(f"Dividing {a} by {b}")
        result = a / b
        logger.info(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Attempted to divide by zero")
        return None

def main():
    logger.info("Program started")
    num1 = 10
    num2 = 0

    # Log a debug message
    logger.debug(f"num1: {num1}, num2: {num2}")

    result = divide_numbers(num1, num2)

    if result is None:
        logger.warning("Division failed")

    logger.info("Program finished")

if __name__ == "__main__":
    main()