---
title: "Jaymani Krishi Sewa - Project Proposal Report"
author: "Manish Pandey & Jayant Raj"
date: "2026-09-15"
geometry: "a4paper, margin=1in"
colorlinks: true
---

<div align="center" style="margin-top: 50px; padding: 40px; background: linear-gradient(to right, #0f2027, #203a43, #2c5364); color: white; border-radius: 15px; box-shadow: 0px 10px 20px rgba(0,0,0,0.2);">
  <h1 style="font-size: 3.5em; margin-bottom: 5px; color: #4ade80; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">🌾 JAYMANI KRISHI SEWA 🌾</h1>
  <h2 style="font-size: 1.8em; font-weight: 300; margin-top: 0; color: #f8fafc;">Digital Agritech Marketplace for Farmers & Local Vendors</h2>
  
  <br><br>
  <div style="background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; display: inline-block;">
    <h3 style="font-size: 1.6em; margin: 0; color: #fbbf24;">Project Proposal Report</h3>
    <p style="font-size: 1.2em; margin-top: 10px;">Submitted in partial fulfillment of the requirements for:</p>
    <h3 style="font-size: 1.5em; color: #38bdf8; margin: 5px 0;"><strong>CSCR2600 — Project Based Learning</strong></h3>
  </div>
  <br><br><br>
  
  <h2 style="font-size: 2em; color: #f8fafc;"><strong>Sharda University</strong></h2>
  <h3 style="font-size: 1.3em; font-weight: 300;">School of Computer Science & Engineering</h3>
</div>

<br><br>

<div style="display: flex; justify-content: space-around; background-color: #f1f5f9; padding: 30px; border-radius: 15px; border-left: 5px solid #2563eb;">
  <div>
    <h4 style="font-size: 1.3em; color: #1e293b; margin-bottom: 5px;">👨‍🎓 Submitted By:</h4>
    <p style="font-size: 1.2em; font-weight: bold; color: #3b82f6; margin: 2px;">Manish Pandey</p>
    <p style="font-size: 1.2em; font-weight: bold; color: #3b82f6; margin: 2px;">Jayant Raj</p>
  </div>
  <div style="text-align: right;">
    <h4 style="font-size: 1.3em; color: #1e293b; margin-bottom: 5px;">👨‍🏫 Under the Guidance of:</h4>
    <p style="font-size: 1.2em; font-weight: bold; color: #10b981; margin: 2px;">Prof. (Dr.) Ali Imam Abidi</p>
  </div>
</div>

<div style="page-break-after: always;"></div>

---

<div style="background-color: #f8fafc; padding: 30px; border-radius: 10px; border: 1px solid #e2e8f0;">
  <h2 align="center" style="color: #0f172a;">📜 CERTIFICATE</h2>
  <br>
  <p style="font-size: 1.1em; line-height: 1.6; text-align: justify;">
    This is to certify that the Project Proposal Report titled <strong>"JAYMANI KRISHI SEWA: Digital Agritech Marketplace for Farmers & Local Vendors"</strong> submitted by <strong>Manish Pandey</strong> and <strong>Jayant Raj</strong> in partial fulfillment of the requirements for the course <strong>CSCR2600 — Project Based Learning</strong> at <strong>Sharda University, School of Computer Science & Engineering</strong>, is a bona fide record of the work proposed and carried out under my guidance and supervision.
  </p>
  <br><br><br>
  <div style="display: flex; justify-content: space-between;">
    <div>
      <p>___________________________</p>
      <p style="margin: 5px 0;"><strong>Prof. (Dr.) Ali Imam Abidi</strong></p>
      <p style="color: #64748b; margin: 0;">Faculty Mentor</p>
    </div>
    <div>
      <p>___________________________</p>
      <p style="margin: 5px 0;"><strong>Head of Department</strong></p>
      <p style="color: #64748b; margin: 0;">School of Computer Science & Engineering</p>
    </div>
  </div>
</div>

<div style="page-break-after: always;"></div>

---

## 🚀 5. EXECUTIVE ABSTRACT

<div style="background-color: #eff6ff; padding: 25px; border-radius: 10px; border-left: 6px solid #3b82f6; font-size: 1.15em; line-height: 1.6;">
Farmers frequently face significant challenges in the local agricultural supply chain, primarily dealing with local price fluctuations, stock uncertainty, and the limitations of traditional, paper-based <em>Bahi-Khata</em> (credit ledgers). These inefficiencies lead to wasted time, increased fuel costs, and potential crop losses. 
<br><br>
This report proposes <strong>Jaymani Krishi Sewa</strong>, a digital agritech marketplace designed to bridge the gap between farmers and verified local vendors. The platform acts as a hyper-local ecosystem providing real-time inventory visibility, localized product discovery, and transparent purchasing mechanisms. 
<br><br>
Furthermore, it integrates a digital <em>Bahi-Khata</em> system, replacing manual credit records with accurate digital ledgers, automated invoices, and seamless payment options.
</div>

**Keywords:** `Agritech` `Digital Marketplace` `Farmers` `Local Retailers` `Inventory Management` `Bahi-Khata`

---

## 🎯 7. PROBLEM STATEMENT (PO1)

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin: 20px 0;">
  
  <div style="background-color: #fef2f2; border: 1px solid #fca5a5; padding: 20px; border-radius: 10px; width: 45%;">
    <h3 style="color: #dc2626; margin-top: 0;">📉 7.1 Price & Stock Uncertainty</h3>
    <p>Farmers travel to multiple shops without knowing the availability of specific products or local prices, leading to a trial-and-error approach.</p>
  </div>

  <div style="background-color: #fff7ed; border: 1px solid #fdba74; padding: 20px; border-radius: 10px; width: 45%;">
    <h3 style="color: #ea580c; margin-top: 0;">📒 7.2 Paper Bahi-Khata</h3>
    <p>Local credit transactions are primarily recorded in manual ledgers. These are difficult to track, prone to miscalculation, and easily lost.</p>
  </div>

  <div style="background-color: #f5f3ff; border: 1px solid #c4b5fd; padding: 20px; border-radius: 10px; width: 45%;">
    <h3 style="color: #7c3aed; margin-top: 0;">⏳ 7.3 Time & Fuel Loss</h3>
    <p>Inefficient access to agricultural inputs wastes valuable time (especially during sowing seasons) and increases fuel expenses.</p>
  </div>

  <div style="background-color: #f0fdf4; border: 1px solid #86efac; padding: 20px; border-radius: 10px; width: 45%;">
    <h3 style="color: #16a34a; margin-top: 0;">🏬 7.4 Vendor Limitations</h3>
    <p>Retailers lack affordable digital tools to manage inventory, update prices dynamically, and maintain organized customer credit histories.</p>
  </div>

</div>

<div style="background-color: #1e293b; color: white; padding: 20px; border-radius: 10px; text-align: center;">
  <h3 style="color: #fbbf24; margin-top: 0;">💡 The Core Problem</h3>
  <p style="font-size: 1.2em; margin-bottom: 0;">There is a pressing need for a simple hyper-local platform connecting farmers with verified local agricultural retailers while combining product discovery, inventory visibility, purchasing, and digital credit records.</p>
</div>

---

## 🔍 8. PROBLEM ANALYSIS (5W1H)

| Dimension | Analysis |
| :--- | :--- |
| 🧑 **WHO?** | Small-scale farmers and local agricultural retailers. |
| ❓ **WHAT?** | Information gap in agricultural product supply, pricing, and credit records. |
| 📍 **WHERE?** | Rural and local agricultural markets. |
| ⏰ **WHEN?** | Especially during critical agricultural and sowing seasons. |
| 🎯 **WHY?** | To reduce unnecessary travel, financial uncertainty, and potential crop-related losses. |
| 🛠️ **HOW?** | Current practices depend heavily on phone calls, word-of-mouth, and manual paper records. |

---

## 🌟 10. PROPOSED PROJECT CONCEPT (PO4)

**Jaymani Krishi Sewa** is conceptualized as a **Hyper-Local Digital Agritech Marketplace**. 

<div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">
```mermaid
graph LR
    F[👨‍🌾 FARMER] <-->|Browse, Order, Pay| JKS((🌱 JAYMANI KRISHI SEWA))
    JKS <-->|Manage Inventory, Fulfill, Ledger| V[🏬 VERIFIED LOCAL VENDOR]
    
    style F fill:#4ade80,stroke:#16a34a,stroke-width:2px,color:black
    style JKS fill:#3b82f6,stroke:#1d4ed8,stroke-width:4px,color:white
    style V fill:#facc15,stroke:#ca8a04,stroke-width:2px,color:black
```
</div>

### System Actors:

1. **👨‍🌾 FARMER:** Browse products, compare prices, place orders, view invoices, and manage digital credit.
2. **🏬 VERIFIED VENDOR:** Manage catalog, update stock/prices dynamically, manage orders, and maintain the customer credit ledger.
3. **💻 PLATFORM:** Hosts the localized Marketplace, facilitates Order routing, tracks Inventory, and manages the Digital Bahi-Khata.

---

## 🔄 11. PROPOSED SYSTEM WORKFLOW

```mermaid
graph TD
    A([🔐 Registration / Login]) --> B{👤 Role Selection}
    B -->|Farmer| C[🛒 Browse / Compare Catalog]
    B -->|Vendor| C2[📦 Manage Catalog & Stock]
    C --> D[🛍️ Cart & Checkout]
    D --> E{💳 Payment / Credit?}
    E -->|Pay Now| F1[📲 Razorpay Gateway]
    E -->|Credit| F2[📒 Digital Bahi-Khata Entry]
    F1 --> G([🧾 Invoice Generation])
    F2 --> G
    
    style A fill:#e2e8f0,stroke:#64748b
    style B fill:#fde047,stroke:#a16207
    style C fill:#bbf7d0,stroke:#15803d
    style D fill:#bfdbfe,stroke:#1d4ed8
    style E fill:#fbcfe8,stroke:#be185d
    style G fill:#ddd6fe,stroke:#6d28d9
```

---

## 📚 14. RESEARCH GAP (PO5)

While platforms like *eNAM* focus on wholesale, *Digital Green* focuses on advisory, and *Khatabook* focuses on generic ledgers, **none provide an integrated hyper-local workflow bridging commerce and credit.**

```mermaid
graph TD
    subgraph EXISTING SOLUTIONS
        S1[eNAM: Wholesale]
        S2[Digital Green: Advisory]
        S3[Khatabook: Generic Ledger]
    end
    
    S1 --> GAP
    S2 --> GAP
    S3 --> GAP
    
    GAP((IDENTIFIED GAP)) -->|Lack of Integrated Workflow| JKS{🌟 Jaymani Krishi Sewa}
    
    style GAP fill:#fecaca,stroke:#b91c1c,stroke-width:2px,color:black
    style JKS fill:#bbf7d0,stroke:#15803d,stroke-width:3px,color:black
```

---

## ⚙️ 16. TECHNOLOGY STACK

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
  <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-left: 5px solid #e34c26;">
    <strong>🎨 Frontend:</strong> HTML5, CSS3, JS (Responsive UI)
  </div>
  <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-left: 5px solid #3776ab;">
    <strong>🧠 Backend:</strong> Python Flask
  </div>
  <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-left: 5px solid #00758f;">
    <strong>🗄️ Database:</strong> MySQL & SQLAlchemy ORM
  </div>
  <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-left: 5px solid #dc382d;">
    <strong>⚡ Caching:</strong> Redis
  </div>
  <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-left: 5px solid #0b65c2;">
    <strong>💳 Payments:</strong> Razorpay Integration
  </div>
  <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-left: 5px solid #2496ed;">
    <strong>🐳 Deployment:</strong> Docker & Nginx
  </div>
</div>

---

## 🏗️ 17. SYSTEM ARCHITECTURE

```mermaid
graph TD
    subgraph USER LAYER
        F[Farmer]
        V[Vendor]
    end
    subgraph APPLICATION LAYER
        M[Marketplace Module]
        O[Orders Module]
        I[Inventory Module]
        B[Bahi-Khata Module]
    end
    subgraph BACKEND & DB
        PF((Python Flask Engine))
        SQLA[SQLAlchemy]
        MySQL[(MySQL)]
    end
    
    F --> M
    F --> B
    V --> I
    V --> O
    
    M --> PF
    O --> PF
    I --> PF
    B --> PF
    
    PF --> SQLA --> MySQL
```

---

## 📅 20. PROJECT ROADMAP (PO11)

<div style="background-color: #f8fafc; padding: 20px; border-radius: 10px; border: 1px solid #cbd5e1;">
  <p><strong>Phase 1-2:</strong> Problem Identification & Requirement Analysis <em>(Weeks 1-4)</em></p>
  <div style="background: #3b82f6; height: 10px; border-radius: 5px; width: 25%; margin-bottom: 10px;"></div>
  
  <p><strong>Phase 3-4:</strong> UI/UX Design & Database/Backend Dev <em>(Weeks 5-8)</em></p>
  <div style="background: #10b981; height: 10px; border-radius: 5px; width: 50%; margin-bottom: 10px;"></div>
  
  <p><strong>Phase 5-6:</strong> Frontend & Payment/Bahi-Khata Integration <em>(Weeks 9-12)</em></p>
  <div style="background: #f59e0b; height: 10px; border-radius: 5px; width: 75%; margin-bottom: 10px;"></div>
  
  <p><strong>Phase 7-8:</strong> Testing, Security, Deployment & Presentation <em>(Weeks 13-14)</em></p>
  <div style="background: #ef4444; height: 10px; border-radius: 5px; width: 100%; margin-bottom: 10px;"></div>
</div>

---

## 👥 21. DISTRIBUTION OF WORK (PO11)

| Team Member | Primary Responsibilities | Supporting Responsibilities |
| :--- | :--- | :--- |
| 🧑‍💻 **Manish Pandey** | Project Research, Requirements Gathering, Documentation, Report Gen. | System Architecture Planning, QA Testing, Presentation |
| 🎨 **Jayant Raj** | UI/UX Design, Frontend Dev, Core Application/Backend Logic. | Database/API Integration, Docker Deployment |

---

## 🌍 25. EXPECTED IMPACT

```mermaid
graph LR
    A[📱 Information Access] -->|Enables| B[💡 Better Purchase Decisions]
    B -->|Requires| C[🔎 Inventory Visibility]
    C -->|Facilitates| D[💳 Digital Transactions]
    D -->|Results In| E[📒 Transparent Credit Management]
    
    style E fill:#ecfdf5,stroke:#059669,stroke-width:3px,color:black
```

---

## ✅ 26. CONCLUSION

**Jaymani Krishi Sewa** addresses grassroots agricultural challenges by providing a dedicated, hyper-local digital layer. By seamlessly connecting local demand, supply, inventory tracking, purchasing, payments, and credit records (Digital *Bahi-Khata*), the project demonstrates high feasibility and significant potential for positive operational impact. 

<div style="text-align: center; margin-top: 50px; font-size: 1.2em; color: #64748b;">
  <em>"Modernizing traditional trust-based economics for a more efficient agricultural ecosystem."</em>
</div>
