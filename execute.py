import pandas as pd

# Read CSV files
csv2_data = pd.read_csv("test.csv")
csv3_data = pd.read_csv("database.CSV")
empty_csv_data = pd.read_csv("unathorized_vechile.CSV")

# Extract rows with valid license numbers
valid_rows = csv2_data.dropna(subset=["license_number", "license_number_score"])

# Get the indices of the rows with the maximum license_number_score for each car_id
max_indices = valid_rows.groupby("car_id")["license_number_score"].idxmax()

# Get the rows corresponding to these indices
best_license_rows = valid_rows.loc[max_indices]

# Initialize a dictionary to store authorization status for each car_id
authorization_status = {}

# Check authorization status for each car_id
for car_id, group in best_license_rows.groupby("car_id"):
    authorized = group["license_number"].isin(csv3_data["license_number"]).all()
    license_number = group["license_number"].iloc[0]  # Get the license plate number
    authorization_status[car_id] = {"Authorized": authorized, "LicenseNumber": license_number}

# Display authorization status, car_id, and license plate number for each car_id
for car_id, status in authorization_status.items():
    print(f"Car ID: {car_id}, Authorized: {status['Authorized']}, License Plate: {status['LicenseNumber']}")

# If unauthorized, store the license numbers and car IDs in the empty CSV file
if any(not status["Authorized"] for status in authorization_status.values()):
    unauthorized_rows = []
    for car_id, status in authorization_status.items():
        if not status["Authorized"]:
            unauthorized_rows.append({"car_id": car_id, "license_number": status["LicenseNumber"]})
    
    unauthorized_df = pd.DataFrame(unauthorized_rows)
    unauthorized_df.to_csv("unathorized_vechile.CSV", index=False, mode="a", header=False)
