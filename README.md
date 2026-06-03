# IT Risk Management Automation 🚀

> **Automated Technology Performance Review (TPR) System for VFS IT**

Transform your monthly TPR reporting process from hours of manual work to a single command. This system automatically consolidates risk data from multiple business areas, generates professional charts, and updates PowerPoint presentations.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Modules](#modules)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

---

## 🎯 Overview

The TPR Automation System streamlines the monthly Technology Performance Review reporting by automating:

- **Data consolidation** from multiple Excel files across business areas
- **Chart generation** with professional visualizations
- **PowerPoint report creation** with embedded charts and statistics
- **Communication management** for data collection and reminders *(coming soon)*

### Current Status: Risk Management Module ✅

The first module (Risk Management) is complete and ready to use!

---

## ✨ Features

### Risk Management Module (Active)

✅ **Automated Data Consolidation**
- Reads 5 business area risk assessment Excel files
- Combines into a master tracking spreadsheet
- Handles missing columns and data cleaning automatically

✅ **Professional Chart Generation**
- **Stacked Bar Chart**: Open risks by priority per business area (High/Medium/Low)
- **Pie Chart 1**: Operational risk statuses distribution (Open/Closed)
- **Pie Chart 2**: Open risk categories breakdown (Resources, Cyber, Stability, Delivery, Budget, 3rd Party)

✅ **PowerPoint Integration**
- Updates existing TPR template with charts and data
- Creates standalone presentation if no template exists
- Includes summary statistics on slides

✅ **Flexible Configuration**
- YAML-based configuration for easy customization
- Adjustable chart styles, colors, and layouts
- Configurable business area names and categories

---

## 📁 Project Structure

```
IT-Risk-Management-Automation/
├── config/
│   └── config.yaml              # Main configuration file
├── data/
│   ├── input/
│   │   └── risk/                # Place Excel files here
│   └── output/                  # Generated files appear here
├── modules/
│   └── risk_management/
│       ├── data_consolidator.py # Data consolidation logic
│       ├── chart_generator.py   # Chart generation
│       └── ppt_updater.py       # PowerPoint integration
├── templates/                   # PowerPoint templates
├── utils/
│   ├── logger.py               # Logging utility
│   └── config_loader.py        # Config management
├── logs/                        # Automatic log files
├── run_risk_module.py          # Main execution script
├── create_sample_data.py       # Generate test data
├── requirements.txt            # Python dependencies
├── SETUP_GUIDE.md             # Detailed setup instructions
└── README.md                   # This file
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/snerantie/IT-Risk-Management-Automation.git
   cd IT-Risk-Management-Automation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure settings**
   
   Edit `config/config.yaml` to match your setup:
   - Update business area names (tech leads)
   - Set PowerPoint slide numbers
   - Adjust chart preferences

4. **Prepare your data**
   
   Place your risk assessment Excel files in `data/input/risk/`:
   ```
   Operational Risk Assessment - Tech Lead 1.xlsx
   Operational Risk Assessment - Tech Lead 2.xlsx
   ...
   ```

5. **Run the automation**
   ```bash
   python run_risk_module.py
   ```

### Test with Sample Data

Want to test before using real data?

```bash
# Generate sample risk assessment files
python create_sample_data.py

# Run the automation
python run_risk_module.py
```

---

## 📊 Modules

### 1. Risk Management ✅ (Active)

**Purpose**: Automate monthly risk data consolidation and reporting

**Input**: 5 Excel files (one per business area) with risk assessments

**Output**:
- `Master_Risk_Tracker.xlsx` - Consolidated risk data
- `risk_priorities_stacked_bar.png` - Priority distribution chart
- `risk_statuses_pie.png` - Status distribution chart
- `risk_categories_pie.png` - Category breakdown chart
- `TPR_Report_[Month]_[Year].pptx` - Updated PowerPoint presentation

**Expected Excel Columns**:
- Risk Name, Category, Risk Description
- Level of Risk Assessment, Departmental Objective
- Control Name, Control Description, Control Owner, Control Effectiveness
- Likelihood, Level of Impact, Risk Rating
- Action Plan Description, Due Date, Progress
- Budget Required, Action Plan Contact, Status

### 2. AWS Cost Optimization 🔜 (Coming Soon)

Automated AWS cost analysis and reporting

### 3. PI Delivery 🔜 (Coming Soon)

Jira integration for PI (Program Increment) delivery metrics

### 4. Tech Assurance 🔜 (Coming Soon)

Status tracking for technical assurance activities

### 5. Communications & Tracking 🔜 (Coming Soon)

- Automated email notifications for data requests
- Submission tracking dashboard
- Automated reminders (7 days, 2 days before deadline)
- Distribution list management

---

## 💻 Usage

### Basic Usage

```bash
python run_risk_module.py
```

### What Happens?

1. **Data Consolidation**: Reads all Excel files in `data/input/risk/`
2. **Data Cleaning**: Standardizes statuses, priorities, and categories
3. **Master Spreadsheet**: Creates consolidated Excel file
4. **Chart Generation**: Creates 3 professional charts
5. **PowerPoint Update**: Updates TPR presentation with charts and data
6. **Logging**: Creates detailed log file in `logs/`

### Output Files

All outputs are saved to `data/output/`:

```
data/output/
├── Master_Risk_Tracker.xlsx              # Consolidated data
├── risk_priorities_stacked_bar.png       # Chart 1
├── risk_statuses_pie.png                 # Chart 2
├── risk_categories_pie.png               # Chart 3
└── TPR_Report_June_2026.pptx            # Updated presentation
```

### Logs

Check logs for detailed execution information:

```
logs/tpr_automation_20260603.log
```

---

## 🗺️ Roadmap

### Phase 1: Risk Management ✅ (Complete)
- [x] Data consolidation from Excel files
- [x] Chart generation (3 charts)
- [x] PowerPoint integration
- [x] Configuration management
- [x] Sample data generator

### Phase 2: AWS & PI Modules (Next)
- [ ] AWS Cost Optimization module
- [ ] Jira API integration for PI delivery
- [ ] Tech Assurance status tracking
- [ ] Combined report generation

### Phase 3: Communications (Future)
- [ ] Email automation (Outlook integration)
- [ ] Submission tracking dashboard
- [ ] Automated reminders
- [ ] Distribution list management

### Phase 4: SharePoint Integration (Future)
- [ ] Direct SharePoint file access
- [ ] Automated file retrieval from Manco site
- [ ] Version control and history tracking

### Phase 5: Advanced Features (Future)
- [ ] Web dashboard for real-time viewing
- [ ] Trend analysis and predictions
- [ ] Automated anomaly detection
- [ ] Executive summary generation with AI

---

## 📚 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup instructions
- **[config/config.yaml](config/config.yaml)** - Configuration options
- **Inline code documentation** - Comprehensive docstrings in all modules

---

## 🛠️ Technology Stack

- **Python 3.8+** - Core language
- **pandas** - Data manipulation and analysis
- **openpyxl** - Excel file handling
- **matplotlib** - Chart generation
- **seaborn** - Enhanced visualizations
- **python-pptx** - PowerPoint generation
- **PyYAML** - Configuration management

---

## 📝 Configuration

Key settings in `config/config.yaml`:

```yaml
risk_management:
  business_areas:
    - "Tech Lead 1"
    - "Tech Lead 2"
    # ... add your business areas
  
  priorities: ["High", "Medium", "Low"]
  statuses: ["Open", "Closed"]
  categories: ["Resources", "Cyber", "Stability", "Delivery", "Budget", "3rd Party"]

powerpoint:
  template_file: "TPR_Template.pptx"
  risk_slide_number: 5  # Adjust to your slide number
```

---

## 🤝 Contributing

This is an internal VFS IT project. For improvements or bug reports:

1. Create a branch for your feature
2. Make your changes
3. Test thoroughly with sample data
4. Submit a pull request with description

---

## 📞 Support

For questions or issues:
- Check `SETUP_GUIDE.md` for detailed instructions
- Review log files in `logs/` for error messages
- Contact the IT automation team

---

## 📜 License

Internal use only - VFS IT

---

## 🎉 Acknowledgments

Built to streamline TPR reporting and save hours of manual work each month!

**Monthly Time Savings**: ~4-6 hours per report cycle

---

**Repository**: [github.com/snerantie/IT-Risk-Management-Automation](https://github.com/snerantie/IT-Risk-Management-Automation)

**Version**: 1.0.0 (Risk Management Module)
