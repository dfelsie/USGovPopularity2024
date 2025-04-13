import json

# Load the data files
# In a real-world scenario, replace these paths with actual file paths
with open("governor_approval.json", "r") as f:
    governor_data = json.load(f)

with open("election_results.json", "r") as f:
    election_data = json.load(f)

# Create dictionaries for easier lookup
governors_by_state = {
    gov["state"]: gov for gov in governor_data["governors_approval_ratings"]
}
election_by_state = {state["state"]: state for state in election_data}

# Process each governor
for state, gov in governors_by_state.items():
    # Skip if state not in election data
    if state not in election_by_state:
        gov["party_margin"] = None
        gov["popularity_vs_margin"] = None
        continue

    # Get the corresponding election data
    election = election_by_state[state]

    # Calculate margin based on governor's party
    if gov.get("party", "").lower() == "republican":
        # For Republican governors, margin is Republican % - Democrat %
        gov["party_margin"] = (
            election["republican_percent"] - election["democrat_percent"]
        )
    elif gov.get("party", "").lower() == "democratic":
        # For Democratic governors, margin is Democrat % - Republican %
        gov["party_margin"] = (
            election["democrat_percent"] - election["republican_percent"]
        )
    else:
        # For independent or other party governors
        gov["party_margin"] = None

    # Calculate approval vs margin difference if we have all the data
    if gov["party_margin"] is not None and gov.get("average_approval") != "N/A":
        # Calculate how much the governor's approval exceeds their party's margin
        gov["popularity_vs_margin"] = float(gov["net_approval"]) - (gov["party_margin"])
    else:
        gov["popularity_vs_margin"] = None

# Save the updated governor data
with open("governor_margin_comparison.json", "w") as f:
    json.dump(governor_data, f, indent=2)

# Print summary of results
print(
    "Analysis complete. Summary of governors who outperform or underperform their party margin:"
)
for state, gov in governors_by_state.items():
    if gov["popularity_vs_margin"] is not None:
        performance = (
            "outperforms" if gov["popularity_vs_margin"] > 0 else "underperforms"
        )
        print(
            f"{gov['governor']} ({state}, {gov.get('party', 'Unknown')}): {performance} party by {abs(gov['popularity_vs_margin']):.1f} points"
        )
