#!/usr/bin/env python3
"""
Risk Management Module Runner
Automates risk data consolidation, chart generation, and PowerPoint updates
"""
import sys
from pathlib import Path
from datetime import datetime
import yaml

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.logger import setup_logger
from utils.config_loader import load_config
from modules.risk_management.data_consolidator import RiskDataConsolidator
from modules.risk_management.chart_generator import RiskChartGenerator
from modules.risk_management.ppt_updater import RiskPowerPointUpdater


def print_banner():
    """Print welcome banner"""
    print("\n" + "="*70)
    print(" " * 15 + "TPR AUTOMATION SYSTEM")
    print(" " * 12 + "Risk Management Module")
    print("="*70 + "\n")


def print_summary(statistics, chart_files):
    """Print summary of results"""
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"\n📊 Data Statistics:")
    print(f"   Total Risks: {statistics.get('total_risks', 0)}")
    print(f"   Open Risks: {statistics.get('open_risks', 0)}")
    print(f"   Closed Risks: {statistics.get('closed_risks', 0)}")
    print(f"   Business Areas: {statistics.get('business_areas', 0)}")
    
    if statistics.get('risks_by_priority'):
        print(f"\n   Risks by Priority:")
        for priority, count in statistics['risks_by_priority'].items():
            print(f"     - {priority}: {count}")
    
    if statistics.get('risks_by_category'):
        print(f"\n   Risks by Category:")
        for category, count in statistics['risks_by_category'].items():
            print(f"     - {category}: {count}")
    
    print(f"\n📈 Charts Generated:")
    for chart_name, chart_path in chart_files.items():
        print(f"   ✓ {chart_name}: {chart_path}")
    
    print("\n" + "="*70 + "\n")


def main():
    """Main execution function"""
    print_banner()
    
    # Set up logger
    logger = setup_logger()
    logger.info("Starting Risk Management Module")
    
    try:
        # Load configuration
        logger.info("Loading configuration...")
        config = load_config()
        
        # Get paths from config
        input_folder = Path(config['paths']['input_data']) / 'risk'
        output_folder = Path(config['paths']['output_data'])
        master_spreadsheet_path = config['paths']['master_spreadsheet']
        
        # Create folders if they don't exist
        input_folder.mkdir(parents=True, exist_ok=True)
        output_folder.mkdir(parents=True, exist_ok=True)
        
        # Check if input files exist
        excel_files = list(input_folder.glob("*.xlsx")) + list(input_folder.glob("*.xls"))
        if not excel_files:
            logger.warning(f"\n⚠️  No Excel files found in: {input_folder}")
            logger.warning("Please place your risk assessment Excel files in this folder and run again.")
            logger.warning("Expected file naming: 'Operational Risk Assessment - [Tech Lead Name].xlsx'")
            return
        
        # Step 1: Consolidate data
        logger.info("\n" + "="*70)
        logger.info("STEP 1: Data Consolidation")
        logger.info("="*70)
        
        consolidator = RiskDataConsolidator(str(input_folder), logger)
        consolidated_data = consolidator.consolidate_data()
        
        if consolidated_data.empty:
            logger.error("No data could be consolidated. Exiting.")
            return
        
        # Save master spreadsheet
        consolidator.save_master_spreadsheet(master_spreadsheet_path)
        
        # Get statistics
        statistics = consolidator.get_summary_statistics()
        
        # Step 2: Generate charts
        logger.info("\n" + "="*70)
        logger.info("STEP 2: Chart Generation")
        logger.info("="*70)
        
        chart_generator = RiskChartGenerator(
            consolidated_data,
            str(output_folder),
            config['risk_management']['charts'],
            logger
        )
        chart_files = chart_generator.generate_all_charts()
        
        # Step 3: Update PowerPoint (optional - only if template exists)
        logger.info("\n" + "="*70)
        logger.info("STEP 3: PowerPoint Update")
        logger.info("="*70)
        
        template_path = Path(config['paths']['templates']) / config['powerpoint']['template_file']
        
        if template_path.exists():
            # Generate output filename with current month/year
            now = datetime.now()
            output_filename = config['powerpoint']['output_file'].format(
                month=now.strftime('%B'),
                year=now.year
            )
            output_ppt_path = output_folder / output_filename
            
            ppt_updater = RiskPowerPointUpdater(
                str(template_path),
                str(output_ppt_path),
                logger
            )
            
            if ppt_updater.load_template():
                slide_number = config['powerpoint']['risk_slide_number']
                ppt_updater.update_risk_slide(
                    slide_number,
                    consolidated_data,
                    chart_files,
                    statistics
                )
                ppt_updater.save_presentation()
        else:
            logger.warning(f"PowerPoint template not found: {template_path}")
            logger.info("Creating standalone presentation with charts...")
            
            output_ppt_path = output_folder / f"Risk_Report_{datetime.now().strftime('%Y%m%d')}.pptx"
            ppt_updater = RiskPowerPointUpdater(
                str(template_path),
                str(output_ppt_path),
                logger
            )
            ppt_updater.create_new_presentation_with_charts(
                consolidated_data,
                chart_files,
                statistics
            )
        
        # Print summary
        print_summary(statistics, chart_files)
        
        logger.info("✅ Risk Management Module completed successfully!")
        logger.info(f"📁 Output location: {output_folder}")
        
    except Exception as e:
        logger.error(f"❌ Error running Risk Management Module: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
