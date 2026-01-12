# How to Add More Rows to the QA Data File

The `qa_data.xlsx` file is flexible and allows you to add more test suites, defects, coverage areas, and risks. Here's how:

## 1. Adding More Test Suites

**Location:** Rows 8-11 (API Data) or Rows 8-11 (Web Data)

**Current structure:**
```
Row 8:  [Suite Name] [Total Tests] [Passed] [Failed] [Blocked] [Pass Rate %] [Status]
Row 9:  [Suite Name] [Total Tests] [Passed] [Failed] [Blocked] [Pass Rate %] [Status]
Row 10: [Suite Name] [Total Tests] [Passed] [Failed] [Blocked] [Pass Rate %] [Status]
Row 11: [Suite Name] [Total Tests] [Passed] [Failed] [Blocked] [Pass Rate %] [Status]
```

**To add more suites:**
1. Copy one of the existing rows (e.g., Row 8)
2. Insert a new row BEFORE the "TOTALS" row (Row 12)
3. Update the values with your new test suite data
4. The script will automatically include it in the report

**Example:**
```
Row 8:  Authentication API | 156 | 152 | 3 | 1 | 97 | Stable
Row 9:  Payment Processing | 289 | 268 | 18 | 3 | 92 | Monitor
Row 10: Inventory Management | 198 | 187 | 9 | 2 | 94 | Stable
Row 11: Reporting Engine | 204 | 182 | 18 | 4 | 89 | Monitor
Row 12: [NEW] User Management | 120 | 115 | 4 | 1 | 96 | Stable  <- Add here
Row 13: TOTALS
```

## 2. Adding More Defects

**Location:** Rows 16-19 (Defect data)

**Current structure:**
```
Row 16: Critical | [count] | [status]
Row 17: High | [count] | [status]
Row 18: Medium | [count] | [status]
Row 19: Low | [count] | [status]
```

**To add more defect priorities:**
1. Insert a new row after Row 19
2. Add your priority name and count
3. The script will include it in the defect chart

**Example:**
```
Row 16: Critical | 2 | Resolved
Row 17: High | 8 | In Progress
Row 18: Medium | 22 | Scheduled
Row 19: Low | 16 | Backlog
Row 20: [NEW] Blocker | 1 | Urgent  <- Add here
```

## 3. Adding More Coverage Areas

**Location:** Rows 23-26 (Coverage data)

**Current structure:**
```
Row 23: [Area Name] | [Coverage %]
Row 24: [Area Name] | [Coverage %]
Row 25: [Area Name] | [Coverage %]
Row 26: [Area Name] | [Coverage %]
```

**To add more coverage areas:**
1. Insert a new row after Row 26
2. Add your area name and coverage percentage
3. The script will include it in the coverage chart

**Example:**
```
Row 23: Authentication | 90
Row 24: Payment | 85
Row 25: Inventory | 60
Row 26: Reporting | 75
Row 27: [NEW] User Management | 88  <- Add here
```

## 4. Adding More Risks

**Location:** Rows 30+ (Risk data)

**Current structure:**
```
Row 30: [Issue ID] | [Description] | [Priority] | [Assigned Owner] | [Target Date]
Row 31: [Issue ID] | [Description] | [Priority] | [Assigned Owner] | [Target Date]
```

**To add more risks:**
1. Copy an existing risk row
2. Add it after the last risk row
3. Update the Issue ID, Description, Priority, Owner, and Target Date
4. The script will include it in the Risks table

**Example:**
```
Row 30: API-001 | Payment Gateway: Multi-currency edge cases failing | HIGH | Michael Chen | Jan 15
Row 31: API-002 | Reporting Engine: Performance degradation >500 req/s | HIGH | David Park | Jan 16
Row 32: [NEW] API-003 | User Auth: Session timeout edge case | MEDIUM | Sarah Lee | Jan 20  <- Add here
```

## Important Notes

⚠️ **DO NOT modify:**
- Row 0: Title row
- Row 2-5: Report metadata (Period, Lead, Email)
- Row 6: Section headers
- Row 7: Column headers for test suites
- Row 12: TOTALS row
- Row 14: Section header for defects
- Row 15: Column headers for defects
- Row 21: Section header for coverage
- Row 22: Column headers for coverage
- Row 28: Section header for risks
- Row 29: Column headers for risks

✅ **Safe to modify:**
- Test suite names, numbers, and status
- Defect counts and status
- Coverage percentages
- Risk descriptions, priorities, and owners
- Add new rows for test suites, defects, coverage, and risks

## Example: Adding a New Test Suite

**Before:**
```
Row 8:  Authentication API | 156 | 152 | 3 | 1 | 97 | Stable
Row 9:  Payment Processing | 289 | 268 | 18 | 3 | 92 | Monitor
Row 10: Inventory Management | 198 | 187 | 9 | 2 | 94 | Stable
Row 11: Reporting Engine | 204 | 182 | 18 | 4 | 89 | Monitor
Row 12: TOTALS
```

**After adding "User Management":**
```
Row 8:  Authentication API | 156 | 152 | 3 | 1 | 97 | Stable
Row 9:  Payment Processing | 289 | 268 | 18 | 3 | 92 | Monitor
Row 10: Inventory Management | 198 | 187 | 9 | 2 | 94 | Stable
Row 11: Reporting Engine | 204 | 182 | 18 | 4 | 89 | Monitor
Row 12: User Management | 120 | 115 | 4 | 1 | 96 | Stable
Row 13: TOTALS
```

Then run: `python generate_all.py`

The new test suite will automatically appear in the API/Web report!

## Troubleshooting

**Q: I added a new row but it doesn't show in the report**
A: Make sure you inserted the row in the correct section and didn't accidentally modify the TOTALS or section header rows.

**Q: The numbers look wrong in the report**
A: Check that your numbers are in the correct columns (Total, Passed, Failed, Blocked, Pass Rate, Status).

**Q: I want to add more than 4 test suites**
A: You can add as many as you want! Just insert new rows before the TOTALS row.

**Q: Can I change the order of test suites?**
A: Yes! You can reorder the rows, and they will appear in that order in the report.
