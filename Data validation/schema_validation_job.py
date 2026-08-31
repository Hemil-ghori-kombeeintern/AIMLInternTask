import pandas as pd

INPUT_FILE = "employee1.csv"

EXPECTED_COLUMNS = [
    "employee_id", "name", "age", "city",
    "department", "salary", "joining_date", "email"
]

ALLOWED_CITIES = ["Surat", "Ahmedabad", "Mumbai", "Pune", "Delhi"]
ALLOWED_DEPARTMENTS = ["AI/ML", "MERN", "DATA"]


def validate_schema(df):
    errors = []

    missing = []
    for c in EXPECTED_COLUMNS:
        if c not in df.columns:
            missing.append(c)

    extra = []
    for c in df.columns:
        if c not in EXPECTED_COLUMNS:
            extra.append(c)
            
    if df.empty:
        errors.append("Dataset is empty.")
    if missing:
        errors.append(f"Missing columns: {missing}")
    if extra:
        errors.append(f"Unexpected columns: {extra}")

    return errors


def validate_required(df):
    errors = []
    for col in EXPECTED_COLUMNS:
        if col in df.columns:
            count = df[col].isna().sum()
            if count:
                errors.append(f"{col}: {count} missing value(s).")
    return errors


def validate_duplicates(df):
    errors = []

    if df["employee_id"].duplicated().any():
        ids = df.loc[
            df["employee_id"].duplicated(keep=False),
            "employee_id"
        ].unique().tolist()
        errors.append(f"Duplicate employee_id: {ids}")

    count = df.duplicated().sum()
    if count:
        errors.append(f"{count} duplicate row(s) found.")

    return errors


def validate_types(df):
    errors = []

    if not pd.api.types.is_numeric_dtype(df["employee_id"]):
        errors.append("employee_id must be numeric.")

    if not pd.api.types.is_numeric_dtype(df["age"]):
        errors.append("age must be numeric.")

    if not pd.api.types.is_numeric_dtype(df["salary"]):
        errors.append("salary must be numeric.")

    return errors


def validate_ranges(df):
    errors = []

    bad_age = (~df["age"].between(18, 100)).fillna(False)
    if bad_age.any():
        errors.append("Age must be between 18 and 100.")

    bad_salary = (df["salary"] < 0).fillna(False)
    if bad_salary.any():
        errors.append("Salary cannot be negative.")

    return errors


def validate_categories(df):
    errors = []

    bad_city = (~df["city"].isin(ALLOWED_CITIES)).fillna(False)
    if bad_city.any():
        errors.append(
            "Invalid city value(s): "
            + str(df.loc[bad_city, "city"].dropna().unique().tolist())
        )

    bad_department = (
        ~df["department"].isin(ALLOWED_DEPARTMENTS)
    ).fillna(False)

    if bad_department.any():
        errors.append(
            "Invalid department value(s): "
            + str(df.loc[
                bad_department, "department"
            ].dropna().unique().tolist())
        )

    return errors


def validate_dates(df):
    errors = []

    converted = pd.to_datetime(
        df["joining_date"],
        errors="coerce"
    )

    invalid = (
        converted.isna() &
        df["joining_date"].notna()
    ).sum()

    if invalid:
        errors.append(f"{invalid} invalid date value(s).")

    return errors


def validate_emails(df):
    errors = []

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    invalid = ~df["email"].astype("string").str.match(
        pattern,
        na=False
    )

    if invalid.any():
        errors.append(
            f"{invalid.sum()} invalid email value(s)."
        )

    return errors


def validate_row_count(df):
    if len(df) < 10:
        return ["Dataset contains fewer than 10 rows."]
    return []


def validate_data(df):
    errors = validate_schema(df)

    if not set(EXPECTED_COLUMNS).issubset(df.columns):
        return errors

    errors += validate_required(df)
    errors += validate_duplicates(df)
    errors += validate_types(df)
    errors += validate_ranges(df)
    errors += validate_categories(df)
    errors += validate_dates(df)
    errors += validate_emails(df)
    errors += validate_row_count(df)

    return errors



df = pd.read_csv(INPUT_FILE)

errors = validate_data(df)

print("=" * 60)
print("DATA VALIDATION RESULT")
print("=" * 60)

if errors:
    print("VALIDATION FAILED")
    print(f"Total errors: {len(errors)}\n")

    for i, error in enumerate(errors, 1):
        print(f"{i}. {error}")

    print("\nDo NOT load this dataset.")
else:
    print("VALIDATION PASSED")
    print("Dataset is ready to load.")
