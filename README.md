
# Food Tracker

## Overview

Food Tracker is a Streamlit application that helps you track your calorie intake, explore recipes, and store your food consumption data. It leverages the power of the Groq's Llama model to provide nutritional information and generate recipes, and uses a MySQL database to store your data.

## Features

*   **Calorie Tracking:** Get detailed nutritional information (protein, fat, carbs, fiber, cholesterol) for various food items using Groq's Llama model.
*   **Recipe Generation:** Generate simple, step-by-step recipes for preparing your favorite foods.
*   **Interactive Chat:** Chat with the application to ask questions about the generated recipes and food preparation.
*   **Database Storage:** Store food items and their nutritional information in a MySQL database for future reference and tracking.
*   **Data Visualization:** View your historical food data, including daily summaries, in an interactive Streamlit interface.


## Technologies Used

*   **Python:**  The primary programming language.
*   **Streamlit:**  For building the interactive web application.
*   **Langchain-Groq:**  For interacting with the Groq's Llama model.
*   **Pandas:**  For data manipulation and analysis.
*   **MySQL:**  For storing food data.
## What Do You Need?

Before running the application, you need to perform the following setup steps:

*  #### Create a Groq API Key:

    Sign up for an account at [Groq](https://groq.com/)

    Obtain an API key from your Groq account dashboard.

*  #### Configure Database:

    Install [MySQL](https://www.mysql.com/downloads/) if you don't have it already.




## Setup

All dependencies are listed in the `requirements.txt` file.  You can install them using pip:

```bash
pip install -r requirements.txt
```

### Then follow these steps:

* Create a new database in MySQL to store your food data.
* Update the DatabaseManager.py file with your MySQL database connection details
* Create a .env file in the root directory of the project.
* Add your Groq API key to the .env file:

## Ready to Run?

execute this command in the terminal by going into the root directory
```bash
streamlit run main.py
```
## Support

For support, suggestions or code related errors [raise an issue](https://github.com/kzeus03/FoodTracker/issues).

