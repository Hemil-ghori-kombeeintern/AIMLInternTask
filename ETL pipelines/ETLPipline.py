import pandas as pd
import numpy as np
import os

INPUT_FILE = "sales_input.csv"


def extract(file):
    print("Extracting data...")
    return pd.read_csv(file)


def transform(df):

    df = df.drop_duplicates()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype("string").str.strip()

    for col in ["age", "salary", "quantity", "unit_price"]:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    for col in ["age", "salary", "quantity", "unit_price"]:
        if col in df.columns:
            df[col] = df[col].fillna(
                df[col].median()
            )

    for col in ["sale_date", "joining_date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )
    if "salary" in df.columns:
        df["salary"] = (
            df["salary"]
            .astype("string")
            .str.strip()
            .str.replace("₹", "", regex=False)
            .str.replace(",", "", regex=False)
        )

        df["salary"] = pd.to_numeric(
            df["salary"],
            errors="coerce"
        )

        invalid_salary = df["salary"] < 0
        df.loc[invalid_salary, "salary"] = 0

    if "city" in df.columns:
        df["city"] = df["city"].str.lower().str.strip()

        city_map = {
            "surat": "Surat",
            "ahmedabad": "Ahmedabad",
            "mumbai": "Mumbai",
            "bombay": "Mumbai",
            "pune": "Pune",
            "delhi": "Delhi",
            "new delhi": "Delhi",
            "bangalore": "Bangalore",
            "bengaluru": "Bangalore",
            "chennai": "Chennai",
            "kolkata": "Kolkata",
            "hyderabad": "Hyderabad",
            "jaipur": "Jaipur",
        }

        df["city"] = df["city"].replace(city_map)

    if "gender" in df.columns:
        df["gender"] = df["gender"].str.lower().str.strip()

        gender_map = {
            "m": "Male",
            "male": "Male",
            "f": "Female",
            "female": "Female",
        }

        df["gender"]=df["gender"].replace(gender_map)



    if "quantity" in df.columns and "unit_price" in df.columns:
        df["total_amount"] = (
            df["quantity"] * df["unit_price"]
        )
    if "product" in df.columns:
        df["product"] = (
            df["product"]
            .str.strip()
            .str.title()
        )

        if "sale_date" in df.columns:
            df["sale_date"] = pd.to_datetime(
                df["sale_date"],
                errors="coerce",
                format="mixed"
            )
            df["sale_date"]=df["sale_date"].dt.strftime("%Y-%m-%d")

    return df


def load(df, input_file):
    print("Loading data...")

    directory = os.path.dirname(input_file)
    filename = os.path.basename(input_file)
    output_file = os.path.join(
        directory,
        "cleaned_" + filename
    )

    df.to_csv(
        output_file,
        index=False
    )
    print(f"Output saved: {output_file}")


def run_etl_pipline():

    print("ETL Pipeline Started")
    df = extract(INPUT_FILE)
    print("Original rows:", len(df))
    df = transform(df)
    print("Cleaned rows:", len(df))
    load(df, INPUT_FILE)
    print("ETL Pipeline Completed Successfully!")


if __name__ == "__main__":
    run_etl_pipline()