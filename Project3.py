import requests

API_KEY = 'WFZIS351NY5T9JDF'

# Function to fetch and validate stock data
def get_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()

        # Check if the API request was successful and the symbol is valid
        if 'Error Message' in data:
            return False, "Invalid stock symbol. Please try again."
        elif 'Note' in data:
            return False, "API limit reached. Please wait before trying again."
        elif 'Time Series (Daily)' not in data:
            return False, "Unexpected error. Please try again."
        else:
            return True, "Stock symbol is valid."
    
    except requests.exceptions.RequestException as e:
        return False, f"Error fetching data: {str(e)}"

# Function to validate the selected chart type
def validate_chart_type(chart_type):
    valid_chart_types = ['line', 'bar']  # Supported chart types

    if chart_type not in valid_chart_types:
        return False, f"Invalid chart type. Available options are: {', '.join(valid_chart_types)}."
    else:
        return True, f"Chart type '{chart_type}' selected."

def main():
    # Step 1: Prompt for stock symbol and validate
    while True:
        symbol = input("Enter the stock symbol: ").upper()
        is_valid, message = get_stock_data(symbol, API_KEY)
        
        if is_valid:
            print("Stock symbol validated successfully!")
            break
        else:
            print(f"Error: {message}")

    # Step 2: Display available chart types
    print("\nAvailable chart types:")
    print("1. Line Chart (line)")
    print("2. Bar Chart (bar)")
    
    # Step 3: Prompt for chart type and validate
    while True:
        chart_type = input("Enter the chart type (line/bar): ").lower()
        is_valid, message = validate_chart_type(chart_type)
        
        if is_valid:
            print(message)
            break
        else:
            print(f"Error: {message}")
    
    # Temporary feedback until we get the other functions in
    print(f"\nYou have selected the stock symbol '{symbol}' and chart type '{chart_type}'.")

if __name__ == "__main__":
    main()
