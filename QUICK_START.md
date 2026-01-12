# QA Reporting System - Quick Start Guide

## What You Have

A complete, professional QA reporting system with:
- ✅ Excel data template (`qa_data.xlsx`)
- ✅ Beautiful HTML/PDF/PowerPoint reports
- ✅ Automated report generation
- ✅ Full documentation

## Installation (One-time)

```bash
cd /home/ubuntu/qa_reporting_system
pip install openpyxl jinja2 weasyprint python-pptx
```

## Usage (Every Time)

### Option 1: Interactive Mode (Choose export format)
```bash
python generate_reports.py
```
Follow the prompts to select:
- 1 = HTML only
- 2 = PDF only
- 3 = PowerPoint only
- 4 = HTML + PDF
- 5 = HTML + PowerPoint
- 6 = All formats (Recommended)

### Option 2: Automated Mode (Generate all formats instantly)
```bash
python generate_all.py
```

## Workflow

1. **Edit Data**
   ```bash
   # Open in Excel or any spreadsheet app
   qa_data.xlsx
   ```
   - Update test metrics
   - Update defect counts
   - Update coverage percentages
   - Update risk information
   - Save the file

2. **Generate Reports**
   ```bash
   python generate_all.py
   ```
   Reports appear in: `reports/` folder

3. **Use Reports**
   - **api_report.html** - View in browser
   - **api_report.pdf** - Print or email
   - **api_report.pptx** - Edit in PowerPoint
   - Same for web_report.*

## Files Included

| File | Purpose |
|------|---------|
| `qa_data.xlsx` | Your data template (edit this!) |
| `template.html` | Report design template |
| `generate_reports.py` | Interactive report generator |
| `generate_all.py` | Automated report generator |
| `create_qa_data.py` | Creates fresh Excel template |
| `README.md` | Full documentation |
| `QUICK_START.md` | This file |

## Sample Data Structure

### API Data Sheet
- Authentication API: 156 tests, 97% pass
- Payment Processing: 289 tests, 92% pass
- Inventory Management: 198 tests, 94% pass
- Reporting Engine: 204 tests, 89% pass

### Web Data Sheet
- Login & Auth Flow: 78 tests, 97% pass
- Checkout Flow: 92 tests, 85% pass
- Product Search: 68 tests, 90% pass
- Dashboard & Reports: 82 tests, 79% pass

## Report Contents

Each report includes:
1. **Header** - Title, lead info, key takeaways
2. **Summary Table** - Test suite breakdown
3. **Risks Section** - High priority issues with owners
4. **Charts**:
   - Testing Overview (counts)
   - Pass vs Fail Ratio (pie chart)
   - Defect by Priority (bar chart)
   - Percentage Coverage (horizontal bar)

## Customization

### Change Report Title
Edit `generate_reports.py` or `generate_all.py`:
```python
report_title = "Your Custom Title"
```

### Change Colors
Edit `template.html` CSS:
```css
background-color: #2C2C54;  /* Dark navy */
```

### Add More Test Suites
1. Add rows to Excel (rows 9-12)
2. Update the row range in Python script

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Module not found" | Run: `pip install openpyxl jinja2 weasyprint python-pptx` |
| PDF not generating | Install: `pip install weasyprint` |
| PowerPoint not generating | Install: `pip install python-pptx` |
| Excel file not found | Run: `python create_qa_data.py` |

## Tips

✅ **Best Practices**
- Update Excel every week at the same time
- Keep backup copies of qa_data.xlsx
- Archive PDF reports for compliance
- Use HTML for quick sharing, PDF for formal docs

❌ **Don't**
- Manually edit generated HTML (changes will be lost)
- Delete template.html
- Change Excel sheet names without updating scripts

## Support

For detailed information, see: `README.md`

---
**Version**: 1.0 | **Updated**: January 2026
