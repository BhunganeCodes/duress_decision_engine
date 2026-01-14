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

