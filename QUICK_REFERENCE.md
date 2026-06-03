# Quick Reference Guide 📖

## Installation (One-Time Setup)

```bash
# Clone repository
git clone https://github.com/snerantie/IT-Risk-Management-Automation.git
cd IT-Risk-Management-Automation

# Install dependencies
pip install -r requirements.txt
```

---

## Monthly Workflow

### 1. Collect Risk Data 📥

**SharePoint Path**:
```
SharePoint → Manco → Documents → General → Risk → 
Operational Risk Assessments → [Current Month Folder]
```

**Files to collect**: 5 business area Excel files

### 2. Place Files Locally 📁

Copy the 5 Excel files to:
```
IT-Risk-Management-Automation/data/input/risk/
```

**Expected naming**:
- `Operational Risk Assessment - [Tech Lead Name].xlsx`

### 3. Run Automation ▶️

```bash
python run_risk_module.py
```

### 4. Review Outputs ✅

Check `data/output/` folder for:
- ✅ Master_Risk_Tracker.xlsx
- ✅ 3 chart images (.png)
- ✅ TPR_Report_[Month]_[Year].pptx

### 5. Use in TPR Report 📊

Open the generated PowerPoint or copy charts to your existing TPR template.

---

## Common Commands

### Generate Test Data
```bash
python create_sample_data.py
```

### Run Risk Module
```bash
python run_risk_module.py
```

### View Logs
```bash
# Today's log
cat logs/tpr_automation_$(date +%Y%m%d).log

# Latest log
ls -lt logs/ | head -2
```

### Clean Output Folder
```bash
rm -rf data/output/*
```

---

## Configuration Quick Reference

Edit `config/config.yaml`:

### Update Business Area Names
```yaml
risk_management:
  business_areas:
    - "John Smith"      # Replace with actual names
    - "Sarah Johnson"
    - "Michael Chen"
    - "Emma Williams"
    - "David Brown"
```

### Update PowerPoint Slide Number
```yaml
powerpoint:
  risk_slide_number: 5  # Change to your actual slide number
```

### Adjust Chart Sizes
```yaml
risk_management:
  charts:
    stacked_bar:
      width: 10   # Inches
      height: 6
```

---

## File Structure Quick Reference

```
📦 IT-Risk-Management-Automation
├── 📂 config
│   └── config.yaml                    ← Edit settings here
├── 📂 data
│   ├── 📂 input/risk                  ← Put Excel files here
│   └── 📂 output                      ← Generated files appear here
├── 📂 templates                       ← Optional: Place TPR template here
├── 📂 logs                            ← Check for errors
├── 🐍 run_risk_module.py             ← Main script to run
└── 🐍 create_sample_data.py          ← Generate test data
```

---

## Expected Excel Columns

Your Excel files should have these columns (order doesn't matter):

| Column Name | Example |
|------------|---------|
| Risk Name | "Resource Shortage" |
| Category | "Resources" |
| Risk Description | "Insufficient staff..." |
| Level of Risk Assessment | "Operational" |
| Departmental Objective | "Maintain delivery" |
| Control Name | "Resource Planning" |
| Control Description | "Monthly reviews" |
| Control Owner | "Jane Doe" |
| Control Effectiveness | "High" |
| Likelihood | "Medium" |
| Level of Impact | "High" |
| Risk Rating | "High" / "Medium" / "Low" |
| Action Plan Description | "Hire contractors" |
| Due Date | "2026-07-01" |
| Progress | "In Progress" |
| Budget Required | "£50,000" |
| Action Plan Contact | "John Smith" |
| Status | "Open" / "Closed" |

---

## Chart Outputs

### 1. Stacked Bar Chart
**File**: `risk_priorities_stacked_bar.png`
- Shows: Open risks by priority per business area
- Colors: 🔴 High (Red), 🟠 Medium (Orange), 🟢 Low (Green)

### 2. Status Pie Chart
**File**: `risk_statuses_pie.png`
- Shows: Open vs Closed risk distribution
- Total risk count

### 3. Categories Pie Chart
**File**: `risk_categories_pie.png`
- Shows: Risk breakdown by category
- Only includes Open risks
- Categories: Resources, Cyber, Stability, Delivery, Budget, 3rd Party

---

## Troubleshooting Quick Fixes

### "No Excel files found"
```bash
# Check files are in correct location
ls data/input/risk/

# Should see files like: "Operational Risk Assessment - *.xlsx"
```

### "Column not found" error
- Check Excel file has all required columns
- Verify spelling matches exactly
- Remove extra spaces in column headers

### Charts look wrong
- Check Status values are exactly "Open" or "Closed"
- Check Risk Rating values are "High", "Medium", or "Low"
- Review data in Master_Risk_Tracker.xlsx

### PowerPoint not updating
- Verify template exists in `templates/TPR_Template.pptx`
- Check slide number in config.yaml is correct
- Try running without template (creates new presentation)

---

## Time Estimates

| Task | Manual | Automated | Savings |
|------|--------|-----------|---------|
| Data consolidation | 1.5 hrs | 5 sec | 99% ⬇️ |
| Chart creation | 1 hr | 10 sec | 98% ⬇️ |
| PowerPoint update | 30 min | 5 sec | 97% ⬇️ |
| **Total** | **3 hrs** | **20 sec** | **99% ⬇️** |

---

## Monthly Checklist

- [ ] Collect 5 business area Excel files from SharePoint
- [ ] Place files in `data/input/risk/`
- [ ] Run `python run_risk_module.py`
- [ ] Check `data/output/` for generated files
- [ ] Review Master_Risk_Tracker.xlsx for accuracy
- [ ] Verify charts look correct
- [ ] Use charts in TPR presentation
- [ ] Archive input files for records

---

## Support Contacts

**For Technical Issues**:
- Check logs in `logs/` folder
- Review SETUP_GUIDE.md
- Contact IT automation team

**For Data Questions**:
- Contact respective business area tech leads
- Verify SharePoint has latest data

---

## Version Info

**Current Version**: 1.0.0 (Risk Management Module)

**Next Updates**:
- AWS Cost Optimization module
- PI Delivery (Jira integration)
- Communications automation

---

**Repository**: [github.com/snerantie/IT-Risk-Management-Automation](https://github.com/snerantie/IT-Risk-Management-Automation)
