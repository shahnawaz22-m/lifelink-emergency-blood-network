# 🩸 LifeLink – Emergency Blood Network

A serverless cloud-based web application that connects blood donors with hospitals in real time during emergencies.

---

## 📌 Project Overview

LifeLink is a cloud-native blood donor management system built using AWS services.  
It allows:

- Donors to register their blood group and contact details
- Hospitals to search for available donors instantly
- Direct WhatsApp contact with matching donors
- Real-time donor count display

The entire system is built using a serverless architecture.

---

## 🏗️ Architecture

Frontend:
- Hosted on Amazon S3 (Static Website Hosting)
- HTML, CSS, JavaScript

Backend:
- AWS Lambda (Python)
- Amazon API Gateway
- Amazon S3 (Data Storage)

---

## ⚙️ Features

### 1️⃣ Donor Registration
- Name
- Blood Group
- Phone Number
- City
- Stored in S3 as JSON
- Unique Donor ID generated

### 2️⃣ Emergency Search
- Search by Blood Group
- Shows:
  - Total Donors Found
  - Name
  - Blood Group
  - Location
  - WhatsApp Contact Button

### 3️⃣ WhatsApp Integration
- One-click contact
- Opens WhatsApp directly with donor number

### 4️⃣ Real-time Donor Count
- Displays total matching donors

---

## 🧠 Technologies Used

- HTML5
- CSS3
- JavaScript (Fetch API)
- Python (AWS Lambda)
- AWS S3
- AWS API Gateway
- JSON

---

## ☁️ AWS Services Used

| Service        | Purpose |
|---------------|----------|
| Amazon S3     | Static Hosting + Data Storage |
| AWS Lambda    | Backend Logic |
| API Gateway   | API Endpoints |
| IAM           | Permissions |

---

## 🔄 Data Storage Format

All donors are stored in:

