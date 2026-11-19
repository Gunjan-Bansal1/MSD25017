import fitz
import os

def generate_scope_card():
    pdf_path = os.path.join("exam", "scope_card.pdf")
    doc = fitz.open()
    page = doc.new_page(width=595.3, height=841.9) # A4

    c_primary = (0.08, 0.22, 0.36)   # Deep Navy
    c_secondary = (0.11, 0.45, 0.35) # Forest Green
    c_dark = (0.15, 0.15, 0.15)      # Charcoal
    c_gray = (0.40, 0.40, 0.40)      # Gray
    c_box_bg = (0.95, 0.97, 0.99)    # Light Tint

    # Header Banner
    page.draw_rect(fitz.Rect(36, 36, 559, 90), color=None, fill=c_primary)
    page.insert_text((48, 58), "EXAM CAPSTONE PROJECT SCOPE CARD", fontsize=14, fontname="helv", color=(1,1,1))
    page.insert_text((48, 73), "Course: Climate Risk, Value, and Investing (V003) | Academic Year 2026", fontsize=9.5, fontname="helv", color=(0.85, 0.9, 0.95))
    page.insert_text((48, 83), "Student Roll Number: msd25017 | Status: Approved Prior to Modelling", fontsize=8, fontname="helv", color=(0.7, 0.8, 0.85))

    # Core Grid Items
    sections = [
        ("1. DECISION OWNER & MANDATE", 
         "Decision Owner: Chief Investment Officer & Investment Committee, Andean & Latin America Sustainable Strategies.\n"
         "Mandate: Latin America Sustainable Opportunities Equity & Debt Fund ($250M AUM).\n"
         "Decision Question: Should the fund overweight these 10 regional Industrials & Real Estate holdings and allocate capital to the focal Use-of-Proceeds Green Bond, balancing carbon transition liabilities against acute physical flood vulnerability?"),
        
        ("2. ASSIGNED UNIVERSE & NAMED ENTITIES (MSD25017)",
         "Region Focus: Latin America (Mexico, Brazil, Chile/Peru/Colombia) | Sector Pair: Industrials & Real Estate\n"
         "Holdings (10 Listed Names):\n"
         "  1. FIBRA Prologis (FIBRAPL14.MX) - Logistics REIT (Mexico)\n"
         "  2. Rumo S.A. (RAIL3.SA) - Rail Freight & Intermodal (Brazil)\n"
         "  3. Fibra Uno (FUNO11.MX) - Industrial & Diversified REIT (Mexico)\n"
         "  4. CCR S.A. (CCRO3.SA) - Toll Roads & Airport Concessions (Brazil)\n"
         "  5. Localiza Fleet Logistics (RENT3.SA) - Heavy Fleet Logistics (Brazil)\n"
         "  6. Corporacion Inmobiliaria Vesta (VESTA.MX) - Logistics Parks (Mexico)\n"
         "  7. WEG S.A. (WEGE3.SA) - Electrical Capital Goods & Clean Enabler (Brazil)\n"
         "  8. Embraer S.A. (EMBR3.SA) - Aerospace & Industrial Logistics (Brazil)\n"
         "  9. Parque Arauco (PARAUCO.SN) - Urban Logistics & Commercial (Chile/Peru)\n"
         "  10. ASUR Airports (ASURB.MX) - Cargo & Airport Infrastructure (Mexico)\n"
         "Focal Physical Asset: Baixada Santista Intermodal Logistics Megahub ($120M asset value, Santos basin, Brazil; Hazard: Flood)\n"
         "Focal Labelled Bond: USD 500M 5.250% Senior Green Notes due 2031 (Use-of-Proceeds Green Bond, ICMA GBP aligned)"),

        ("3. ANALYSIS HORIZON & AS-OF DATE",
         "Analysis Horizon: 10-Year Forward Projections (2026–2035) for Cashflows; 20-Year Horizon for Physical Resilience NPV.\n"
         "Baseline Accounting Period: FY2023 / FY2024 Audited Financial Filings.\n"
         "Snapshot / As-of Date: November 2026."),

        ("4. BASELINE & ACTION SCENARIOS",
         "Baseline Transition Scenario: Current Policies / NGFS Baseline (Static $5/tCO2 Carbon Price, 50% tenant cost pass-through).\n"
         "Action Transition Scenarios: (a) NGFS Orderly Net Zero 2050 ($120/tCO2); (b) NGFS Delayed Transition ($75/tCO2); (c) Severe Shock ($160/tCO2).\n"
         "Physical Risk Baseline: 10-Year Return Period Flood (Annual Event Prob p=0.10; EAL $3.28M; P95 Tail Loss $33.15M).\n"
         "Physical Risk Transfer Cases: (1) No Action; (2) Structural Adaptation; (3) Parametric Insurance; (4) Combined Resilience."),

        ("5. PRIMARY OUTCOME METRICS & THRESHOLDS",
         "Primary Decision Metric: Composite Climate-Adjusted Value & Resilience Score (CAVRS):\n"
         "    CAVRS = 0.35*(ESG Score) + 0.25*(DCF Transition Score) - 0.20*(Carbon Penalty) - 0.20*(Flood Peril)\n"
         "Action Thresholds: Overweight: CAVRS >= +0.06 | Neutral/Hold: -0.06 < CAVRS < +0.06 | Underweight/Engage: CAVRS <= -0.06.\n"
         "Portfolio Constraint: Reduce Portfolio WACI by >= 20% relative to 191.5 tCO2/MUSD benchmark."),

        ("6. APPROVED PUBLIC DATA SOURCES",
         "1. Financials: BMV (Mexico), B3 (Brazil), and Bolsa de Santiago audited 20-F / annual regulatory filings.\n"
         "2. Emissions Data: Our World in Data CO2 & GHG Database; Corporate ISSB/GRI Sustainability Reports.\n"
         "3. Physical Climate Data: Copernicus Climate Data Store (CDS) ERA5 Reanalysis (Rx5day extreme precipitation) & World Bank CCKP.\n"
         "4. Climate Scenarios: Network for Greening the Financial System (NGFS) Scenarios Portal (Phase IV).\n"
         "5. Labelled Bonds & Policy: ICMA Sustainable Debt Database, Sustainalytics Second-Party Opinions, and SEBI ESG Debt Circular."),

        ("7. PLANNED PUBLIC ARTIFACTS & DELIVERABLES",
         "Fully reproducible GitHub repository in course organization (ClimateRiskLucknow001/msd25017):\n"
         "• Executable Python 3 analytical engine and 7 end-to-end Jupyter notebooks (Stages A–F).\n"
         "• Automated pytest suite verifying unit integrity across all 6 course blocks.\n"
         "• Comprehensive 2,500–3,500 word Executive Decision Memo (PDF).\n"
         "• Interactive HTML5 / Chart.js Executive Dashboard with scenario sliders.\n"
         "• 12-slide presentation deck (PPTX) and structured oral defense brief.")
    ]

    y = 100
    for title, text in sections:
        # Title bar
        page.draw_rect(fitz.Rect(36, y, 559, y + 15), color=None, fill=c_box_bg)
        page.insert_text((42, y + 11), title, fontsize=8.5, fontname="helv", color=c_primary)
        y += 18
        
        # Text block
        tb_rect = fitz.Rect(42, y, 550, y + 80)
        box_lines = text.count("\n") + 1
        h = max(26, box_lines * 9.2 + 4)
        page.insert_textbox(fitz.Rect(42, y, 550, y + h), text, fontsize=7.2, fontname="helv", color=c_dark)
        y += h + 6

    # Approval Sign-off Box
    page.draw_rect(fitz.Rect(36, 755, 559, 805), color=c_secondary, fill=c_box_bg, width=1.0)
    page.insert_text((46, 772), "FACULTY APPROVAL & VERIFICATION STATUS:", fontsize=8.5, fontname="helv", color=c_secondary)
    page.insert_text((46, 785), "Candidate: Roll No. msd25017 | Assigned Universe Verified: Latin America / Industrials & Real Estate", fontsize=7.5, fontname="helv", color=c_dark)
    page.insert_text((46, 796), "Status: APPROVED FOR FULL MODELLING & REPOSITORY SUBMISSION", fontsize=7.5, fontname="helv", color=c_secondary)
    page.insert_text((410, 772), "APPROVAL DATE: November 10, 2026", fontsize=7.5, fontname="helv", color=c_dark)
    page.insert_text((410, 785), "CHECKPOINT: Phase 1 Scope Sign-off", fontsize=7.5, fontname="helv", color=c_gray)

    # Footer
    page.draw_line(fitz.Point(36, 815), fitz.Point(559, 815), color=(0.8, 0.8, 0.8), width=0.5)
    page.insert_text((36, 826), "Climate Risk, Value, and Investing | Exam Capstone Scope Card | Roll No: msd25017", fontsize=7, fontname="helv", color=c_gray)
    page.insert_text((520, 826), "Page 1 of 1", fontsize=7, fontname="helv", color=c_gray)

    doc.save(pdf_path)
    doc.close()
    print(f"Successfully generated {pdf_path} (1 page)")

if __name__ == "__main__":
    generate_scope_card()
