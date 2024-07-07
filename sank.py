import plotly.graph_objects as go

# Define the labels
labels = [
    "Revenue from Operations 2023", "Other Income 2023", "Total Income 2023", "Cost of Materials Consumed 2023",
    "Purchase of Stock-in-Trade 2023", "Changes in Inventories 2023", "Employee Benefit Expense 2023",
    "Finance Costs 2023", "Depreciation and Amortisation 2023", "Other Expenses 2023", "Total Expenses 2023",
    "Profit before Tax 2023", "Current Tax 2023", "Deferred Tax Charge 2023", "Profit for the Year 2023",
    "Revenue from Operations 2022", "Other Income 2022", "Total Income 2022", "Cost of Materials Consumed 2022",
    "Purchase of Stock-in-Trade 2022", "Changes in Inventories 2022", "Employee Benefit Expense 2022",
    "Finance Costs 2022", "Depreciation and Amortisation 2022", "Other Expenses 2022", "Total Expenses 2022",
    "Profit before Tax 2022", "Current Tax 2022", "Deferred Tax Charge 2022", "Profit for the Year 2022"
]

# Define the source and target nodes
sources = [
    0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 11, 11, 11, 3, 4, 5, 6, 7, 8, 9, 18, 18, 18, 18, 18, 18, 18, 26, 26, 26
]
targets = [
    2, 2, 11, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 10, 10, 10, 10, 10, 10, 10, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29
]

# Define the values
values = [
    59144, 640, 59784, 19229, 11968, -53, 2665, 101, 1030, 11703, 13079, 2922, 195, 9962, 51193, 393, 51586, 15869, 9274, -19, 2399, 98, 1025, 11167, 11739, 2778, 143, 8818
]

# Define the colors for the nodes and links
node_colors = [
    "blue", "lightblue", "lightgreen", "orange", "yellow", "lightcoral", "lightpink", "lightgrey", "lightcyan", 
    "lightgoldenrodyellow", "lightblue", "lightgreen", "orange", "yellow", "lightcoral", "lightpink", "lightgrey",
    "lightcyan", "lightgoldenrodyellow", "blue", "lightblue", "lightgreen", "orange", "yellow", "lightcoral",
    "lightpink", "lightgrey", "lightcyan", "lightgoldenrodyellow"
]

link_colors = [
    "blue", "lightblue", "lightgreen", "orange", "yellow", "lightcoral", "lightpink", "lightgrey", "lightcyan",
    "lightgoldenrodyellow", "lightblue", "lightgreen", "orange", "yellow", "lightcoral", "lightpink", "lightgrey",
    "lightcyan", "lightgoldenrodyellow", "blue", "lightblue", "lightgreen", "orange", "yellow", "lightcoral",
    "lightpink", "lightgrey", "lightcyan", "lightgoldenrodyellow"
]

# Create the Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=node_colors
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=link_colors
    )
))

fig.update_layout(title_text="Income and Expenses Flow for 2023 and 2022", font_size=10)
fig.show()

