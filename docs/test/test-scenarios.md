# Personal Finance Tracker — Test Scenario Catalogue

## Version

**Version:** 1.0  
**Scope:** MVP  
**Total High-Level Test Scenarios:** 85

---

## Purpose

This document defines the high-level test scenarios for the Personal Finance Tracker application.

The scenarios cover:

- Functional testing
- Validation testing
- Authentication and authorisation
- Security testing
- Data integrity
- Multi-currency functionality
- Data import and export
- Financial analytics
- Accessibility
- Responsive behaviour
- Browser compatibility
- Performance
- Reliability

Detailed test cases, test data, expected results and execution results will be maintained separately.

---

## Scenario ID Convention

Each scenario has a unique identifier using the format:

`TS-XXX`

Existing scenario IDs shall not be renumbered. New scenarios shall use the next available identifier.

---

# 1. Authentication

## TS-001 — User Registration

**Module:** Authentication  
**Priority:** High  
**Type:** Functional  
**Requirement:** FR-001

**Scenario:**  
Verify that a new user can create an account using a valid name, email address, password and password confirmation.

---

## TS-002 — Registration Validation

**Module:** Authentication  
**Priority:** High  
**Type:** Functional / Validation  
**Requirement:** FR-002 to FR-009

**Scenario:**  
Verify that registration fields are mandatory and that name, email and password validation rules are correctly enforced.

---

## TS-003 — Duplicate Email Registration

**Module:** Authentication  
**Priority:** High  
**Type:** Functional / Security  
**Requirement:** FR-014 to FR-016

**Scenario:**  
Verify that the system prevents multiple accounts from being registered using the same email address and does not unnecessarily expose account information.

---

## TS-004 — User Login

**Module:** Authentication  
**Priority:** High  
**Type:** Functional  
**Requirement:** FR-023 to FR-027

**Scenario:**  
Verify that a verified user can successfully log in using valid email and password credentials.

---

## TS-005 — Invalid Login

**Module:** Authentication  
**Priority:** High  
**Type:** Negative / Security  
**Requirement:** FR-024 to FR-025

**Scenario:**  
Verify that the system rejects invalid authentication attempts and provides appropriate feedback without unnecessarily revealing account information.

---

## TS-006 — Protected Resource Access

**Module:** Authentication / Authorisation  
**Priority:** Critical  
**Type:** Security  
**Requirement:** FR-028 to FR-030

**Scenario:**  
Verify that unauthenticated users cannot access protected application pages, APIs or financial information.

---

## TS-007 — User Logout

**Module:** Authentication / Session Management  
**Priority:** High  
**Type:** Functional / Security  
**Requirement:** FR-031 to FR-034

**Scenario:**  
Verify that an authenticated user can log out and cannot subsequently access protected resources without authenticating again.

---

## TS-008 — Password Management

**Module:** Authentication  
**Priority:** High  
**Type:** Functional / Security  
**Requirement:** FR-035 to FR-046

**Scenario:**  
Verify that users can securely change or reset their password and that password validation and protection requirements are enforced.

---

# 2. Dashboard

## TS-009 — Dashboard Access

**Module:** Dashboard  
**Priority:** High  
**Type:** Functional  
**Requirement:** FR-047, FR-054

**Scenario:**  
Verify that an authenticated user can access the dashboard and view their authorised financial information.

---

## TS-010 — Income Summary

**Module:** Dashboard  
**Priority:** High  
**Type:** Functional / Calculation  
**Requirement:** FR-048, FR-055

**Scenario:**  
Verify that the dashboard correctly displays the user's total income for the selected period.

---

## TS-011 — Expense Summary

**Module:** Dashboard  
**Priority:** High  
**Type:** Functional / Calculation  
**Requirement:** FR-049, FR-055

**Scenario:**  
Verify that the dashboard correctly displays the user's total expenses for the selected period.

---

## TS-012 — Balance Calculation

**Module:** Dashboard  
**Priority:** Critical  
**Type:** Functional / Calculation  
**Requirement:** FR-050, FR-054 to FR-055

**Scenario:**  
Verify that the dashboard calculates the user's financial balance correctly from authorised income and expense transactions.

---

## TS-013 — Recent Transactions

**Module:** Dashboard  
**Priority:** Medium  
**Type:** Functional  
**Requirement:** FR-051

**Scenario:**  
Verify that the dashboard displays the user's recent transactions correctly.

---

## TS-014 — Dashboard Period Selection

**Module:** Dashboard  
**Priority:** High  
**Type:** Functional / Boundary  
**Requirement:** FR-052, FR-096

**Scenario:**  
Verify that changing the dashboard financial period displays the correct financial information for the selected period.

---

# 3. Transactions

## TS-015 — Create Income Transaction

**Module:** Transactions  
**Priority:** Critical  
**Type:** Functional  
**Requirement:** FR-056 to FR-058

**Scenario:**  
Verify that an authenticated user can successfully create a valid income transaction.

---

## TS-016 — Create Expense Transaction

**Module:** Transactions  
**Priority:** Critical  
**Type:** Functional  
**Requirement:** FR-057 to FR-058

**Scenario:**  
Verify that an authenticated user can successfully create a valid expense transaction.

---

## TS-017 — Transaction Validation

**Module:** Transactions  
**Priority:** Critical  
**Type:** Validation  
**Requirement:** FR-060 to FR-061, FR-077 to FR-078

**Scenario:**  
Verify that invalid transaction amounts, dates, categories, currencies and other mandatory transaction information are rejected.

---

## TS-018 — Transaction Confirmation

**Module:** Transactions  
**Priority:** Medium  
**Type:** Functional / Usability  
**Requirement:** FR-062

**Scenario:**  
Verify that the user receives appropriate confirmation after successfully creating a transaction.

---

## TS-019 — Transaction History

**Module:** Transactions  
**Priority:** High  
**Type:** Functional  
**Requirement:** FR-063

**Scenario:**  
Verify that saved transactions are correctly displayed in the user's transaction history.

---

## TS-020 — Edit Transaction

**Module:** Transactions  
**Priority:** High  
**Type:** Functional / Data Integrity  
**Requirement:** FR-064, FR-069, FR-080

**Scenario:**  
Verify that an authenticated user can edit their own transaction and that the updated information is correctly persisted.

---

## TS-021 — Delete Transaction

**Module:** Transactions  
**Priority:** High  
**Type:** Functional / Data Integrity  
**Requirement:** FR-065 to FR-066, FR-080

**Scenario:**  
Verify that an authenticated user can delete their own transaction and that appropriate deletion confirmation is provided.

---

## TS-022 — Transaction Search

**Module:** Transactions  
**Priority:** Medium  
**Type:** Functional  
**Requirement:** FR-067

**Scenario:**  
Verify that users can search their transaction history and receive accurate matching results.

---

## TS-023 — Transaction Filtering

**Module:** Transactions  
**Priority:** Medium  
**Type:** Functional  
**Requirement:** FR-068

**Scenario:**  
Verify that users can filter transactions using the supported transaction filtering criteria.

---

## TS-024 — Transaction Authorisation

**Module:** Transactions / Security  
**Priority:** Critical  
**Type:** Security / Authorisation  
**Requirement:** FR-069, NFR-009

**Scenario:**  
Verify that a user cannot view, edit or delete transactions belonging to another user.

---

# 4. Categories

## TS-025 — Display Categories

**Module:** Categories  
**Priority:** Medium  
**Type:** Functional  
**Requirement:** FR-081

**Scenario:**  
Verify that the system displays the predefined income and expense categories correctly.

---

## TS-026 — Assign Transaction Category

**Module:** Categories / Transactions  
**Priority:** High  
**Type:** Functional  
**Requirement:** FR-082

**Scenario:**  
Verify that a user can assign an appropriate category to a transaction.

---

## TS-027 — Missing Category Validation

**Module:** Categories / Transactions  
**Priority:** High  
**Type:** Validation  
**Requirement:** FR-083

**Scenario:**  
Verify that a transaction cannot be saved when a mandatory category is missing.

---

# 5. Financial Analytics

## TS-028 — Income and Expense Calculation

**Module:** Analytics  
**Priority:** Critical  
**Type:** Functional / Calculation  
**Requirement:** FR-087

**Scenario:**  
Verify that total income and expenses are calculated accurately for the selected period.

---

## TS-029 — Category Spending Analysis

**Module:** Analytics  
**Priority:** High  
**Type:** Functional / Calculation  
**Requirement:** FR-088

**Scenario:**  
Verify that spending is correctly analysed and grouped by category.

---

## TS-030 — Income vs Expenses

**Module:** Analytics  
**Priority:** High  
**Type:** Functional / Calculation  
**Requirement:** FR-089

**Scenario:**  
Verify that the system correctly compares income and expenses for the selected period.

---

## TS-031 — Spending Trends

**Module:** Analytics  
**Priority:** High  
**Type:** Functional / Calculation  
**Requirement:** FR-090

**Scenario:**  
Verify that spending trends are correctly calculated and displayed over time.

---

## TS-032 — Analytics Period Selection

**Module:** Analytics  
**Priority:** High  
**Type:** Functional / Boundary  
**Requirement:** FR-091, FR-096

**Scenario:**  
Verify that analytics correctly update when the user changes the analysis period.

---

## TS-033 — Analytics Data Authorisation

**Module:** Analytics / Security  
**Priority:** Critical  
**Type:** Security / Authorisation  
**Requirement:** FR-092, NFR-009

**Scenario:**  
Verify that analytics only use transaction data belonging to the authenticated user.

---

# 6. Data Management

## TS-034 — Transaction Data Persistence

**Module:** Data Management  
**Priority:** Critical  
**Type:** Data Integrity  
**Requirement:** FR-098, FR-080, NFR-025

**Scenario:**  
Verify that transaction data is correctly persisted and remains accurate after creation, modification and retrieval.

---

## TS-035 — Financial Data Export

**Module:** Data Management  
**Priority:** High  
**Type:** Functional / Data Integrity  
**Requirement:** FR-099 to FR-103

**Scenario:**  
Verify that an authorised user can export their financial data and that the exported information accurately represents their stored transactions.

---

## TS-036 — Supported File Import

**Module:** Data Management  
**Priority:** High  
**Type:** Functional  
**Requirement:** FR-104 to FR-106

**Scenario:**  
Verify that the system accepts valid financial data imports using supported `.docx`, `.txt` and `.csv` files.

---

## TS-037 — Unsupported/Invalid File Import

**Module:** Data Management  
**Priority:** Critical  
**Type:** Negative / Validation / Security  
**Requirement:** FR-107 to FR-114

**Scenario:**  
Verify that the system rejects unsupported file formats, corrupted files and files containing invalid or incomplete financial data, including PDF and image files.

---

## TS-038 — Import/Export Feedback

**Module:** Data Management  
**Priority:** Medium  
**Type:** Functional / Usability  
**Requirement:** FR-118 to FR-121

**Scenario:**  
Verify that users receive appropriate feedback for successful and unsuccessful import and export operations.

---

# 7. User Settings

## TS-039 — Account Settings

**Module:** User Settings  
**Priority:** Medium  
**Type:** Functional  
**Requirement:** FR-122

**Scenario:**  
Verify that users can view and manage their supported account settings.

---

## TS-040 — Default Currency

**Module:** User Settings / Currency  
**Priority:** High  
**Type:** Functional  
**Requirement:** FR-123 to FR-124

**Scenario:**  
Verify that a user can select a default display currency after registration and authentication and that currency selection is not required during registration.

---

## TS-041 — Currency Application

**Module:** Currency / User Settings  
**Priority:** Critical  
**Type:** Functional / Calculation  
**Requirement:** FR-125, FR-130 to FR-133

**Scenario:**  
Verify that the selected default display currency is correctly applied to relevant financial information and analytics.

---

## TS-042 — User Preferences

**Module:** User Settings  
**Priority:** Medium  
**Type:** Functional  
**Requirement:** FR-127

**Scenario:**  
Verify that supported user preferences can be viewed, updated and persisted correctly.

---

# 8. Cross-Cutting Quality

## TS-043 — User Data Isolation

**Module:** Security / Data  
**Priority:** Critical  
**Type:** Security / Authorisation  
**Requirement:** FR-030, FR-069, NFR-005, NFR-009

**Scenario:**  
Verify that a user can only access, create, modify, delete, import and export their own financial information.

---

## TS-044 — Responsive Application

**Module:** Cross-Cutting  
**Priority:** High  
**Type:** Non-Functional / UI  
**Requirement:** NFR-036 to NFR-037

**Scenario:**  
Verify that the application remains usable and that core functionality is accessible across supported desktop, tablet and mobile screen sizes.

---

## TS-045 — Browser Compatibility

**Module:** Cross-Cutting  
**Priority:** High  
**Type:** Compatibility  
**Requirement:** NFR-035

**Scenario:**  
Verify that the application works correctly across supported modern web browsers.

---

## TS-046 — Accessibility

**Module:** Cross-Cutting  
**Priority:** High  
**Type:** Accessibility  
**Requirement:** NFR-031 to NFR-034

**Scenario:**  
Verify that core application functionality is accessible using supported accessibility mechanisms and assistive technologies.

---

## TS-047 — Error Handling

**Module:** Cross-Cutting  
**Priority:** High  
**Type:** Negative / Reliability  
**Requirement:** NFR-022, NFR-027, NFR-056

**Scenario:**  
Verify that application and validation errors are handled appropriately without exposing sensitive technical information.

---

## TS-048 — Performance

**Module:** Cross-Cutting  
**Priority:** High  
**Type:** Performance  
**Requirement:** NFR-001 to NFR-004, NFR-052

**Scenario:**  
Verify that common application operations remain within acceptable performance levels under normal and increased data volumes.

---

## TS-049 — Security

**Module:** Cross-Cutting  
**Priority:** Critical  
**Type:** Security  
**Requirement:** NFR-005 to NFR-015

**Scenario:**  
Verify that the application protects authentication credentials, financial information, APIs, sessions and user-provided data against common security threats.

---

## TS-050 — Data Integrity

**Module:** Cross-Cutting  
**Priority:** Critical  
**Type:** Data Integrity / Reliability  
**Requirement:** NFR-022 to NFR-025, FR-080

**Scenario:**  
Verify that financial data remains accurate, consistent and complete during normal operations and application/database failures.

---

# 9. Additional Authentication Scenarios

## TS-051 — Email Verification

**Module:** Authentication  
**Priority:** Critical  
**Type:** Functional / Security  
**Requirement:** FR-017 to FR-018

**Scenario:**  
Verify that a newly registered user must successfully verify their email address before accessing protected application functionality.

---

## TS-052 — Email Verification Failure/Expiry

**Module:** Authentication  
**Priority:** High  
**Type:** Negative / Security  
**Requirement:** FR-019 to FR-022

**Scenario:**  
Verify that invalid, expired or already-used verification mechanisms are rejected and that users can request verification again where supported.

---

## TS-053 — Disposable Email Prevention

**Module:** Authentication  
**Priority:** High  
**Type:** Validation / Security  
**Requirement:** FR-015

**Scenario:**  
Verify that known disposable or temporary email addresses cannot be used to register an account.

---

## TS-054 — Session Expiration

**Module:** Authentication / Session Management  
**Priority:** Critical  
**Type:** Security  
**Requirement:** FR-033 to FR-034, NFR-014

**Scenario:**  
Verify that an expired or invalid authentication session cannot be used to access protected application functionality or financial information.

---

# 10. Additional Dashboard Scenarios

## TS-055 — Dashboard Multi-Currency Display

**Module:** Dashboard / Currency  
**Priority:** Critical  
**Type:** Functional / Calculation  
**Requirement:** FR-055, FR-128 to FR-133

**Scenario:**  
Verify that dashboard financial summaries correctly handle transactions recorded in multiple currencies.

---

## TS-056 — Dashboard With No Transactions

**Module:** Dashboard  
**Priority:** Medium  
**Type:** Functional / Boundary  
**Requirement:** FR-053

**Scenario:**  
Verify that the dashboard displays an appropriate state when the user has no financial transactions.

---

## TS-057 — Dashboard Calculation Accuracy

**Module:** Dashboard  
**Priority:** Critical  
**Type:** Calculation / Data Integrity  
**Requirement:** FR-048 to FR-050, FR-055

**Scenario:**  
Verify that dashboard income, expense and balance calculations accurately reflect the underlying transaction data.

---

# 11. Additional Transaction Scenarios

## TS-058 — Transaction Currency Selection

**Module:** Transactions / Currency  
**Priority:** Critical  
**Type:** Functional / Validation  
**Requirement:** FR-058, FR-070 to FR-072

**Scenario:**  
Verify that a user can select an appropriate currency when creating a financial transaction.

---

## TS-059 — Multiple Currency Transactions

**Module:** Transactions / Currency  
**Priority:** Critical  
**Type:** Functional / Data Integrity  
**Requirement:** FR-072, FR-128 to FR-129

**Scenario:**  
Verify that a user can record transactions using different currencies within the same account.

---

## TS-060 — Original Currency Preservation

**Module:** Transactions / Currency  
**Priority:** Critical  
**Type:** Data Integrity  
**Requirement:** FR-070 to FR-074, FR-134

**Scenario:**  
Verify that the original transaction amount and currency remain unchanged when the user's default display currency changes.

---

## TS-061 — Currency Conversion

**Module:** Transactions / Currency  
**Priority:** Critical  
**Type:** Functional / Calculation  
**Requirement:** FR-075 to FR-076, FR-130 to FR-131

**Scenario:**  
Verify that financial values are converted correctly when conversion to the default display currency is required.

---

## TS-062 — Transaction Amount Boundary Validation

**Module:** Transactions  
**Priority:** High  
**Type:** Boundary / Validation  
**Requirement:** FR-077

**Scenario:**  
Verify that transaction amount boundary conditions and invalid amounts are handled according to the defined validation rules.

---

## TS-063 — Duplicate Transaction Submission

**Module:** Transactions  
**Priority:** High  
**Type:** Data Integrity / Negative  
**Requirement:** FR-079

**Scenario:**  
Verify that repeated submission of the same transaction request does not unintentionally create duplicate transactions.

---

## TS-064 — Future Transaction Date

**Module:** Transactions  
**Priority:** Medium  
**Type:** Boundary / Validation  
**Requirement:** FR-078

**Scenario:**  
Verify that transactions using future dates are handled according to the application's defined date rules.

---

## TS-065 — Transaction Date Boundary

**Module:** Transactions  
**Priority:** High  
**Type:** Boundary / Validation  
**Requirement:** FR-078, FR-080

**Scenario:**  
Verify that transaction dates at supported minimum, maximum and period-boundary values are handled correctly.

---

## TS-066 — Large Transaction Dataset

**Module:** Transactions / Performance  
**Priority:** High  
**Type:** Performance / Scalability  
**Requirement:** NFR-004, NFR-052

**Scenario:**  
Verify that transaction history, search, filtering and related operations remain usable when a large number of transactions exist.

---

# 12. Additional Category Scenarios

## TS-067 — Invalid Category

**Module:** Categories  
**Priority:** High  
**Type:** Validation  
**Requirement:** FR-084

**Scenario:**  
Verify that invalid or unsupported categories cannot be assigned to transactions.

---

## TS-068 — Category Type Validation

**Module:** Categories  
**Priority:** Medium  
**Type:** Functional / Validation  
**Requirement:** FR-085

**Scenario:**  
Verify that category rules are correctly applied according to the transaction type.

---

# 13. Additional Analytics Scenarios

## TS-069 — Analytics With No Data

**Module:** Analytics  
**Priority:** Medium  
**Type:** Boundary / Functional  
**Requirement:** FR-093

**Scenario:**  
Verify that analytics display an appropriate result when the user has no financial transaction data.

---

## TS-070 — Multi-Currency Analytics

**Module:** Analytics / Currency  
**Priority:** Critical  
**Type:** Functional / Calculation  
**Requirement:** FR-094 to FR-095, FR-128 to FR-133

**Scenario:**  
Verify that analytics correctly handle transactions recorded in multiple currencies using appropriate currency conversion.

---

## TS-071 — Analytics Calculation Accuracy

**Module:** Analytics  
**Priority:** Critical  
**Type:** Calculation / Data Integrity  
**Requirement:** FR-087 to FR-090, FR-097

**Scenario:**  
Verify that analytics calculations accurately represent the underlying financial transaction data.

---

## TS-072 — Analytics Date Boundaries

**Module:** Analytics  
**Priority:** High  
**Type:** Boundary / Calculation  
**Requirement:** FR-091, FR-096

**Scenario:**  
Verify that analytics correctly include and exclude transactions at financial period boundaries.

---

# 14. Additional Data Management Scenarios

## TS-073 — Export Data Accuracy

**Module:** Data Management  
**Priority:** Critical  
**Type:** Data Integrity  
**Requirement:** FR-100 to FR-101

**Scenario:**  
Verify that exported financial data accurately represents the user's stored transaction information, including original amounts and currencies.

---

## TS-074 — Export Data Privacy

**Module:** Data Management / Security  
**Priority:** Critical  
**Type:** Security / Privacy  
**Requirement:** FR-102 to FR-103, NFR-007, NFR-015

**Scenario:**  
Verify that exported financial data is accessible only to the authorised user and does not unnecessarily expose sensitive security information.

---

## TS-075 — Import Duplicate Handling

**Module:** Data Management  
**Priority:** Critical  
**Type:** Data Integrity  
**Requirement:** FR-115 to FR-117

**Scenario:**  
Verify that importing financial data does not unintentionally create duplicate transactions or overwrite existing financial records.

---

# 15. Additional User Settings Scenarios

## TS-076 — Default Currency Change

**Module:** User Settings / Currency  
**Priority:** Critical  
**Type:** Functional / Data Integrity  
**Requirement:** FR-123, FR-125 to FR-126

**Scenario:**  
Verify that a user can change their default display currency and that the change is correctly applied to relevant financial information.

---

## TS-077 — Original Transaction Currency Preservation

**Module:** User Settings / Transactions  
**Priority:** Critical  
**Type:** Data Integrity  
**Requirement:** FR-126, FR-134

**Scenario:**  
Verify that changing the default display currency does not modify the original currency or amount stored for existing transactions.

---

# 16. Additional Security and Quality Scenarios

## TS-078 — API Security

**Module:** API / Security  
**Priority:** Critical  
**Type:** Security  
**Requirement:** FR-029, NFR-010 to NFR-012

**Scenario:**  
Verify that backend APIs enforce appropriate authentication, authorisation, secure communication and input validation.

---

## TS-079 — Authentication Session Security

**Module:** Authentication / Security  
**Priority:** Critical  
**Type:** Security  
**Requirement:** FR-031 to FR-034, NFR-014

**Scenario:**  
Verify that authentication sessions are securely created, maintained, expired and terminated.

---

## TS-080 — Sensitive Data Exposure

**Module:** Security / Privacy  
**Priority:** Critical  
**Type:** Security  
**Requirement:** FR-046, NFR-007, NFR-015, NFR-019

**Scenario:**  
Verify that passwords, authentication credentials, session information and sensitive financial information are not unnecessarily exposed through the application.

---

## TS-081 — Input Injection Protection

**Module:** Security  
**Priority:** Critical  
**Type:** Security / Negative  
**Requirement:** FR-009, NFR-008, NFR-012

**Scenario:**  
Verify that malicious or executable input cannot be used to execute unintended HTML, JavaScript, SQL or other injection attacks.

---

## TS-082 — Accessibility Keyboard Navigation

**Module:** Accessibility  
**Priority:** High  
**Type:** Accessibility  
**Requirement:** NFR-031 to NFR-034

**Scenario:**  
Verify that core application functionality can be accessed and operated using keyboard navigation and appropriate accessibility mechanisms.

---

## TS-083 — API Response Validation

**Module:** API / Data Integrity  
**Priority:** High  
**Type:** API / Data Integrity  
**Requirement:** NFR-044, NFR-048

**Scenario:**  
Verify that API responses contain the correct structure, data and status information and do not expose unauthorised or sensitive information.

---

## TS-084 — Database Integrity

**Module:** Database / Data Integrity  
**Priority:** Critical  
**Type:** Database / Data Integrity  
**Requirement:** FR-080, NFR-023 to NFR-025, NFR-048

**Scenario:**  
Verify that database operations maintain transaction relationships, user ownership, financial accuracy and data consistency.

---

## TS-085 — Recovery and Backup Validation

**Module:** Reliability / Data Management  
**Priority:** High  
**Type:** Reliability / Recovery  
**Requirement:** NFR-023 to NFR-025

**Scenario:**  
Verify that financial data can be appropriately recovered following a supported backup, database or service failure scenario.

---

# Scenario Summary

| Module | Scenario Range | Count |
|---|---:|---:|
| Authentication | TS-001 - TS-008 | 8 |
| Dashboard | TS-009 - TS-014 | 6 |
| Transactions | TS-015 - TS-024 | 10 |
| Categories | TS-025 - TS-027 | 3 |
| Financial Analytics | TS-028 - TS-033 | 6 |
| Data Management | TS-034 - TS-038 | 5 |
| User Settings | TS-039 - TS-042 | 4 |
| Cross-Cutting Quality | TS-043 - TS-050 | 8 |
| Additional Authentication | TS-051 - TS-054 | 4 |
| Additional Dashboard | TS-055 - TS-057 | 3 |
| Additional Transactions | TS-058 - TS-066 | 9 |
| Additional Categories | TS-067 - TS-068 | 2 |
| Additional Analytics | TS-069 - TS-072 | 4 |
| Additional Data Management | TS-073 - TS-075 | 3 |
| Additional User Settings | TS-076 - TS-077 | 2 |
| Additional Security & Quality | TS-078 - TS-085 | 8 |
| **Total** | **TS-001 - TS-085** | **85** |

---

## Future Feature Testing

The following features are outside the current MVP scenario scope and shall receive dedicated scenarios if and when they are implemented:

- Login OTP
- Two-factor authentication
- Multi-factor authentication
- Passwordless authentication
- AI/OCR PDF extraction
- AI/OCR image and receipt extraction
- Budget management
- Recurring transactions
- Debt and EMI tracking
- Financial goals
- Advanced personalised financial insights
- Notifications
- Dedicated mobile application
- Advertising
- Paid subscription
