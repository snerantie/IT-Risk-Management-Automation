# TPR Automation System

Automated Technology Performance Review (TPR) reporting system for VFS IT.

## Project Structure

```
tpr-automation/
├── config/                 # Configuration files
├── data/                   # Data storage
│   ├── input/             # Input Excel files
│   │   └── risk/          # Risk management files
│   └── output/            # Generated reports and charts
├── modules/               # Automation modules
│   ├── risk_management/   # Risk management module
│   ├── aws_cost/          # AWS cost optimization module (coming soon)
│   ├── pi_delivery/       # PI delivery module (coming soon)
│   └── communications/    # Email & tracking module (coming soon)
├── templates/             # PowerPoint templates
└── utils/                 # Shared utilities
```

## Modules

### 1. Risk Management (Active)
- Consolidates 5 business area risk spreadsheets
- Generates 3 charts:
  - Stacked bar graph: Open risks priorities per business area
  - Pie chart: Operational Risk statuses
  - Pie chart: % Split Open Risk Categories
- Updates PowerPoint slides

### 2. AWS Cost Optimization (Coming Soon)
### 3. PI Delivery (Coming Soon)
### 4. Tech Assurance (Coming Soon)
### 5. Communications & Tracking (Coming Soon)

## Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Configuration

Edit `config/config.yaml` to set your preferences.

## Usage

### Risk Management Module

```bash
python run_risk_module.py
```

This will:
1. Read risk assessment files from `data/input/risk/`
2. Consolidate data into master spreadsheet
3. Generate charts
4. Update PowerPoint slides
