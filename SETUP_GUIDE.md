# TPR Automation - Setup Guide

## Quick Start

### 1. Installation

```bash
# Navigate to project directory
cd tpr-automation

# Install required packages
pip install -r requirements.txt
```

### 2. Configuration

Edit `config/config.yaml` to customize settings:

- **Business Areas**: Update the `risk_management.business_areas` list with your actual tech lead names
- **Slide Number**: Set `powerpoint.risk_slide_number` to the correct slide in your TPR template
- **Email Settings**: Configure email settings for future automation (not needed for initial setup)

### 3. Prepare Your Data

#### Option A: Local Folder (Recommended for Testing)

1. Create the input folder structure:
   ```
   tpr-automation/
   └── data/
       └── input/
           └── risk/
   ```

2. Copy your 5 business area Excel files to `data/input/risk/`
   - File naming: `Operational Risk Assessment - [Tech Lead Name].xlsx`
   - Example: `Operational Risk Assessment - John Smith.xlsx`

#### Option B: SharePoint Integration (Coming Soon)

The system will automatically pull files from SharePoint in future versions.

### 4. Prepare PowerPoint Template (Optional)

If you have an existing TPR PowerPoint template:

1. Copy it to `templates/TPR_Template.pptx`
2. Note which slide number contains risk management content
3. Update `config/config.yaml` with the correct slide number

If you don't have a template, the system will create a new presentation with the charts.

### 5. Run the Risk Management Module

```bash
python run_risk_module.py
```

## What the Module Does

### 1. Data Consolidation
- Reads all 5 business area Excel files
- Combines them into a master spreadsheet
- Adds "Business Area" column to track the source
- Saves to: `data/output/Master_Risk_Tracker.xlsx`

### 2. Chart Generation
Creates 3 charts automatically:

1. **Stacked Bar Chart**: Open risks by priority per business area
   - Shows High, Medium, Low risks for each business area
   - Colors: Red (High), Orange (Medium), Green (Low)

2. **Pie Chart**: Operational Risk Statuses
   - Shows distribution of Open vs Closed risks
   - Total risk count

3. **Pie Chart**: % Split Open Risk Categories
   - Shows distribution across: Resources, Cyber, Stability, Delivery, Budget, 3rd Party
   - Only includes Open risks

All charts saved to: `data/output/`

### 3. PowerPoint Update
- Loads your TPR template (if it exists)
- Inserts charts into the risk management slide
- Adds summary statistics
- Saves updated presentation to: `data/output/TPR_Report_[Month]_[Year].pptx`

## Expected Excel Structure

Each business area Excel file should contain these columns:

| Column Name | Description | Example |
|------------|-------------|---------|
| Risk Name | Name of the risk | "Resource Shortage" |
| Category | Risk category | "Resources", "Cyber", "Stability", etc. |
| Risk Description | Detailed description | "Insufficient staff for Q2 projects" |
| Level of Risk Assessment | Assessment level | TBD |
| Departmental Objective | Related objective | "Maintain service delivery" |
| Control Name | Control measure name | "Resource Planning" |
| Control Description | How it's controlled | "Monthly resource reviews" |
| Control Owner | Person responsible | "Jane Doe" |
| Control Effectiveness | How effective | "Medium", "High", etc. |
| Likelihood | Probability of occurrence | "High", "Medium", "Low" |
| Level of Impact | Impact if occurs | "High", "Medium", "Low" |
| Risk Rating | Overall risk level | "High", "Medium", "Low" |
| Action Plan Description | Mitigation actions | "Hire 2 contractors" |
| Due Date | Action due date | "2026-07-01" |
| Progress | Current progress | "In Progress", "Not Started" |
| Budget Required | Budget needed | "£50,000" |
| Action Plan Contact | Person handling action | "John Smith" |
| Status | Risk status | "Open" or "Closed" |

## Output Files

After running, you'll find:

```
data/output/
├── Master_Risk_Tracker.xlsx              # Consolidated data
├── risk_priorities_stacked_bar.png       # Chart 1
├── risk_statuses_pie.png                 # Chart 2
├── risk_categories_pie.png               # Chart 3
└── TPR_Report_[Month]_[Year].pptx       # Updated presentation
```

## Troubleshooting

### No Excel files found
- Check that files are in `data/input/risk/` folder
- Verify filenames contain "Operational Risk Assessment"
- Check file extensions (.xlsx or .xls)

### Column name errors
- Ensure Excel files have the expected column names
- Check for extra spaces in column headers
- Verify column names match exactly (case-sensitive)

### PowerPoint errors
- Verify template path is correct
- Check slide number is valid
- Ensure template file is not open in PowerPoint

### Chart generation fails
- Check that data contains required columns
- Verify Status column has "Open" and "Closed" values
- Ensure Risk Rating has "High", "Medium", "Low" values

## Next Steps

Once the Risk Management module is working:

1. **AWS Cost Optimization Module** - Similar approach for AWS data
2. **PI Delivery Module** - Integration with Jira for project data
3. **Communications Module** - Automated emails and reminders
4. **SharePoint Integration** - Direct file access from SharePoint

## Support

For issues or questions, check the logs in `logs/tpr_automation_[date].log`
