# API Requirements – Inventory Management System

## Domain
E-commerce and Warehouse Inventory Management.

## Target Users
- Inventory Managers
- Data Analysts
- Developers

## Core Operations
1. Create Product
2. Update Product
3. Delete Product
4. Get Product by ID
5. List All Products
6. Search Products
7. Update Stock Level
8. Get Low Stock Alerts
9. Batch Upload
10. Category List

## Data Validation Rules
- SKU must be unique.
- Price must be > 0.

## Non-Functional Requirements
- Auth: JWT required.
- Response time < 200ms.
