import pandas as pd
import matplotlib.pyplot as plt

def process_data(input_file, output_file, age_threshold=30):
    try:
        # Read the dataset from the CSV file
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: File '{input_file}' is empty.")
        return
    except pd.errors.ParserError:
        print(f"Error: Unable to parse '{input_file}'. Make sure it's a valid CSV file.")
        return

    # Calculating summary statistics
    summary_stats = df.describe()

    # Data filtering based on specific criteria (age)
    filtered_data = df[df['Age'] > age_threshold]

    # Generating a histogram
    plt.hist(df['Salary'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.show()

    # Save the processed data to a new CSV file
    filtered_data.to_csv(output_file, index=False)

    print(f"Data processing complete. Results saved to '{output_file}'.")
    print("\nSummary Statistics:")
    print(summary_stats)

if __name__ == "__main__":
    # Provide the input and output file paths
    input_file_path = "sample_data.csv"
    output_file_path = "processed_data.csv"

    # Call the process_data function
    process_data(input_file_path, output_file_path)
