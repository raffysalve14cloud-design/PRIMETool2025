# PRIME Tool Export Functionality

## Excel Export Features
- Export all employers
- Export by branch
- Export delinquent employers
- Export unregistered employers
- Custom column selection
- Timestamped filenames

## Export Locations

### Android APK
1. **Primary**: `/storage/emulated/0/Download/PRIME_Exports/`
2. **Fallback**: `/storage/emulated/0/Documents/PRIME_Exports/`
3. **App Storage**: `[app_storage]/files/exports/`

### Desktop
- `./exports/` (in project directory)

## File Format
Excel files (.xlsx) with the following naming convention:
- All employers: `PRIME_All_Employers_YYYYMMDD_HHMMSS.xlsx`
- Branch: `PRIME_Branch_[BranchName]_YYYYMMDD_HHMMSS.xlsx`
- Delinquent: `PRIME_All_Delinquent_Employers_YYYYMMDD_HHMMSS.xlsx`
- Unregistered: `PRIME_All_Unregistered_YYYYMMDD_HHMMSS.xlsx`

## Android Permissions Required
- WRITE_EXTERNAL_STORAGE
- READ_EXTERNAL_STORAGE

## Dependencies
- openpyxl (Excel file creation)
- et_xmlfile (Excel XML support)
- jdcal (Date calculations for Excel)