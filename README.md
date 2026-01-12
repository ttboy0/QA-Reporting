# QA Reporting System

This system generates professional, data-driven QA status reports in HTML format from a simple Excel template.

## Features

- **Data-Driven**: Reports are generated from `qa_data.xlsx`.
- **Professional Design**: Clean, modern design with interactive charts.
- **Automated**: Run one command to generate all reports.
- **Customizable**: Easily change data, titles, and colors.

## Quick Start

### 1. Setup

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Create Data Template

If `qa_data.xlsx` doesn't exist, create it:

```bash
python create_qa_data.py
```

### 3. Edit Data

Open `qa_data.xlsx` and update the metrics in the **API Data** and **Web Data** sheets.

### 4. Generate Reports

Run the main generation script:

```bash
python generate_all.py
```

### 5. View Reports

Your reports will be in the `reports/` directory:
- `reports/api_report.html`
- `reports/web_report.html`

## File Structure

- `qa_data.xlsx`: Excel data template
- `template.html`: HTML/Jinja2 template
- `generate_all.py`: Main generation script
- `create_qa_data.py`: Script to create the Excel template
- `requirements.txt`: Python dependencies
- `reports/`: Output directory for generated reports
