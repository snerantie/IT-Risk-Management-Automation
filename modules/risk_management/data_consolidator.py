"""
Risk Management Data Consolidator
Consolidates risk data from multiple business area Excel files
"""
import pandas as pd
from pathlib import Path
from typing import List, Dict
import os


class RiskDataConsolidator:
    """Consolidates risk assessment data from multiple Excel files"""
    
    # Expected columns in business area files
    BUSINESS_AREA_COLUMNS = [
        "Risk Name",
        "Category",
        "Risk Description",
        "Level of Risk Assessment",
        "Departmental Objective",
        "Control Name",
        "Control Description",
        "Control Owner",
        "Control Effectiveness",
        "Likelihood",
        "Level of Impact",
        "Risk Rating",
        "Action Plan Description",
        "Due Date",
        "Progress",
        "Budget Required",
        "Action Plan Contact",
        "Status"
    ]
    
    # Master spreadsheet columns (includes Business Area)
    MASTER_COLUMNS = ["Business Area"] + BUSINESS_AREA_COLUMNS
    
    def __init__(self, input_folder: str, logger=None):
        """
        Initialize the consolidator
        
        Args:
            input_folder: Path to folder containing business area Excel files
            logger: Logger instance
        """
        self.input_folder = Path(input_folder)
        self.logger = logger
        self.consolidated_data = None
    
    def _log(self, message, level="info"):
        """Log message if logger is available"""
        if self.logger:
            getattr(self.logger, level)(message)
        else:
            print(f"{level.upper()}: {message}")
    
    def find_risk_files(self) -> List[Path]:
        """
        Find all risk assessment Excel files in the input folder
        
        Returns:
            List of file paths
        """
        if not self.input_folder.exists():
            self._log(f"Input folder does not exist: {self.input_folder}", "error")
            return []
        
        # Look for Excel files matching the pattern
        excel_files = list(self.input_folder.glob("*.xlsx")) + list(self.input_folder.glob("*.xls"))
        
        # Filter for risk assessment files
        risk_files = [f for f in excel_files if "Operational Risk Assessment" in f.name]
        
        self._log(f"Found {len(risk_files)} risk assessment files")
        for file in risk_files:
            self._log(f"  - {file.name}")
        
        return risk_files
    
    def extract_business_area(self, filename: str) -> str:
        """
        Extract business area name from filename
        
        Args:
            filename: Name of the file
            
        Returns:
            Business area name
        """
        # Remove "Operational Risk Assessment - " prefix and file extension
        business_area = filename.replace("Operational Risk Assessment - ", "")
        business_area = business_area.replace(".xlsx", "").replace(".xls", "")
        return business_area.strip()
    
    def read_risk_file(self, file_path: Path) -> pd.DataFrame:
        """
        Read a single risk assessment Excel file
        
        Args:
            file_path: Path to Excel file
            
        Returns:
            DataFrame with risk data
        """
        try:
            self._log(f"Reading file: {file_path.name}")
            
            # Read Excel file (assuming data is in first sheet)
            df = pd.read_excel(file_path, sheet_name=0)
            
            # Normalize column names (strip whitespace, handle case variations)
            df.columns = df.columns.str.strip()
            
            # Add business area column
            business_area = self.extract_business_area(file_path.name)
            df.insert(0, "Business Area", business_area)
            
            self._log(f"  Loaded {len(df)} rows from {business_area}")
            
            return df
            
        except Exception as e:
            self._log(f"Error reading file {file_path.name}: {str(e)}", "error")
            return pd.DataFrame()
    
    def consolidate_data(self) -> pd.DataFrame:
        """
        Consolidate all risk assessment files into a single DataFrame
        
        Returns:
            Consolidated DataFrame
        """
        self._log("Starting data consolidation...")
        
        risk_files = self.find_risk_files()
        
        if not risk_files:
            self._log("No risk assessment files found!", "warning")
            return pd.DataFrame(columns=self.MASTER_COLUMNS)
        
        # Read and consolidate all files
        all_data = []
        for file_path in risk_files:
            df = self.read_risk_file(file_path)
            if not df.empty:
                all_data.append(df)
        
        if not all_data:
            self._log("No data could be read from files!", "error")
            return pd.DataFrame(columns=self.MASTER_COLUMNS)
        
        # Combine all dataframes
        consolidated_df = pd.concat(all_data, ignore_index=True)
        
        # Ensure all expected columns exist
        for col in self.MASTER_COLUMNS:
            if col not in consolidated_df.columns:
                consolidated_df[col] = None
        
        # Reorder columns to match master format
        consolidated_df = consolidated_df[self.MASTER_COLUMNS]
        
        # Clean data
        consolidated_df = self._clean_data(consolidated_df)
        
        self.consolidated_data = consolidated_df
        
        self._log(f"Consolidation complete: {len(consolidated_df)} total risks from {len(risk_files)} business areas")
        
        return consolidated_df
    
    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean and standardize data
        
        Args:
            df: Input DataFrame
            
        Returns:
            Cleaned DataFrame
        """
        # Standardize Status values
        if "Status" in df.columns:
            df["Status"] = df["Status"].str.strip().str.title()
            df["Status"] = df["Status"].replace({"Opened": "Open"})
        
        # Standardize Risk Rating values
        if "Risk Rating" in df.columns:
            df["Risk Rating"] = df["Risk Rating"].str.strip().str.title()
        
        # Standardize Category values
        if "Category" in df.columns:
            df["Category"] = df["Category"].str.strip()
        
        # Convert Due Date to datetime
        if "Due Date" in df.columns:
            df["Due Date"] = pd.to_datetime(df["Due Date"], errors="coerce")
        
        return df
    
    def save_master_spreadsheet(self, output_path: str) -> bool:
        """
        Save consolidated data to master Excel spreadsheet
        
        Args:
            output_path: Path to save the master spreadsheet
            
        Returns:
            True if successful, False otherwise
        """
        if self.consolidated_data is None or self.consolidated_data.empty:
            self._log("No data to save!", "warning")
            return False
        
        try:
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            self._log(f"Saving master spreadsheet to: {output_path}")
            
            # Save to Excel with formatting
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                self.consolidated_data.to_excel(writer, sheet_name='Risk Data', index=False)
                
                # Auto-adjust column widths
                worksheet = writer.sheets['Risk Data']
                for idx, col in enumerate(self.consolidated_data.columns):
                    max_length = max(
                        self.consolidated_data[col].astype(str).apply(len).max(),
                        len(col)
                    )
                    worksheet.column_dimensions[chr(65 + idx)].width = min(max_length + 2, 50)
            
            self._log(f"Master spreadsheet saved successfully with {len(self.consolidated_data)} risks")
            return True
            
        except Exception as e:
            self._log(f"Error saving master spreadsheet: {str(e)}", "error")
            return False
    
    def get_summary_statistics(self) -> Dict:
        """
        Get summary statistics of consolidated data
        
        Returns:
            Dictionary with statistics
        """
        if self.consolidated_data is None or self.consolidated_data.empty:
            return {}
        
        df = self.consolidated_data
        
        stats = {
            "total_risks": len(df),
            "business_areas": df["Business Area"].nunique(),
            "open_risks": len(df[df["Status"] == "Open"]),
            "closed_risks": len(df[df["Status"] == "Closed"]),
            "risks_by_priority": df["Risk Rating"].value_counts().to_dict(),
            "risks_by_category": df["Category"].value_counts().to_dict(),
            "risks_by_business_area": df["Business Area"].value_counts().to_dict()
        }
        
        return stats
