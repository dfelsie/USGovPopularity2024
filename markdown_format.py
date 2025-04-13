import json

# Load the governor data with party comparison
with open("governor_margin_comparison.json", "r") as f:
    data = json.load(f)

# Extract the governors list
governors = data["governors_approval_ratings"]

# Filter out entries with missing data
filtered_governors = []
for gov in governors:
    if (
        "party_margin" in gov
        and gov["party_margin"] is not None
        and "average_approval" in gov
        and gov["average_approval"] != "N/A"
    ):
        filtered_governors.append(gov)

# Sort by popularity_vs_margin (descending)
sorted_governors = sorted(
    filtered_governors,
    key=lambda x: (
        x["popularity_vs_margin"] if x["popularity_vs_margin"] is not None else -9999
    ),
    reverse=True,
)

# Create a markdown table
markdown = "# Governors Compared to Their Party's Electoral Margin\n\n"
markdown += "| State | Governor | Party | Approval Rating | Party Margin | vs Expected | Number of Polls |\n"
markdown += "|-------|----------|-------|----------------|--------------|-------------|-------|\n"

for gov in sorted_governors:
    # Format the difference with a plus sign for positive values
    diff = gov["popularity_vs_margin"]
    diff_format = f"+{diff:.1f}%" if diff > 0 else f"{diff:.1f}%"

    # Format party margin with +/- sign
    margin = gov["party_margin"]
    margin_format = f"+{margin:.1f}%" if margin > 0 else f"{margin:.1f}%"

    markdown += f"| {gov['state']} | {gov['governor']} | {gov['party']} | "
    markdown += f"{gov['average_approval']:.1f}% | {margin_format} | {diff_format} | {gov['number_of_polls']} |\n"

# Write the markdown to a file
with open("governor_margin_comparison.md", "w") as f:
    f.write(markdown)

print("Markdown table created successfully in 'governor_margin_comparison.md'")
print("\nPreview of the table:")
print(markdown[:500] + "...\n")
