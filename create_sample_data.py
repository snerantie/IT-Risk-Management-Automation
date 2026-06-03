#!/usr/bin/env python3
"""
Create sample risk assessment Excel files for testing
"""
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
import random

# Sample data for different business areas
TECH_LEADS = [
    "John Smith",
    "Sarah Johnson",
    "Michael Chen",
    "Emma Williams",
    "David Brown"
]

RISK_CATEGORIES = ["Resources", "Cyber", "Stability", "Delivery", "Budget", "3rd Party"]
PRIORITIES = ["High", "Medium", "Low"]
STATUSES = ["Open", "Closed"]

SAMPLE_RISKS = {
    "Resources": [
        "Staff shortage in critical area",
        "Key personnel retention risk",
        "Skill gap in new technology",
        "Contractor dependency"
    ],
    "Cyber": [
        "Unpatched security vulnerabilities",
        "Inadequate access controls",
        "Phishing attack exposure",
        "Data encryption gaps"
    ],
    "Stability": [
        "System performance degradation",
        "Infrastructure aging",
        "Single point of failure",
        "Insufficient redundancy"
    ],
    "Delivery": [
        "Project timeline slippage",
        "Scope creep on key projects",
        "Dependencies on external teams",
        "Resource allocation conflicts"
    ],
    "Budget": [
        "Cost overrun on cloud services",
        "Unplanned licensing costs",
        "Budget cuts impacting delivery",
        "Currency fluctuation impact"
    ],
    "3rd Party": [
        "Vendor service level issues",
        "Third-party security vulnerabilities",
        "Contract renewal uncertainty",
        "Supplier capacity constraints"
    ]
}


def generate_risk_data(tech_lead, num_risks=8):
    """Generate sample risk data for a tech lead"""
    risks = []
    
    for i in range(num_risks):
        category = random.choice(RISK_CATEGORIES)
        priority = random.choice(PRIORITIES)
        status = random.choice(STATUSES)
        
        # Select a risk from the category
        risk_name = random.choice(SAMPLE_RISKS[category])
        
        # Generate dates
        due_date = datetime.now() + timedelta(days=random.randint(30, 180))
        
        risk = {
            "Risk Name": risk_name,
            "Category": category,
            "Risk Description": f"Detailed description of {risk_name.lower()} affecting {tech_lead}'s area",
            "Level of Risk Assessment": random.choice(["Strategic", "Operational", "Tactical"]),
            "Departmental Objective": "Ensure service continuity and delivery excellence",
            "Control Name": f"Control for {category}",
            "Control Description": f"Mitigation controls in place for {risk_name.lower()}",
            "Control Owner": tech_lead,
            "Control Effectiveness": random.choice(["High", "Medium", "Low"]),
            "Likelihood": random.choice(PRIORITIES),
            "Level of Impact": random.choice(PRIORITIES),
            "Risk Rating": priority,
            "Action Plan Description": f"Action plan to address {risk_name.lower()}",
            "Due Date": due_date.strftime("%Y-%m-%d"),
            "Progress": random.choice(["Not Started", "In Progress", "Completed", "On Hold"]),
            "Budget Required": f"£{random.randint(5, 100) * 1000}",
            "Action Plan Contact": tech_lead,
            "Status": status
        }
        
        risks.append(risk)
    
    return pd.DataFrame(risks)


def create_sample_files():
    """Create sample Excel files for all tech leads"""
    output_dir = Path("data/input/risk")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("Creating sample risk assessment files...")
    print("="*70)
    
    for tech_lead in TECH_LEADS:
        # Generate data
        df = generate_risk_data(tech_lead)
        
        # Save to Excel
        filename = f"Operational Risk Assessment - {tech_lead}.xlsx"
        filepath = output_dir / filename
        
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Risk Assessment', index=False)
            
            # Auto-adjust column widths
            worksheet = writer.sheets['Risk Assessment']
            for idx, col in enumerate(df.columns):
                max_length = max(df[col].astype(str).apply(len).max(), len(col))
                worksheet.column_dimensions[chr(65 + idx)].width = min(max_length + 2, 50)
        
        print(f"✓ Created: {filename} ({len(df)} risks)")
    
    print("="*70)
    print(f"\nSample files created in: {output_dir}")
    print("\nYou can now run: python run_risk_module.py")


if __name__ == "__main__":
    create_sample_files()
