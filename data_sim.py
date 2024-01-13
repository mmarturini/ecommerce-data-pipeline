import pandas as pd
from faker import Faker
import random
from datetime import datetime


if __name__=='__main__':    
    faker = Faker()
    num_records = 5
    data = {
        "Product_ID": [random.randint(1000, 9999) for _ in range(num_records)],
        "Product_Name": [faker.word() for _ in range(num_records)],
        "Quantity_Sold": [random.randint(1, 10) for _ in range(num_records)],
        "Sale_Price": [random.uniform(10.0, 1000.0) for _ in range(num_records)],
        "Customer_ID": [random.randint(10000, 99999) for _ in range(num_records)],
        "Purchase_Timestamp": [faker.date_time_between(start_date="-2y", end_date="now") for _ in range(num_records)]
    }
    df = pd.DataFrame(data)
    df.to_csv('ecommerce_sales_data.csv', index=False)
