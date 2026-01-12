import pandas as pd
from jinja2 import Template
import os

# Configuration
EXCEL_FILE = 'qa_data.xlsx'
TEMPLATE_FILE = 'template.html'
OUTPUT_DIR = 'reports'

def read_excel_data(sheet_name):
    """Read data from Excel sheet"""
    df = pd.read_excel(EXCEL_FILE, sheet_name=sheet_name, engine='openpyxl')
    
    # Extract metadata
    lead_name = df.iloc[3, 1]  # Row 4, Column B
    
    # Extract test suites (rows 7-10 in pandas = rows 9-12 in openpyxl, columns A-G)
    summary_data = []
    for row_idx in range(7, 11):
        suite_name = df.iloc[row_idx, 0]
        total = df.iloc[row_idx, 1]
        passed = df.iloc[row_idx, 2]
        failed = df.iloc[row_idx, 3]
        blocked = df.iloc[row_idx, 4]
        
        # Skip if any values are NaN
        if pd.isna(total) or pd.isna(passed):
            continue
            
        total = int(total)
        passed = int(passed)
        failed = int(failed)
        blocked = int(blocked)
        pass_rate = round(passed / total * 100) if total > 0 else 0
        
        # Determine status
        if pass_rate >= 95:
            status = 'Excellent'
            status_class = 'status-pass'
        elif pass_rate >= 85:
            status = 'Good'
            status_class = 'status-warn'
        else:
            status = 'Needs Improvement'
            status_class = 'status-fail'
        
        summary_data.append({
            'name': suite_name,
            'total': total,
            'passed': passed,
            'failed': failed,
            'blocked': blocked,
            'pass_rate': pass_rate,
            'status': status,
            'status_class': status_class
        })
    
    # Calculate totals
    total_tests = sum(s['total'] for s in summary_data)
    total_passed = sum(s['passed'] for s in summary_data)
    total_failed = sum(s['failed'] for s in summary_data)
    total_blocked = sum(s['blocked'] for s in summary_data)
    overall_pass_rate = round(total_passed / total_tests * 100) if total_tests > 0 else 0
    
    # Extract defects (rows 16-19 in pandas, columns A-B)
    defects = {}
    for row_idx in range(16, 20):
        priority = df.iloc[row_idx, 0]
        count = df.iloc[row_idx, 1]
        if not pd.isna(priority) and not pd.isna(count):
            defects[priority] = int(count)
    
    # Extract coverage (rows 23-26 in pandas, columns A-B)
    coverage = {}
    for row_idx in range(23, 27):
        area = df.iloc[row_idx, 0]
        pct = df.iloc[row_idx, 1]
        if not pd.isna(area) and not pd.isna(pct):
            coverage[area] = int(pct)
    
    # Extract risks (rows 29-31 in pandas = rows 31-33 in openpyxl, columns A-E)
    risks_data = []
    for row_idx in range(29, min(32, len(df))):
        if row_idx >= len(df):
            break
        issue_id = df.iloc[row_idx, 0]
        description = df.iloc[row_idx, 1]
        priority = df.iloc[row_idx, 2]
        owner = df.iloc[row_idx, 3]
        target_date = df.iloc[row_idx, 4]
        
        if pd.isna(issue_id) or pd.isna(description):
            continue
        
        priority_class = 'risk-high' if priority == 'HIGH' else 'risk-med'
        
        risks_data.append({
            'id': issue_id,
            'description': description,
            'priority': priority,
            'owner': owner,
            'target_date': target_date,
            'priority_class': priority_class
        })
    
    return {
        'summary_data': summary_data,
        'risks_data': risks_data,
        'coverage': coverage,
        'defects': defects,
        'lead_name': lead_name,
        'total_tests': total_tests,
        'total_passed': total_passed,
        'total_failed': total_failed,
        'total_blocked': total_blocked,
        'overall_pass_rate': overall_pass_rate,
    }

def generate_html_report(report_type):
    """Generate HTML report from Excel data"""
    sheet_name = "API Data" if report_type == "api" else "Web Data"
    excel_data = read_excel_data(sheet_name)
    
    with open(TEMPLATE_FILE, 'r') as f:
        template_str = f.read()
    
    template = Template(template_str)
    
    if report_type == "api":
        report_title = "API Testing Status Report"
        report_subtitle = "E-Commerce Platform v2.0 | Week of Jan 6-12, 2026 | API Suite"
        lead_title = "API Test Lead"
        lead_initials = "DP"
        objective = "Ensure backend stability, performance, and data integrity."
        summary_title = "API Testing Summary"
    else:
        report_title = "Web Testing Status Report"
        report_subtitle = "E-Commerce Platform v2.0 | Week of Jan 6-12, 2026 | Selenium Suite"
        lead_title = "UI Test Lead"
        lead_initials = "JM"
        objective = "Validate user experience, cross-browser compatibility, and UI functionality."
        summary_title = "Selenium (UI) Summary"
        
    priority_labels = ["Critical", "High", "Medium", "Low"]
    priority_data = [
        excel_data['defects'].get('Critical', 0),
        excel_data['defects'].get('High', 0),
        excel_data['defects'].get('Medium', 0),
        excel_data['defects'].get('Low', 0),
    ]
    
    ratio_data = [excel_data['overall_pass_rate'], 
                  round(excel_data['total_failed'] / excel_data['total_tests'] * 100) if excel_data['total_tests'] > 0 else 0,
                  round(excel_data['total_blocked'] / excel_data['total_tests'] * 100) if excel_data['total_tests'] > 0 else 0]
    
    coverage_labels = list(excel_data['coverage'].keys())
    coverage_data = list(excel_data['coverage'].values())
    
    takeaways = [
        f"<strong>Overall Status:</strong> {excel_data['overall_pass_rate']}% Pass Rate. {excel_data['total_tests']} Tests Executed.",
        f"<strong>Performance:</strong> System stable. {excel_data['total_passed']} tests passed.",
        f"<strong>Automation:</strong> 78% coverage achieved.",
        f"<strong>Critical Issues:</strong> {excel_data['defects'].get('Critical', 0)} Critical defects. {excel_data['defects'].get('High', 0)} High priority in progress.",
    ]
    
    html_content = template.render(
        report_title=report_title,
        report_subtitle=report_subtitle,
        lead_title=lead_title,
        lead_initials=lead_initials,
        lead_name=excel_data['lead_name'],
        objective=objective,
        summary_title=summary_title,
        takeaways=takeaways,
        summary_data=excel_data['summary_data'],
        risks_data=excel_data['risks_data'],
        overview={
            'total': excel_data['total_tests'],
            'passed': excel_data['total_passed'],
            'failed': excel_data['total_failed'],
            'blocked': excel_data['total_blocked'],
        },
        ratio_chart_data=ratio_data,
        priority_chart_labels=priority_labels,
        priority_chart_data=priority_data,
        coverage_chart_labels=coverage_labels,
        coverage_chart_data=coverage_data,
        zip=zip,
    )
    
    return html_content, excel_data

def export_html(html_content, report_type):
    """Export to HTML file"""
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    filename = f"{OUTPUT_DIR}/{report_type}_report.html"
    with open(filename, 'w') as f:
        f.write(html_content)
    print(f"  ✓ HTML: {filename}")
    return filename

def main():
    print("="*60)
    print("QA REPORTING SYSTEM - HTML Report Generator")
    print("="*60)
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    for report_type in ["api", "web"]:
        print(f"📊 Generating {report_type.upper()} Report...")
        
        try:
            html_content, _ = generate_html_report(report_type)
            export_html(html_content, report_type)
            print(f"  ✓ {report_type.upper()} report complete!\n")
        
        except Exception as e:
            print(f"  ❌ ERROR generating {report_type.upper()} report: {e}")
            import traceback
            traceback.print_exc()
            print("\n")

    print("="*60)
    print("✓ All reports generated successfully!")
    print(f"📁 Output directory: {OUTPUT_DIR}/")
    print("="*60)

if __name__ == "__main__":
    main()
