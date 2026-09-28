from bs4 import BeautifulSoup
import pandas as pd

# Input HTML report
html_file = "InteropHtmlLog_07_13_2026_151557.html"

# Output Excel file
excel_file = "Interop_Report.xlsx"

# Read HTML
with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
    soup = BeautifulSoup(f, "html.parser")

data = []

# Find all result sections
for result_section in soup.find_all("td", class_="results"):

    # Find all tables inside the result section
    tables = result_section.find_all("table")

    for table in tables:
        rows = table.find_all("tr")

        # Look for tables containing Name/Value/Expected/Actual/Result columns
        if rows:
            headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]

            if headers == ["Name", "Value", "Expected", "Actual", "Result"]:

                for row in rows[1:]:
                    cols = row.find_all("td")

                    if len(cols) == 5:
                        data.append({
                            "Name": cols[0].get_text(strip=True),
                            "Value": cols[1].get_text(strip=True),
                            "Expected": cols[2].get_text(strip=True),
                            "Actual": cols[3].get_text(strip=True),
                            "Result": cols[4].get_text(strip=True)
                        })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Validation_Results", index=False)

print(f"Excel file generated: {excel_file}")
print(f"Total rows exported: {len(df)}")