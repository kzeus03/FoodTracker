import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host = "", # include your host eg: localhost or server host
    user = "", # include your username
    password = "", # include your password
    database = "" # include your database name
)

cursor = conn.cursor()

def create_meals_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meals (
        id INT AUTO_INCREMENT PRIMARY KEY,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        food_item VARCHAR(255),
        protein FLOAT,
        carbs FLOAT,
        fiber FLOAT,
        fat FLOAT,
        cholesterol FLOAT
    );
""")

def store_meal_data(Food_Item,df):
    create_meals_table()
    print("Table created")
    data = {row["Category"]:row['Grams'] for _,row in df.iterrows()}
    protein = data.get("Protein", 0)
    fat = data.get("Fat", 0)
    carbs = data.get("Carbs", 0)
    fiber = data.get("Fiber", 0)
    cholesterol = data.get("Cholesterol", 0)
    print("Protein : ",protein)
    print("Data extracted")
    cursor.execute("""
            INSERT INTO meals (Food_Item,Protein,Carbs,fiber,fat,cholesterol) VALUES (%s,%s,%s,%s,%s,%s)       
        """,(Food_Item,protein,carbs,fiber,fat,cholesterol)
    )
    conn.commit()
    print("Data stored successfully")

def fetch_all_meals():
    # get all data
    cursor.execute("SELECT * FROM meals")
    records = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    df_1 = pd.DataFrame(records, columns=column_names)

    #get daily data
    cursor.execute("""
        SELECT
            DATE(created_at) AS date, 
            SUM(protein) AS protein, 
            SUM(carbs) AS carbs, 
            SUM(fat) AS fat, 
            SUM(fiber) AS fiber, 
            SUM(cholesterol) AS cholesterol
        FROM meals
        GROUP BY DATE(created_at);   
    """)
    daily_records = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    df_2 = pd.DataFrame(daily_records,columns=column_names)

    #get today's data
    cursor.execute("""
        SELECT
            DATE(created_at) AS date, 
            SUM(protein) AS protein, 
            SUM(carbs) AS carbs, 
            SUM(fat) AS fat, 
            SUM(fiber) AS fiber, 
            SUM(cholesterol) AS cholesterol
        FROM meals
        WHERE DATE(created_at)=CURDATE()
        GROUP BY DATE(created_at);      
    """)
    today_records=cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    df3 = pd.DataFrame(today_records,columns=column_names)
    return df_1,df_2,df3



