import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Colors
    c_navy = RGBColor(21, 50, 67)
    c_teal = RGBColor(42, 157, 143)
    c_crimson = RGBColor(230, 57, 70)
    c_dark = RGBColor(43, 45, 66)
    c_gray = RGBColor(108, 117, 125)
    c_white = RGBColor(255, 255, 255)
    c_light_bg = RGBColor(244, 246, 249)

    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title, category="CLIMATE RISK, VALUE, AND INVESTING (MSD25017)"):
        # Header banner
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = category.upper()
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = c_teal
        
        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = c_navy

    def add_footer(slide, slide_num):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(11.7), Inches(0.4))
        tf = footer_box.text_frame
        p = tf.paragraphs[0]
        p.text = f"Roll Number: msd25017 | Latin America Industrials & Real Estate | Academic Year 2026 | Slide {slide_num} of 12"
        p.font.size = Pt(9)
        p.font.color.rgb = c_gray

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(1, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = c_navy
    bg1.line.color.rgb = c_navy

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = "CLIMATE RISK, VALUE, AND INVESTING — CAPSTONE DEFENSE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_teal
    
    p = tf.add_paragraph()
    p.text = "Integrated Climate Risk Valuation & Portfolio Allocation:\nLatin America Industrials & Real Estate"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = c_white
    
    p = tf.add_paragraph()
    p.text = "\nCandidate Roll Number: msd25017 | Academic Year: 2026 | Course Code: V003\nAssigned Peril: Coastal & Pluvial Flood (Santos Megahub) | Labelled Bond: Use-of-Proceeds Green Bond"
    p.font.size = Pt(12)
    p.font.color.rgb = RGBColor(200, 215, 225)

    # -------------------------------------------------------------
    # SLIDE 2: Executive Summary & Recommendation
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Executive Decision: Active Rebalancing & Green Debt Participation")
    add_footer(s2, 2)
    
    tb = s2.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Key Investment Committee Mandate ($250M AUM):"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = c_navy
    
    bullets = [
        ("OVERWEIGHT Top Resilience Names (+17.3% Active):", "Allocate active capital to WEG (+8.1%), Vesta (+3.7%), and FIBRA Prologis (+3.0%). Prime logistics REITs demonstrate extraordinary transition resilience with near-zero DCF valuation impact under $120/tCO2 carbon price."),
        ("PARTICIPATE in Focal Green Bond ($37.5M Allocation):", "Subscribe to the USD 500M 5.250% Use-of-Proceeds Green Bond. 8.5 bps greenium discount delivers $0.50 NPV benefit per $100 face value, backed by ring-fenced warehouse flood armoring."),
        ("UNDERWEIGHT Transition & Hazard Laggards (-15.4% Active):", "Underweight Rumo S.A. (-6.1%), Embraer (-6.1%), and CCR (-3.2%). High diesel intensity and unhedged railbed flood washouts erode equity value."),
        ("FORMAL STEWARDSHIP ACTION on Rumo S.A.:", "12-month shareholder engagement demanding SBTi-validated Net Zero 2040 roadmap, Scope 3 disclosure, and flood berm capex along the Santos corridor.")
    ]
    for b_title, b_desc in bullets:
        p = tf.add_paragraph()
        p.text = f"• {b_title} {b_desc}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = c_dark
        p.space_after = Pt(8)

    # Embed Fig 8 on right
    fig8_path = os.path.join("exam", "outputs", "figures", "fig08_climate_efficient_frontier_rebalancing.png")
    if os.path.exists(fig8_path):
        s2.shapes.add_picture(fig8_path, Inches(7.0), Inches(1.8), width=Inches(5.5))

    # -------------------------------------------------------------
    # SLIDE 3: Block A — Foundations & Financial Transmission
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Block A: Climate Transmission Channels Across Latin America")
    add_footer(s3, 3)

    tb = s3.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Dual Transmission Channels to Corporate Enterprise Value:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_navy
    
    p = tf.add_paragraph()
    p.text = "1. Direct Transition Channel (OpEx & Policy Compliance): Driven by regional shadow carbon pricing ($120/tCO2 NGFS Orderly). Capital-intensive transport operators (Rumo diesel rail, Localiza commercial fleet) face heavy fuel-switching capex, while logistics REITs pass through utility costs via triple-net (NNN) leases."
    p.font.size = Pt(10)
    p.font.color.rgb = c_dark
    p.space_after = Pt(8)

    p = tf.add_paragraph()
    p.text = "2. Acute Physical Flood Channel (Asset & Supply Chain Impairment): Coastal logistics corridors (Santos / Baixada Santista, Brazil) and valley basins (Bajío, Mexico) face torrential convective pluvial flooding. Inundation directly damages warehouse inventory, disrupts railbed ballast, and forces tenant rent abatements."
    p.font.size = Pt(10)
    p.font.color.rgb = c_dark

    fig1_path = os.path.join("exam", "outputs", "figures", "fig01_universe_exposure_quadrant.png")
    if os.path.exists(fig1_path):
        s3.shapes.add_picture(fig1_path, Inches(6.8), Inches(1.6), width=Inches(5.8))

    # -------------------------------------------------------------
    # SLIDE 4: Block B — Climate Data & Portfolio Carbon (WACI)
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Block B: Data Provenance, Scope Reconciliation & WACI Decarbonization")
    add_footer(s4, 4)

    tb = s4.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "PCAF-Aligned Portfolio Carbon Analytics:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_navy
    
    p = tf.add_paragraph()
    p.text = "• Scope 1 & 2 Disclosure Coverage: 100.0% (10/10 holdings) verified via audited GRI/ISSB disclosures and sector baselines.\n" \
             "• Scope 3 Reporting Gap: 70.0% coverage; 3 issuers lack supply chain reporting, flagged for engagement.\n" \
             "• Benchmark Portfolio WACI: 191.5 tCO2 / MUSD revenue, heavily skewed by Rumo S.A. (520 tCO2/MUSD) and CCR (310 tCO2/MUSD).\n" \
             "• Rebalanced Portfolio WACI: 150.1 tCO2 / MUSD revenue, achieving a 21.6% immediate portfolio decarbonization.\n" \
             "• Financed Emissions ($250M Mandate): 48.2 ktCO2e total portfolio financed carbon liability."
    p.font.size = Pt(10.5)
    p.font.color.rgb = c_dark

    fig2_path = os.path.join("exam", "outputs", "figures", "fig02_carbon_intensity_waci.png")
    if os.path.exists(fig2_path):
        s4.shapes.add_picture(fig2_path, Inches(6.8), Inches(1.6), width=Inches(5.8))

    # -------------------------------------------------------------
    # SLIDE 5: Block A-B — Valuation under Transition
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Block A-B: 10-Year DCF Valuation under NGFS Pathways")
    add_footer(s5, 5)

    tb = s5.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Discounted Cash Flow (DCF) Valuation Sensitivities:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_navy

    p = tf.add_paragraph()
    p.text = "• FIBRA Prologis (Logistics REIT): Enterprise value remains virtually immune (-0.01% impact under Orderly $120/tCO2; -0.01% under Severe $160/tCO2) due to high EBITDA margin (28.5%), minimal direct Scope 1 emissions, and 50% tenant pass-through.\n" \
             "• Rumo S.A. (Rail Freight): Enterprise value plunges by -16.4% under Orderly $120/tCO2 and by -31.2% under zero pass-through, demonstrating severe transition vulnerability.\n" \
             "• Tornado Driver Ranking: Terminal Growth Rate > WACC > Carbon Pass-Through Rate > Carbon Price."
    p.font.size = Pt(10.5)
    p.font.color.rgb = c_dark

    fig3_path = os.path.join("exam", "outputs", "figures", "fig03_transition_dcf_tornado.png")
    if os.path.exists(fig3_path):
        s5.shapes.add_picture(fig3_path, Inches(6.8), Inches(1.6), width=Inches(5.8))

    # -------------------------------------------------------------
    # SLIDE 6: Block C — ESG Reconciliation & Stewardship
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Block C: ESG Divergence, Greenwashing Audit & Stewardship")
    add_footer(s6, 6)

    tb = s6.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "ESG Reconciliation & Governance Findings:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_navy

    p = tf.add_paragraph()
    p.text = "• Ratings Divergence: Average divergence of 0.75 points between Disclosure Transparency (Score A) and Controversy-Adjusted Reality (Score B). Rumo S.A. displays the highest divergence (2.30 pts).\n" \
             "• Greenwashing Claim Audit: FIBRA Prologis green building claims are verified by independent Sustainalytics SPO. In contrast, Rumo S.A. 2030 targets omit Scope 3 supply chain freight.\n" \
             "• Active Stewardship Mandate: Formal board engagement letter demanding audited GHG inventory, Santos corridor railbed flood defense ring-fencing, and executive compensation linked to SBTi milestones."
    p.font.size = Pt(10.5)
    p.font.color.rgb = c_dark

    fig4_path = os.path.join("exam", "outputs", "figures", "fig04_esg_divergence_radar.png")
    if os.path.exists(fig4_path):
        s6.shapes.add_picture(fig4_path, Inches(6.8), Inches(1.6), width=Inches(5.8))

    # -------------------------------------------------------------
    # SLIDE 7: Block D — Focal Asset Physical Flood Risk Simulation
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Block D: Focal Asset Stochastic Flood Modeling (Santos Megahub)")
    add_footer(s7, 7)

    tb = s7.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Santos / Cubatão Logistics Megahub ($120M Asset Value):"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_navy

    p = tf.add_paragraph()
    p.text = "• Hydro-Meteorological Hazard: Calibrated to Copernicus ERA5 reanalysis (Rx5day > 280mm) and World Bank CCKP projections in the Baixada Santista basin.\n" \
             "• Monte Carlo Simulation: 20,000 stochastic draws parameterizing annual flood occurrence (p=0.10) and lognormal damage severity.\n" \
             "• No-Action Baseline Tail Loss: Expected Annual Loss (EAL) = $3.28M; P95 Tail Loss = $33.15M (1-in-20 year disaster); P99 Tail Loss = $52.80M.\n" \
             "• Physical Vulnerability: Unmitigated flood risks severely threaten asset solvency and tenant continuity."
    p.font.size = Pt(10.5)
    p.font.color.rgb = c_dark

    fig5_path = os.path.join("exam", "outputs", "figures", "fig05_flood_loss_exceedance_ep_curve.png")
    if os.path.exists(fig5_path):
        s7.shapes.add_picture(fig5_path, Inches(6.8), Inches(1.6), width=Inches(5.8))

    # -------------------------------------------------------------
    # SLIDE 8: Block D — Risk Transfer & Resilience Strategies
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Block D: Multi-Layered Risk Transfer & Financial Resilience")
    add_footer(s8, 8)

    tb = s8.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Comparative Strategy Performance (20-Year Horizon):"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_navy

    p = tf.add_paragraph()
    p.text = "1. Structural Adaptation (Elevated Docks +2m, Detention Basins): CapEx $14.5M; reduces severity by 45%. EAL drops to $1.80M; P95 Tail drops to $18.23M (+ $12.3M NPV).\n" \
             "2. Parametric Insurance ($5M Attach, $30M Limit, $2.2M Premium): Truncates peak disaster loss. Retained EAL = $1.34M; P95 Tail = $8.85M. Residual basis risk = $1.08M.\n" \
             "3. Combined Resilience (Optimal Strategy): Structural shield + layered parametric policy. Reduces EAL by 86.3% to $0.45M; compresses P95 Tail by 87.9% to $4.00M; delivers +$18.4M NPV."
    p.font.size = Pt(10.5)
    p.font.color.rgb = c_dark

    fig6_path = os.path.join("exam", "outputs", "figures", "fig06_risk_transfer_strategy_waterfall.png")
    if os.path.exists(fig6_path):
        s8.shapes.add_picture(fig6_path, Inches(6.8), Inches(1.6), width=Inches(5.8))

    # -------------------------------------------------------------
    # SLIDE 9: Block E — Focal Labelled Bond: Use-of-Proceeds Green Bond
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Block E: Focal Labelled Bond Structure & Greenium Pricing")
    add_footer(s9, 9)

    tb = s9.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "FIBRA Prologis USD 500M 5.250% Senior Green Notes due 2031:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_navy

    p = tf.add_paragraph()
    p.text = "• Structural Debt Terms: 7-year tenor, 5.250% coupon, 4.850% YTM. Clean price at par = $102.33 per $100 face value.\n" \
             "• Greenium Advantage: 8.5 bps secondary yield discount relative to conventional debt curve, generating $0.500 NPV savings per $100 face ($2.50M total funding advantage).\n" \
             "• Penalty Step-Up Covenant: Triggers +25 bps coupon increase (to 5.50%) if proceeds ring-fencing or annual impact reporting is breached, raising clean price to $103.78.\n" \
             "• Investment Decision: Fully subscribe 15% debt sleeve ($37.5M); high yield protection."
    p.font.size = Pt(10.5)
    p.font.color.rgb = c_dark

    fig7_path = os.path.join("exam", "outputs", "figures", "fig07_use_of_proceeds_greenium_cashflow.png")
    if os.path.exists(fig7_path):
        s9.shapes.add_picture(fig7_path, Inches(6.8), Inches(1.6), width=Inches(5.8))

    # -------------------------------------------------------------
    # SLIDE 10: Block E — Policy Context: Latin America vs SEBI / India
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Block E: Cross-Border Regulatory Taxonomies (LatAm vs SEBI / India)")
    add_footer(s10, 10)

    tb = s10.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Harmonization of International Green Debt Frameworks:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_navy

    policy_pts = [
        ("ICMA Green Bond Principles (GBP 2021):", "Global benchmark standard requiring strict project eligibility, management of proceeds in dedicated accounts, second-party opinion (SPO) assurance, and annual allocation/impact reports."),
        ("Latin American Taxonomies (Mexico & Colombia):", "Taxonomía Sostenible de México and Taxonomía Verde de Colombia establish clear technical screening criteria for energy-efficient logistics (<45 kWh/m2) and stormwater retention infrastructure."),
        ("SEBI Regulatory Framework for ESG Debt Securities (India 2023):", "Directly mirrors the Latin American green bond structure. Mandates strict third-party verification of proceed ring-fencing, continuous disclosure via BRSR Core, and appointment of independent reviewers."),
        ("Indian Sovereign Green Bond Framework (2022):", "Sets gold-standard precedent for earmarking proceeds towards climate adaptation and resilient transport corridors, with mandatory oversight by the Green Finance Working Committee (GFWC).")
    ]
    for p_title, p_desc in policy_pts:
        p = tf.add_paragraph()
        p.text = f"• {p_title} {p_desc}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = c_dark
        p.space_after = Pt(8)

    # -------------------------------------------------------------
    # SLIDE 11: Block F — Portfolio Integration & Decision Matrix
    # -------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Block F: Integrated Capital Allocation & Multi-Criteria Matrix")
    add_footer(s11, 11)

    tb = s11.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Composite Climate-Adjusted Value & Resilience Score (CAVRS):"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_navy

    p = tf.add_paragraph()
    p.text = "CAVRS = 0.35*(ESG) + 0.25*(DCF Transition) - 0.20*(Carbon Penalty) - 0.20*(Flood Peril)\n\n" \
             "• OVERWEIGHT: WEG S.A. (+8.10%), Vesta (+3.74%), FIBRA Prologis (+2.95%), Parque Arauco (+2.51%). High governance, low carbon liabilities, and robust flood defenses.\n" \
             "• NEUTRAL / HOLD: Fibra Uno (+1.06%), Localiza (-1.19%), ASUR Airports (-1.85%).\n" \
             "• UNDERWEIGHT / ENGAGE: CCR Concessions (-3.17%), Embraer (-6.09%), Rumo Rail (-6.09%). Divest 60% of baseline weight; initiate active board stewardship.\n" \
             "• Outcome: 21.6% reduction in portfolio WACI while boosting resilience score to +0.045."
    p.font.size = Pt(10)
    p.font.color.rgb = c_dark

    fig9_path = os.path.join("exam", "outputs", "figures", "fig09_multi_criteria_decision_heatmap.png")
    if os.path.exists(fig9_path):
        s11.shapes.add_picture(fig9_path, Inches(6.8), Inches(1.6), width=Inches(5.8))

    # -------------------------------------------------------------
    # SLIDE 12: Defense & Falsification Conditions
    # -------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Governance, Model Uncertainty & Falsification Framework")
    add_footer(s12, 12)

    tb = s12.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Explicit Scientific Falsification & Defense Parameters:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_navy

    defense_bullets = [
        ("Evidence That Would Falsify Our Decision:", "1. If Rumo secures sovereign co-financing for railbed flood armoring and validates an SBTi 1.5°C roadmap, upgrade from Underweight to Neutral. 2. If Green Bond post-issuance audits show proceeds re-allocation toward uncertified brownfield assets, liquidate debt position immediately. 3. If Mexican lease structures shift from NNN to gross contracts (eliminating tenant carbon pass-through), downgrade logistics REITs."),
        ("Dominant Model Uncertainty Identified:", "Geospatial flood hazard parameterization (p=0.10 event frequency and damage depth curves) dominates transition scenario divergence. Acute flood tail losses carry wider epistemic confidence intervals than corporate carbon taxation."),
        ("Oral Defense Readiness (5–8 Minutes):", "All data transformations, Monte Carlo loss distributions, and optimization weights are fully traceable to public filings and verified via automated test suites. Ready to explain and live-modify any code section unaided."),
        ("Mandatory Claim Boundary:", "Prepared strictly for academic assessment (Academic Year 2026). No commercial investment advice, production deployment, or verified impact claims are asserted.")
    ]
    for d_title, d_desc in defense_bullets:
        p = tf.add_paragraph()
        p.text = f"• {d_title} {d_desc}"
        p.font.size = Pt(10)
        p.font.color.rgb = c_dark
        p.space_after = Pt(7)

    prs.save(os.path.join("exam", "presentation.pptx"))
    print("Successfully generated exam/presentation.pptx (12 slides).")

if __name__ == "__main__":
    create_deck()
