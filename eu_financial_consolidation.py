"""
EU Financial Consolidation Platform
----------------------------------

This script demonstrates how to consolidate transaction data from multiple
European startups, calculate VAT liabilities and produce a summarised
Excel report.  It reads a sample dataset (`multi_startup_financials.xlsx`)
generated for demonstration purposes and outputs a consolidated view.

To run the script:

    python eu_financial_consolidation.py --input multi_startup_financials.xlsx --output consolidated_report.xlsx

Dependencies:
    pandas, openpyxl
"""

import argparse
import pandas as pd


def consolidate_transactions(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name='Transactions')
    # Summarise amount and VAT per company and currency
    summary = df.groupby(['Company','Currency','Type']).agg({'Amount':'sum','VAT':'sum'}).reset_index()
    return summary


def export_report(summary: pd.DataFrame, output_path: str) -> None:
    with pd.ExcelWriter(output_path) as writer:
        summary.to_excel(writer, sheet_name='Consolidated', index=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Consolidate multi-startup financial data")
    parser.add_argument('--input', required=True, help='Path to the multi-startup financials Excel file')
    parser.add_argument('--output', required=True, help='Path to save the consolidated report')
    args = parser.parse_args()
    summary = consolidate_transactions(args.input)
    export_report(summary, args.output)
    print(f'Consolidated report saved to {args.output}')


if __name__ == '__main__':
    main()