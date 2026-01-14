# Silent Duress ATM Safety Protocol (Prototype)

**Author:** Thamsanqa Hadebe  
**Role:** Founder / Software Developer  
**Project Type:** Fintech Security Prototype  
**Status:** MVP / Proof of Concept  

---

## 📌 Overview

The **Silent Duress ATM Safety Protocol** is a software-first fintech security prototype designed to reduce ATM-related crime by enabling customers to silently signal distress during forced withdrawals.

The system introduces a **dual-PIN mechanism**, where a secondary (duress) PIN triggers an invisible safety protocol without alerting attackers. The solution is intentionally designed to integrate with existing banking and ATM infrastructure **without requiring hardware replacement**.

This repository contains a **simulation-based prototype** intended to demonstrate feasibility, logic, and system integration — not a production banking system.

---

## 🎯 Problem Statement

ATM crime often involves coercion, where customers are forced to withdraw money under threat. Current ATM systems cannot distinguish between voluntary and forced transactions, leaving customers vulnerable and banks exposed to repeated losses.

There is a critical gap at the **point of transaction**:
- No discreet way for users to signal danger  
- No real-time differentiation between safe and coerced withdrawals  
- Responses are reactive rather than preventative  

---

## 💡 Proposed Solution

This prototype models a **Silent Duress Response Engine** that sits within the fraud/risk layer of a bank’s transaction flow.

### Core Concept
- **Primary PIN** → normal withdrawal  
- **Duress PIN** → silent safety protocol  

The ATM interface remains unchanged, while backend systems respond intelligently.

---

## 🧱 System Architecture (Conceptual)

ATM Simulator (Frontend)
↓
Transaction Switch API
↓
Duress / Risk Decision Engine
↓
Core Banking Simulator
↓
Transaction Response


> ⚠️ Note: All systems are simulated. No real banking infrastructure is accessed.

---

## 🧩 Components

### 1. ATM Simulator
- Mimics user interaction with an ATM
- Captures PIN, withdrawal amount, location, and time
- Sends transaction requests to the Transaction Switch

### 2. Transaction Switch (API Layer)
- Acts as a routing and validation layer
- Forwards transactions to the Duress Engine
- Represents real-world ATM switch behavior conceptually

### 3. Duress / Risk Decision Engine (Core Innovation)
- Evaluates whether a transaction is normal or coerced
- Applies duress logic and configurable rules
- Determines response behavior (e.g. limited cash, alerts)

### 4. Core Banking Simulator
- Mock account balances
- Simulated approvals and declines
- Ledger updates for demo purposes

### 5. Admin Dashboard (Optional / Phase 2)
- View flagged duress events
- Monitor outcomes and system behavior
- Demonstrate auditability and oversight

---

## ⚙️ Technology Stack (Proposed)

**Backend**
- Python
- FastAPI
- PostgreSQL / SQLite (for simulation)

**Frontend**
- React (ATM simulator & dashboard)

**Other**
- REST APIs
- JSON-based transaction payloads

---

## 📦 Example Transaction Payload

```json
{
  "card_id": "CARD-001",
  "pin": "4321",
  "amount": 1000,
  "atm_id": "ATM-JHB-09",
  "location": "Johannesburg",
  "timestamp": "2026-01-14T21:32:00"
}