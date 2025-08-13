import json

mock_data = {
    "posts": [
        {"content": "AI is transforming LinkedIn marketing!", "likes": 120, "comments": 45, "shares": 15},
        {"content": "Top 5 tips for professional networking", "likes": 90, "comments": 30, "shares": 10}
    ]
}

with open("frontend/static/mock_analytics.json", "w") as f:
    json.dump(mock_data, f)

print("✅ Mock data seeded.")
