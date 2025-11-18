import streamlit as st
import pandas as pd

# ---------------------------------------------
# 1. DATA (Excel actions and formulas)
# ---------------------------------------------
data = {
    "Action": [
        "How to do a vertical search?",
        "How to do a horizontal search?",
        "How to find value by exact match?",
        "How to get value by row and column number?",
        "How to find the position of value in a range?",
        "How to pick a value from a list?",
        "How to return a cell address?",
        "How to fetch value from text reference?",
        "How to combine first and last names?",
        "How to join text with a delimiter?",
        "How to count cells greater than 100?",
        "How to sum values above 200?",
        "How to average marks greater than 50?",
        "How to apply IF statement?",
        "How to assign grades using nested IF?",
        "How to get current date and time?",
        "How to extract current date?",
        "How to extract month name from a date?",
        "How to calculate age in years?",
        "How to round a number to 2 decimals?",
        "How to round up a number?",
        "How to round down a number?",
        "How to get maximum value from range?",
        "How to get minimum value from range?",
        "How to calculate average of range?",
    ],
    "Formula": [
        "=VLOOKUP(1001,A1:D10,4,FALSE)",
        "=HLOOKUP(\"Sales\",A1:J2,2,FALSE)",
        "=XLOOKUP(\"Apple\",A2:A20,B2:B20)",
        "=INDEX(A1:C10,3,2)",
        "=MATCH(\"Orange\",A2:A10,0)",
        "=CHOOSE(2,\"Red\",\"Blue\",\"Green\")",
        "=ADDRESS(5,5)",
        "=INDIRECT(\"B2\")",
        "=CONCAT(A1,\" \",B2)",
        "=TEXTJOIN(\", \",TRUE,A2:A5)",
        "=COUNTIF(A2:A20,\">100\")",
        "=SUMIF(A2:A20,\">200\")",
        "=AVERAGEIF(A2:A20,\">50\")",
        "=IF(A2>=35,\"Pass\",\"Fail\")",
        "=IF(A2>90,\"A\",IF(A2>=75,\"B\",\"C\"))",
        "=NOW()",
        "=TODAY()",
        "=TEXT(A2,\"MMMM\")",
        "=DATEDIF(A2,TODAY(),\"Y\")",
        "=ROUND(A2,2)",
        "=ROUNDUP(A2,0)",
        "=ROUNDDOWN(A2,0)",
        "=MAX(A2:A20)",
        "=MIN(A2:A20)",
        "=AVERAGE(A2:A20)",
    ]
}

df = pd.DataFrame(data)

# ---------------------------------------------
# 2. STREAMLIT UI
# ---------------------------------------------
st.set_page_config(page_title="Excel Formula Helper", layout="wide")

st.title("🔍 Excel Formula Helper")
st.write("Search any Excel action below to instantly see its formula.")

# Search box
query = st.text_input("Search an action or keyword", "").lower()

# Filter results
if query:
    filtered_df = df[df["Action"].str.lower().str.contains(query)]
else:
    filtered_df = df

# Show results
st.dataframe(filtered_df, use_container_width=True)

# Copy formula section
st.subheader("📋 Copy Formula")
selected_action = st.selectbox("Select an action to copy its formula:", df["Action"])
formula = df[df["Action"] == selected_action]["Formula"].values[0]

st.code(formula, language="text")
