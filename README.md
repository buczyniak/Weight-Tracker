# Weight-Tracker
![weight_tracker1](https://github.com/buczyniak/Weight-Tracker/assets/78871310/9a8f48c3-af6e-4f9e-8326-ab48ff4f6af3)

## Introduction to Weight Tracker:

The Weight Tracker is a user-friendly GUI application designed to help individuals monitor and track their weight-related 
measurements over time. This application allows users to input and save their weight, body fat percentage, muscle mass, 
neck circumference, biceps size, chest size, waist size, belly size, hip size, thigh size, calf size, and visceral fat 
measurement data. The Weight Tracker then calculates and displays the differences between the current and previous records 
for each measurement, enabling users to monitor their progress and identify trends.

The Weight Tracker also provides insightful visualizations in the form of line charts for each of the recorded measurements 
over time. These charts allow users to visualize their weight and body measurements' historical trends, aiding in identifying 
patterns and progress:

![weight_tracker2](https://github.com/buczyniak/Weight-Tracker/assets/78871310/5854c21d-b53a-42ca-8a65-f38a06485476)

All records are saved in Excel file:

![tracker3](https://github.com/buczyniak/Weight-Tracker/assets/78871310/6c1f3ebc-91e1-4ad1-a4b2-24470123ebe3)

## Explanation of the Code:

The Weight Tracker consists of two Python files: "main.py" and "charts.py." Let's explore the functionality of each section:

### "main.py" - GUI Application:

This file handles the graphical user interface (GUI) of the Weight Tracker application. It utilizes the Tkinter library to 
create a user-friendly interface with input fields, labels, and buttons.

* Function: get_difference()

  * This function calculates the differences between the most recent weight-related measurements and the previous recorded
    measurements stored in the "Weight Tracker.xlsx" Excel file. It then updates the corresponding labels on the GUI to
    display these differences, indicating whether each measurement has increased or decreased compared to the last record.

* Function: save_values()

  * When the user clicks the "Save values" button, this function is triggered. It retrieves the input values from the entry fields 
    (weight, body fat percentage, muscle mass, etc.) and saves this data to the "Weight Tracker.xlsx" Excel file.
  * If the file already exists, the function reads the existing data into a pandas DataFrame, appends the new data, and then saves 
    it back to the file. If the file doesn't exist, a new DataFrame is created and saved.
  * After saving the data, it displays a message confirming that the data was successfully saved.
  * The function also calls get_difference() to update the difference labels on the GUI.

* Tkinter GUI Setup:

  * The code sets up the main Tkinter window, configures its appearance, and defines the elements such as labels, entry fields, and 
    buttons.
  * Users can enter their weight and various body measurements into the provided entry fields.
  * The "Save values" button triggers the save_values() function to store the data and update the difference labels.
  * There is a label to display the result of the data save operation.
  * Two additional buttons, "Close window" and "Show charts," are added after data is saved. The "Close window" button allows users 
    to exit the application, while the "Show charts" button displays historical line charts for each recorded measurement.

### "charts.py" - Chart Visualization:

This file contains the necessary functions to generate line charts based on the data stored in the "Weight Tracker.xlsx" Excel file.

* Function: show_charts()
  * This function reads the data from the "Weight Tracker.xlsx" file into a pandas DataFrame.
  * It converts the 'Date' column to the datetime format for proper chart visualization.
  * The function then creates line charts for each of the recorded measurements (weight, body fat percentage, etc.) over time.
  * Each chart is displayed on the same plot, organized in rows and columns to accommodate all measurements efficiently.
  * The charts are annotated with proper labels and date formatting to ensure clarity and readability.
  * If there are fewer measurements than subplots, the function removes any empty subplots to optimize the layout.
  * The charts are presented using the plt.show() function from the matplotlib library, allowing users to visualize their weight tracking
    progress.

## Summary
In conclusion, the Weight Tracker application offers users an easy and effective way to monitor and track their weight and body
measurements. The GUI interface enables users to input data conveniently, and the application automatically calculates differences
and presents insightful line charts to visualize their progress over time. This tool is well-suited for individuals looking to
maintain a healthy lifestyle, track fitness goals, and make data-driven decisions to achieve their desired body composition.
