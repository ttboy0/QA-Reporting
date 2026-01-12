# QA Reporting System - Complete Setup Instructions

## Prerequisites

### Step 1: Install Python 3.11

**⚠️ IMPORTANT: This project requires Python 3.11 or higher**

#### Windows

1. Download Python 3.11 from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **IMPORTANT:** Check the box "Add Python to PATH" during installation
4. Click "Install Now"
5. Verify installation:
   ```bash
   python --version
   ```
   Should show: `Python 3.11.x`

#### macOS

Using Homebrew (recommended):
```bash
brew install python@3.11
```

Verify installation:
```bash
python3.11 --version
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv
```

Verify installation:
```bash
python3.11 --version
```

---

## Project Setup

### Step 2: Extract the Project

1. Extract `qa_reporting_system_final.zip` to your desired location
2. Open a terminal/command prompt
3. Navigate to the project folder:
   ```bash
   cd qa_reporting_system_final
   ```

### Step 3: Create a Virtual Environment

**Virtual environments isolate project dependencies and prevent conflicts with other projects.**

#### Windows

```bash
# Create virtual environment
python -m venv qa_env

# Activate virtual environment
.\qa_env\Scripts\activate
```

You should see `(qa_env)` at the beginning of your command prompt.

#### macOS / Linux

```bash
# Create virtual environment with Python 3.11
python3.11 -m venv qa_env

# Activate virtual environment
source qa_env/bin/activate
```

You should see `(qa_env)` at the beginning of your terminal prompt.

### Step 4: Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Step 5: Install Project Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- pandas (data processing)
- openpyxl (Excel file handling)
- Jinja2 (HTML template rendering)

**Expected output:**
```
Successfully installed pandas-2.x.x openpyxl-3.x.x Jinja2-3.x.x
```

---

## Using the System

### Generate Reports

```bash
python generate_all.py
```

This will:
1. Read data from `qa_data.xlsx`
2. Generate HTML reports
3. Save reports to the `reports/` folder

**Expected output:**
```
📊 Generating API Report...
✓ API Report generated successfully!
📊 Generating WEB Report...
✓ WEB Report generated successfully!
```

### View Reports

Open the generated reports in your web browser:
- `reports/api_report.html` - API Testing Status Report
- `reports/web_report.html` - Web Testing Status Report

### Run Tests

```bash
python test_system.py
```

This will run 24 comprehensive tests to verify:
- Report generation works correctly
- Data modifications are reflected in reports
- All sections display properly

**Expected output:**
```
✓ PASS: Report Generation
✓ PASS: API Data Modifications
✓ PASS: Web Data Modifications
...
TEST SUMMARY
Total Tests: 24
Passed: 24
Failed: 0
```

---

## Editing Your Data

### Edit Excel File

1. Open `qa_data.xlsx` in Microsoft Excel, Google Sheets, or LibreOffice Calc
2. Update the data in the following sections:
   - **Test Suites:** Add/modify test suite names, counts, and status
   - **Defects:** Update defect counts by priority
   - **Coverage:** Update coverage percentages by area
   - **Risks:** Add/modify risk descriptions and assigned owners
3. Save the file
4. Run `python generate_all.py` to regenerate reports

### Adding More Rows

See `HOW_TO_ADD_ROWS.md` for detailed instructions on:
- Adding new test suites
- Adding new defect priorities
- Adding new coverage areas
- Adding new risks

---

## Deactivating Virtual Environment

When you're done working on the project:

```bash
deactivate
```

The `(qa_env)` prefix will disappear from your prompt.

---

## Troubleshooting

### Issue: "python: command not found" or "python is not recognized"

**Solution:** Python 3.11 is not installed or not in PATH
- Windows: Reinstall Python and check "Add Python to PATH"
- macOS: Use `python3.11` instead of `python`
- Linux: Install Python 3.11: `sudo apt install python3.11`

### Issue: "No module named 'pandas'" or similar import error

**Solution:** Dependencies not installed
```bash
# Make sure virtual environment is activated (you should see (qa_env) in prompt)
pip install -r requirements.txt
```

### Issue: "ModuleNotFoundError: No module named 'six.moves'"

**Solution:** This is a known issue with older Python versions
- Ensure you're using Python 3.11: `python --version`
- Reinstall dependencies: `pip install --upgrade -r requirements.txt`

### Issue: Virtual environment not activating

**Windows:**
```bash
# Try PowerShell version
.\qa_env\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
# Make sure you're in the project directory
source qa_env/bin/activate
```

### Issue: Reports folder is empty

**Solution:** Run the generator
```bash
python generate_all.py
```

### Issue: Excel file shows error when opening

**Solution:** Make sure the file is not open in another program
- Close any open instances of the Excel file
- Try opening it again

---

## Project Structure

```
qa_reporting_system_final/
├── qa_env/                    # Virtual environment (created after setup)
├── reports/                   # Generated HTML reports
│   ├── api_report.html
│   └── web_report.html
├── qa_data.xlsx              # Excel data template (EDIT THIS)
├── template.html             # HTML template for reports
├── generate_all.py           # Main report generator (RUN THIS)
├── create_qa_data.py         # Creates fresh Excel template
├── test_system.py            # Test suite
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview
├── QUICK_START.md            # Quick reference
├── HOW_TO_ADD_ROWS.md        # Guide for adding rows
└── SETUP_INSTRUCTIONS.md     # This file
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Create virtual environment | `python -m venv qa_env` |
| Activate (Windows) | `.\qa_env\Scripts\activate` |
| Activate (macOS/Linux) | `source qa_env/bin/activate` |
| Install dependencies | `pip install -r requirements.txt` |
| Generate reports | `python generate_all.py` |
| Run tests | `python test_system.py` |
| Deactivate environment | `deactivate` |

---

## Next Steps

1. ✅ Install Python 3.11
2. ✅ Create virtual environment
3. ✅ Install dependencies
4. ✅ Edit `qa_data.xlsx` with your test data
5. ✅ Run `python generate_all.py`
6. ✅ Open reports in your browser
7. ✅ Run `python test_system.py` to verify everything works

---

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review `HOW_TO_ADD_ROWS.md` for data editing
3. Review `README.md` for project overview
4. Check `QUICK_START.md` for quick reference

---

## Important Notes

⚠️ **Always activate the virtual environment before running commands:**
```bash
# Windows
.\qa_env\Scripts\activate

# macOS/Linux
source qa_env/bin/activate
```

✅ **Best Practice:** Keep the virtual environment in the project folder so all dependencies are isolated to this project.

✅ **Reproducibility:** Virtual environments ensure the same versions of dependencies are used every time, making the system reproducible across different machines.
