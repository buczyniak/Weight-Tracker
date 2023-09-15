import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def show_charts():
    # Read data from the Excel file
    file_path = "Weight Tracker.xlsx"
    df = pd.read_excel(file_path)

    # Get the list of columns (excluding the 'Date' column)
    columns = df.columns[1:]

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Calculate the number of rows and columns for subplots
    num_cols = 3
    num_rows = (len(columns) + num_cols - 1) // num_cols

    # Create subplots for all columns
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 4 * num_rows))

    # Set font size and font name
    font_size = 6
    font_name = 'Times New Roman'
    plt.rc('font', size=font_size, family=font_name)

    # Create a line chart for each column
    for i, col in enumerate(columns):
        row_idx = i // num_cols
        col_idx = i % num_cols

        axes[row_idx, col_idx].plot(df['Date'], df[col], marker='o', markersize=3, linestyle='-')
        axes[row_idx, col_idx].set_xlabel('Date', fontsize=font_size)
        axes[row_idx, col_idx].set_ylabel(col, fontsize=8)
        # axes[row_idx, col_idx].set_title(f'{col} over time', fontsize=font_size)
        # axes[row_idx, col_idx].grid(True)
        axes[row_idx, col_idx].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        axes[row_idx, col_idx].tick_params(axis='both', which='major', labelsize=font_size)

    # Remove any empty subplots
    if len(columns) < num_rows * num_cols:
        for i in range(len(columns), num_rows * num_cols):
            fig.delaxes(axes.flatten()[i])

    # Adjust layout and spacing
    plt.tight_layout()
    #
    # # Save the combined chart to a file
    # combined_chart_filename = "combined_line_chart.png"
    # plt.savefig(combined_chart_filename)

    plt.show()
