# EU Financial Consolidation Platform

This project simulates the work performed as a freelance accountant for multiple EU startups. It consolidates multi‑currency transactions, calculates VAT liabilities and generates investor‑ready reports and dashboards.

## Scenario

As a freelance accountant overseeing the books for several European SaaS companies, you needed a unified view of revenue, expenses and VAT across jurisdictions. Each startup operated in different currencies and had unique tax rates. To scale your services and reduce manual effort, you built an automated consolidation platform.

## Key Features

* **Multi‑company ingestion** – Load transaction exports for several startups and standardise the data (date, currency, type and amount).
* **VAT calculation** – Apply country‑specific VAT rates and calculate liabilities automatically.
* **Currency conversion** – Convert USD and GBP transactions into EUR for unified reporting.
* **Consolidated reporting** – Summarise revenue and expenses by company and currency and produce an Excel report with coloured headers and a separate summary sheet.

## Files

* `multi_startup_financials.xlsx` – Mock transaction data for four startups with multi‑currency revenue and expense transactions. The workbook includes a coloured header row and a summary tab.
* `eu_financial_consolidation.py` – Python script that reads the dataset, consolidates amounts and VAT per company and outputs a report.

## Usage

Run the script from the command line to generate a consolidated report:

```bash
python eu_financial_consolidation.py --input multi_startup_financials.xlsx --output consolidated_report.xlsx
```

The resulting `consolidated_report.xlsx` will contain a `Consolidated` sheet showing totals per company, currency and transaction type.