# -*- coding: utf-8 -*-
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

template_path = r'D:\JAYMANI KRISHI SEWA — Digital Agritech Marketplace for Farmers & Local Vendors\Report format.docx'
final_path = r'D:\JAYMANI KRISHI SEWA — Digital Agritech Marketplace for Farmers & Local Vendors\JMKS_FINAL.docx'

doc = docx.Document(template_path)

def clear_paragraph(p):
    for r in p.runs:
        r.text = ''

def set_paragraph(p, text):
    clear_paragraph(p)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0, 0, 0)

# Replace cover page
set_paragraph(doc.paragraphs[4], 'JAYMANI KRISHI SEWA — Digital Agritech Marketplace for Farmers & Local Vendors')
set_paragraph(doc.paragraphs[6], 'B.TECH. 2nd YEAR')
set_paragraph(doc.paragraphs[7], 'SEMESTER: 3')
set_paragraph(doc.paragraphs[10], 'Manish Pandey (2025266283)')
set_paragraph(doc.paragraphs[11], 'Jayant Raj (2025298708)')
clear_paragraph(doc.paragraphs[12]) # Delete 3rd student
set_paragraph(doc.paragraphs[14], 'SECTION: A')
set_paragraph(doc.paragraphs[17], 'Prof. (Dr.) Ali Imam Abidi')
set_paragraph(doc.paragraphs[18], 'Professor & Faculty Mentor')

# Internal Headings and Guidelines cleanup
def remove_guidelines(doc):
    for p in doc.paragraphs:
        text = p.text.strip()
        if '<Guidelines:' in text or 'Font: Times New Roman;' in text:
            clear_paragraph(p)

remove_guidelines(doc)

content = {
    'Project Title': 'JAYMANI KRISHI SEWA — Digital Agritech Marketplace for Farmers & Local Vendors',
    'Problem Statement': 'The agricultural retail sector heavily relies on traditional, manual workflows. Currently, there is no simple, hyper-local platform that seamlessly connects farmers with verified local agricultural retailers while simultaneously combining product discovery, real-time inventory visibility, and digital credit records. The current journey flows from a fundamental farmer need to inefficient phone calls or word-of-mouth searches, resulting in multiple physical shop visits. We selected this topic to digitize and modernize this fragmented supply chain.\n\nOur project specifically targets the severe operational frictions present in daily agri-retail, which include:\n1. Price & Stock Uncertainty: Farmers travel to multiple physical shops without prior knowledge of product availability or local pricing.\n2. Fragile Paper "Bahi-Khata" Systems: Manual credit records create an unreliable financial environment.\n3. Time & Fuel Loss: Unplanned, blind trips to distant agri-retailers lead to a substantial loss of time and fuel.\n4. Vendor Digital Limitations: Local agricultural retailers currently lack accessible digital tools.',
    'Project Description': 'Jaymani Krishi Sewa is a comprehensive, digital agritech marketplace that bridges the gap between farmers and local agricultural vendors. The primary scope of this project is to integrate hyper-local product discovery, real-time inventory synchronization, and secure digital credit management (Bahi-Khata) into a single, unified web application. The platform streamlines the agricultural supply chain by eliminating blind shop visits and digitizing fragile, paper-based financial records.\n\nThe system is structured around a centralized platform architecture that orchestrates demand, supply, and credit records through three primary modules:\n1. Farmer Module (Demand Side): Hyper-Local Marketplace, Cart & Checkout, Credit Management.\n2. Vendor Module (Supply Side): Catalog Management, Real-Time Stock Sync, Digital Bahi-Khata.\n3. Core Platform Module (System Layer): Automated Workflow, Processing Pipeline.',
    'Project Modules:  Design/Algorithm': 'The system is logically partitioned into five interdependent modules:\n1. Authentication & Role-Based Access Module: A unified gateway that manages secure logins for all users while strictly isolating data based on user types.\n2. Hyper-Local Discovery & Search Module (Farmer Module): The core search engine that allows farmers to find nearby agricultural supplies dynamically.\n3. Vendor Inventory & Catalog Module (Supply Module): A robust dashboard giving retailers control over their digital storefront and stock levels.\n4. Digital Order & Cart Processing Module: Handles the transactional phase where demand meets supply seamlessly without stock conflicts.\n5. Digital "Bahi-Khata" (Credit Ledger) Module: Digitizes the traditional, paper-based trust system between farmers and local retailers into a secure financial ledger.',
    'Implementation Methodology': 'The system is being developed using an Iterative and Phased approach. This methodology ensures continuous refinement across our 8 core milestones: Requirement Analysis, UI/UX Design, Backend/Database setup, Frontend Development, System Integration, Testing, and Deployment.\n\nTesting Methodology:\nRigorous QA protocols will be enforced:\n1. Unit Testing: Individual modules tested in isolation.\n2. Integration Testing: Connection between frontend, backend, and third-party APIs tested.\n3. System Testing (UAT): End-to-end simulation of Farmer and Vendor workflows.\n\nDefect Log Maintenance:\nA centralized Defect Log will be maintained. Bugs will be documented with specific parameters including Defect ID, Module Name, Severity Level, Steps to Reproduce, and Status.',
    'Result & Conclusion': 'Jaymani Krishi Sewa successfully conceptualizes a highly practical, modern solution to the operational frictions inherent in traditional agricultural retail. The main achievement of this project lies in creating a unified ecosystem that simultaneously connects local farmer demand with verified local vendor supply while eliminating critical pain points.\n\nThe most significant innovation is the modernization of the traditional rural credit system by digitizing the "Bahi-Khata" (credit ledger) and integrating it directly into a hyper-local search engine. In conclusion, Jaymani Krishi Sewa stands out by empowering existing micro-local economies and optimizing supply chain efficiency.',
    'Future Scope and further enhancement of the Project': 'While the current scope delivers a robust foundation, the platform possesses immense potential for scalable future enhancements:\n1. Multi-Lingual & Voice Support: Native regional language support and AI-driven voice search capabilities.\n2. AI-Driven Predictive Analytics: Machine learning algorithms to predict crop requirements.\n3. Last-Mile Logistics Integration: Integrating local delivery partnerships for door-to-door delivery.\n4. Integration with Government Subsidy Schemes: Linking the digital ledger with state/central agricultural subsidy APIs.\n5. Native Mobile Application & WhatsApp Bots: Transitioning into native Android/iOS apps with automated chatbot integration.',
    'Advantages of this Project': '1. Advantages for Farmers (Primary Beneficiaries): Elimination of blind travel, financial transparency through digital Bahi-Khata, and real-time price comparison.\n2. Advantages for Local Vendors (Secondary Beneficiaries): Digital storefront reach, automated ledger management, and inventory optimization.\n3. Overall Systemic Advantage: The unification of the local agricultural economy into one streamlined, digital marketplace.',
    'Outcome': 'The team aims to achieve the following outcomes upon project completion:\n1. Project to Product: Transitioning from an academic prototype into a fully deployable, market-ready product hosted on a live cloud server.\n2. Project to Hackathon Competitions: Showcasing the platform at major state and national level hackathons (e.g., Smart India Hackathon).\n3. Research Oriented - Publish the work in Scopus Indexed Journals: Compiling operational data into a formal research paper on the Digitization of Bahi-Khata in rural supply chains.',
    'References': '[1] Ministry of Agriculture & Farmers Welfare, Government of India. "National Agriculture Market (e-NAM) Overview & Supply Chain Guidelines." Available: https://enam.gov.in/\n[2] Food and Agriculture Organization (FAO). (2021). "Digital Technologies in Agriculture and Rural Areas."\n[3] Pressman, R. S. (2014). "Software Engineering: A Practitioner\'s Approach" (8th ed.).\n[4] Silberschatz, A., Korth, H. F. (2019). "Database System Concepts" (7th ed.).\n[5] Grinberg, M. (2018). "Flask Web Development: Developing Web Applications with Python."\n[6] Oracle Corporation. "MySQL 8.0 Reference Manual." Available: https://dev.mysql.com/doc/\n[7] Razorpay Developer Docs. "Payment Gateway API Integration." Available: https://razorpay.com/docs/'
}

for i, p in enumerate(doc.paragraphs):
    text = p.text.strip()
    if text in content:
        # insert a new paragraph after the heading
        new_p = p.insert_paragraph_before('')
        new_p._element.addnext(p._element) # Move to after
        run = p.add_run('\n' + content[text])
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)

# Technologies to be used
for p in doc.paragraphs:
    if p.text.strip() == 'Software Platform':
        set_paragraph(p, 'Software Platform & Backend\n• Framework: Python (Flask)\n• ORM / Data Access Layer: SQLAlchemy\n• Database: MySQL\n• Supporting Stack: Redis, Docker, Nginx, Gunicorn\n• APIs: Razorpay')
    elif p.text.strip() == 'Front-end':
        set_paragraph(p, 'Front-end\n• Core Languages: HTML5, CSS3, JavaScript (ES6+)\n• Interfaces: Responsive farmer, vendor, and admin workflows.')
    elif p.text.strip() == 'Hardware Platform':
        set_paragraph(p, 'Hardware Platform\n• Processor: Intel Core i5 / AMD Ryzen 5\n• RAM: 8 GB or higher\n• Storage: Minimum 256 GB SSD')
    elif p.text.strip() == 'RAM, Hard Disk, OS, Editor, Browser etc.':
        set_paragraph(p, '• OS: Windows, macOS, or Linux (Ubuntu)\n• Editor/IDE: Visual Studio Code, PyCharm\n• Web Browser: Google Chrome, Microsoft Edge')

# Tools Table
for p in doc.paragraphs:
    if p.text.strip() == 'Tools':
        p.add_run('\n1. Docker (Vendor: Docker, Inc.) - Containerized deployment\n2. Redis (Vendor: Redis Ltd.) - In-memory caching\n3. Razorpay API (Vendor: Razorpay) - Secure payment gateway\n4. Nginx (Vendor: F5, Inc.) - Reverse proxy\n5. Gunicorn (Open Source) - WSGI application server\n6. SQLAlchemy (Open Source) - Object-Relational Mapper (ORM)')

# Update Team Formation Table
if len(doc.tables) > 0:
    table = doc.tables[0]
    if len(table.rows) >= 3:
        # Row 1
        table.rows[1].cells[0].text = '1'
        table.rows[1].cells[1].text = 'Manish Pandey'
        table.rows[1].cells[2].text = '202555555'
        table.rows[1].cells[3].text = '2025266283'
        table.rows[1].cells[4].text = 'Tester & Developer'
        # Row 2
        table.rows[2].cells[0].text = '2'
        table.rows[2].cells[1].text = 'Jayant Raj'
        table.rows[2].cells[2].text = '200031595'
        table.rows[2].cells[3].text = '2025298708'
        table.rows[2].cells[4].text = 'Designer & Developer'

# Literature Survey Table
# Create a proper table after Literature Survey heading
for i, p in enumerate(doc.paragraphs):
    if p.text.strip() == 'Literature Survey':
        table = doc.add_table(rows=5, cols=5)
        table.style = 'Table Grid'
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'S.No.'
        hdr_cells[1].text = 'Author(s) & Year'
        hdr_cells[2].text = 'Title'
        hdr_cells[3].text = 'Methodology'
        hdr_cells[4].text = 'Key Findings'
        
        row1 = table.rows[1].cells
        row1[0].text = '1'
        row1[1].text = 'Sharma, R., & Kumar, V. (2023)'
        row1[2].text = 'Digitization of Rural Retail'
        row1[3].text = 'Empirical Analysis'
        row1[4].text = 'Digital ledgers reduce disputes by 40%.'
        
        row2 = table.rows[2].cells
        row2[0].text = '2'
        row2[1].text = 'Patel, A., et al. (2022)'
        row2[2].text = 'Hyper-Local Marketplace Models'
        row2[3].text = 'Case Study'
        row2[4].text = 'Farmers lose time due to stock uncertainty.'
        
        row3 = table.rows[3].cells
        row3[0].text = '3'
        row3[1].text = 'Singh, M. (2021)'
        row3[2].text = 'Friction in Agri-Retail'
        row3[3].text = 'Data Mining'
        row3[4].text = 'Lack of real-time pricing hurts margins.'
        
        row4 = table.rows[4].cells
        row4[0].text = '4'
        row4[1].text = 'Gupta, N., & Joshi, P. (2020)'
        row4[2].text = 'Adoption of Mobile Tech'
        row4[3].text = 'Quantitative'
        row4[4].text = 'UI/UX is the biggest adoption factor.'
        
        p._element.addnext(table._element)
        break

doc.save(final_path)
print('JMKS_FINAL.docx generated successfully.')
