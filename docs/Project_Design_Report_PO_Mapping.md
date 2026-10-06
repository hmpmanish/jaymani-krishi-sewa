# 🌾 JAYMANI KRISHI SEWA: Project Design & PO Mapping Report

> **Project Design Report (PO12) | B.Tech CSE**
> **Theme:** 60% Visuals & 40% Text

---

## 🎯 1. Objectives and Methodology (PO1) - 5 Marks

**Objective:** Bridge the gap between farmers and vendors via a digital marketplace, solving stock uncertainty and manual *Bahi-Khata* issues.

```mermaid
graph TD
    A[Phase 1: Requirement Analysis] -->|Identify Farmer Needs| B[Phase 2: System Design]
    B -->|DB Schema & Architecture| C[Phase 3: Module Dev]
    C -->|Flask + React| D[Phase 4: Integration]
    D -->|Testing| E((Phase 5: Deployment))
    
    style E fill:#4ade80,stroke:#166534,stroke-width:4px
```

---

## 🛠️ 2. Identification of Necessary Tools / Formulas (PO5) - 5 Marks

**Logic Over Math:** The project utilizes CRUD operations and database joins rather than complex mathematical formulas.

| Category | Technology Used | Icon/Symbol |
| :--- | :--- | :---: |
| **Frontend** | React, Tailwind CSS, Vite | ⚛️ 🎨 |
| **Backend** | Python, Flask, Flask-CORS | 🐍 🌐 |
| **Database** | SQLite (Relational DB) | 🗄️ |
| **Tools** | Git, GitHub, VS Code | 🐙 💻 |

---

## 🧩 3. Identification of the Modules (PO2) - 5 Marks

```mermaid
mindmap
  root((JAYMANI KRISHI SEWA))
    User Authentication
      Admin
      Farmer
      Vendor
    Hyper-Local Discovery
      Search Products
      Check Availability
    Inventory Management
      Add Stock
      Update Prices
    Digital Credit System
      Place Order
      Track Bahi-Khata
```

---

## 🏗️ 4. Working with High-Level Design (PO3) - 5 Marks

**Client-Server Architecture:** Separation of concerns between UI, Business Logic, and Data Storage.

```mermaid
graph LR
    subgraph Client Tier
    A[React/Tailwind UI]
    end
    
    subgraph Application Tier
    B(Flask REST API)
    end
    
    subgraph Data Tier
    C[(SQLite Database)]
    end
    
    A <-->|HTTP / JSON| B
    B <-->|SQL Queries| C
    
    style A fill:#60a5fa,color:#fff
    style B fill:#f472b6,color:#fff
    style C fill:#fbbf24,color:#fff
```

---

## ⚙️ 5. Working with Low-Level Design (PO4) - 5 Marks

**Module-wise Component Interaction:** (Example: Discovery & Order Module)

```mermaid
sequenceDiagram
    actor Farmer
    participant React UI
    participant Flask API
    participant SQLite
    
    Farmer->>React UI: Clicks 'View Products'
    React UI->>Flask API: GET /api/products
    Flask API->>SQLite: SELECT * FROM products JOIN users
    SQLite-->>Flask API: Return Rows
    Flask API-->>React UI: JSON Data
    React UI-->>Farmer: Displays Inventory
    
    Farmer->>React UI: Clicks 'Buy Now'
    React UI->>Flask API: POST /api/orders (farmer_id, vendor_id, total)
    Flask API->>SQLite: INSERT INTO orders
    SQLite-->>Flask API: Success (lastrowid)
    Flask API-->>React UI: Order Confirmation JSON
```

---

## 🗣️ 6. Communication & Presentation (PO10) - 5 Marks

*   **Target Audience:** Farmers (end-users), Vendors (suppliers), and Academic Evaluators.
*   **Mode of Communication:** Simple, intuitive UI (React) and professional Viva PPTX.

```mermaid
pie title "Presentation & Communication Breakdown"
    "Visual Diagrams (Architecture, Flow)" : 60
    "Concise Text (Bullet Points)" : 30
    "Live Demo / Verbal" : 10
```

---
*Generated mapping perfectly aligns with the Program Outcomes (PO) mapping syllabus.*
