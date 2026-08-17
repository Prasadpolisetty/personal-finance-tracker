# Personal Finance Tracker - Requirements

## 1. Project Overview

This application is a Personal Finance Tracker.

Users can record their income and expenses and see their financial position.

The purpose is to help people understand where their money is going.

The application will be simple and easy to use, with analytics and features that help users make better financial decisions.

The application will initially be provided free of charge, with the core personal finance tracking functionality available to users without requiring payment.

## 2. Problem Statement

Managing personal finances can become difficult when income and expenses come from different sources. Users may not have a simple way to understand their overall financial position.

Users may record transactions but still struggle to understand their spending patterns, recurring expenses and monthly cash flow.

This application aims to provide a simple way to record financial transactions and turn that data into useful information.

The application will also support users who deal with multiple currencies, allowing each transaction to retain its original currency while providing a default display currency for financial summaries and analysis.

## 3. Target Users

### 3.1 General Users

People who want a simple way to record income and expenses and understand their monthly spending.

### 3.2 Students

Students who need to manage limited income and track their spending.

### 3.3 International Users

Users who receive income or make payments in different currencies.

## 4. Project Goals

The main goals of the Personal Finance Tracker are:

### 4.1 Simplify Personal Finance Management

Provide users with an easy way to record and manage their income and expenses.

### 4.2 Improve Financial Awareness

Help users understand their financial position by showing their income, expenses, balance and overall cash flow in a clear format.

### 4.3 Provide Financial Analytics

Provide useful financial analytics that help users identify spending patterns, major expense categories and changes in their financial behaviour.

### 4.4 Support Informed Financial Decisions

Present financial information in a simple and understandable way.

### 4.5 Protect User Financial Information

Protect user financial information through appropriate security, privacy and data-protection practices.

### 4.6 Provide a Reliable User Experience

Provide a reliable and user-friendly application that works effectively across commonly used devices and screen sizes.

### 4.7 Provide the Core Application Free of Charge

Make the application freely available to the public so that users can access the core personal finance tracking features without paying for the service.

### 4.8 Apply Professional Software Development and Testing Practices

Build the application using professional software-development and testing practices, including:

- Version control
- Requirements management
- Test scenario design
- Test case design
- Manual testing
- Automated testing
- API testing
- Database testing
- Continuous integration
- Defect management
- Regression testing

### 4.9 Continuous Improvement

Continuously improve the application using user feedback, application usage data and identified defects or usability issues.

# 5. Functional Requirements

## 5.1 User Account and Authentication

### Registration

**FR-001:** The system shall allow a new user to create an account using a name, email address, password and password confirmation.

**FR-002:** The system shall require all mandatory registration fields to be completed before an account can be created.

### Name Requirements

**FR-003:** The name shall be used as the user's display name and does not need to represent the user's legal or real-world name.

**FR-004:** The name shall not be empty or contain only whitespace.

**FR-005:** The system shall allow a name consisting of a single character, word or longer name.

**FR-006:** The system shall allow numbers, spaces and supported special characters in the name.

**FR-007:** Emojis shall not be permitted in the name field.

**FR-008:** Prohibited or offensive terms shall not be permitted in the name field.

**FR-009:** User-provided name content shall be safely handled and shall not execute HTML, JavaScript or other executable content.

### Email Requirements

**FR-010:** The email address shall be required for registration.

**FR-011:** The email address shall follow the application's supported valid email format.

**FR-012:** Leading and trailing whitespace shall be removed from an email address before processing.

**FR-013:** Email addresses shall be treated case-insensitively for account identification.

**FR-014:** The system shall prevent more than one account from being registered using the same email address.

**FR-015:** The system shall prevent registration using known disposable or temporary email addresses.

**FR-016:** The system shall avoid unnecessarily revealing whether a specific email address is already registered.

### Email Verification

**FR-017:** The system shall require the user to verify their registered email address before accessing protected application functionality.

**FR-018:** The system shall provide an email verification mechanism after successful registration.

**FR-019:** Invalid email verification attempts shall be rejected.

**FR-020:** Expired email verification mechanisms shall be rejected.

**FR-021:** An email verification mechanism that has already been successfully used shall not be reusable.

**FR-022:** The system shall provide an appropriate mechanism for users to request email verification again where required.

### Login

**FR-023:** The system shall allow verified users to log in using valid email and password credentials.

**FR-024:** The system shall reject invalid authentication attempts.

**FR-025:** Authentication errors shall provide appropriate feedback without unnecessarily revealing whether an email address is registered.

**FR-026:** Email addresses shall be treated case-insensitively during authentication.

**FR-027:** Leading and trailing whitespace around an email address shall not cause a valid account to be incorrectly rejected.

### Protected Access

**FR-028:** The system shall prevent unauthenticated users from accessing protected financial information or functionality.

**FR-029:** Protected application APIs shall enforce authentication independently of frontend restrictions.

**FR-030:** The system shall ensure that authenticated users can only access financial information belonging to their own account.

### Logout and Session Management

**FR-031:** The system shall allow authenticated users to log out of their account.

**FR-032:** The system shall terminate or invalidate the authenticated session appropriately after logout.

**FR-033:** An expired or invalid session shall not provide access to protected resources.

**FR-034:** Previously authenticated users shall not be able to access protected financial information after logout without authenticating again.

### Password Management

**FR-035:** The system shall provide a secure mechanism for users to change their password.

**FR-036:** The system shall provide a secure mechanism for users to reset a forgotten password.

**FR-037:** Passwords shall be between 8 and 64 characters.

**FR-038:** Passwords shall contain at least one uppercase letter.

**FR-039:** Passwords shall contain at least one lowercase letter.

**FR-040:** Passwords shall contain at least one number.

**FR-041:** Passwords shall contain at least one special character.

**FR-042:** Password confirmation shall be required during registration.

**FR-043:** The system shall prevent registration when the password and confirmation password do not match.

**FR-044:** Passwords shall never be stored as plain text.

**FR-045:** Passwords shall be securely hashed before being stored.

**FR-046:** Passwords shall not be exposed through URLs, logs, inappropriate API responses or user-facing error messages.

### Authentication MVP Scope

The MVP shall use email address and password authentication.

The following authentication features are outside the MVP scope:

- Login OTP
- Two-factor authentication
- Multi-factor authentication
- Passwordless OTP authentication

These may be considered as future security enhancements.

## 5.2 Dashboard

**FR-047:** The system shall provide an overview of the user's financial information after successful authentication.

**FR-048:** The dashboard shall display the user's total income for the selected period.

**FR-049:** The dashboard shall display the user's total expenses for the selected period.

**FR-050:** The dashboard shall display the user's calculated balance for the selected period.

**FR-051:** The dashboard shall display a summary of recent financial transactions.

**FR-052:** The dashboard shall allow the user to select or change the financial period being analysed.

**FR-053:** The dashboard shall correctly display financial information when the user has no transactions.

**FR-054:** Dashboard calculations shall use only authorised transaction data belonging to the authenticated user.

**FR-055:** Dashboard financial summaries shall correctly account for transactions recorded in multiple currencies.

## 5.3 Transactions

**FR-056:** The system shall allow authenticated users to create an income transaction.

**FR-057:** The system shall allow authenticated users to create an expense transaction.

**FR-058:** A transaction shall contain, at minimum:

- Transaction type
- Amount
- Date
- Category
- Currency

**FR-059:** The system shall allow users to optionally provide additional transaction information, such as:

- Description
- Payment method

**FR-060:** The system shall validate transaction information before saving the transaction.

**FR-061:** The system shall prevent invalid transaction data from being saved.

**FR-062:** The system shall display a confirmation when a transaction has been successfully created.

**FR-063:** The system shall display saved transactions in the user's transaction history.

**FR-064:** The system shall allow users to edit their own transactions.

**FR-065:** The system shall allow users to delete their own transactions.

**FR-066:** The system shall require appropriate confirmation before permanently deleting a transaction.

**FR-067:** The system shall allow users to search their transactions.

**FR-068:** The system shall allow users to filter their transactions.

**FR-069:** The system shall ensure that users can only view and modify transactions belonging to their own account.

### Transaction Currency Requirements

**FR-070:** Each transaction shall retain its original transaction amount.

**FR-071:** Each transaction shall retain its original transaction currency.

**FR-072:** A transaction may use a currency different from the user's default display currency.

**FR-073:** Changing the user's default display currency shall not change the original amount or original currency of an existing transaction.

**FR-074:** The system shall not directly combine amounts from different currencies as though they were the same currency.

**FR-075:** Where currency conversion is required, the system shall use an appropriate exchange rate.

**FR-076:** Where currency conversion is performed, the system shall retain sufficient information to identify the conversion used.

### Transaction Validation and Integrity

**FR-077:** The system shall validate transaction amounts according to defined amount rules.

**FR-078:** The system shall validate transaction dates according to defined date rules.

**FR-079:** The system shall prevent unintended duplicate transaction creation caused by repeated submission of the same transaction request.

**FR-080:** The system shall maintain transaction data integrity when transactions are created, edited, deleted or retrieved.

## 5.4 Categories

**FR-081:** The system shall provide predefined income and expense categories.

**FR-082:** The system shall allow users to assign a category to a transaction.

**FR-083:** The system shall prevent a transaction from being saved when a mandatory category is missing.

**FR-084:** The system shall reject invalid or unsupported transaction categories.

**FR-085:** The system shall apply appropriate category rules based on the transaction type where such rules are defined.

**FR-086:** The system may allow users to manage personal categories in a future release.

## 5.5 Financial Analytics

**FR-087:** The system shall calculate total income and expenses for a selected period.

**FR-088:** The system shall provide a breakdown of expenses by category.

**FR-089:** The system shall display income versus expenses for a selected period.

**FR-090:** The system shall provide spending trends over time.

**FR-091:** The system shall allow users to change the period used for financial analysis.

**FR-092:** The system shall ensure that analytics are calculated using the user's authorised transaction data.

**FR-093:** The system shall provide appropriate results when the user has no financial transaction data.

**FR-094:** Analytics shall correctly handle transactions recorded in multiple currencies.

**FR-095:** Analytics calculations shall use appropriate currency conversion where required.

**FR-096:** Analytics calculations shall correctly handle financial period boundaries.

**FR-097:** Analytics shall accurately represent the underlying transaction data.

## 5.6 Data Management

**FR-098:** The system shall securely store user transaction data.

### Financial Data Export

**FR-099:** The system shall allow users to export their financial transaction data in a supported format.

**FR-100:** Exported financial data shall accurately represent the user's stored financial records.

**FR-101:** Exported transaction records shall retain the original transaction amount and currency.

**FR-102:** Exported financial information shall only be accessible to the authorised user.

**FR-103:** Exported files shall not unnecessarily contain passwords, authentication credentials, session information or other sensitive security information.

### Financial Data Import

**FR-104:** The system shall allow users to import financial data using supported DOCX (.docx), Text (.txt) and Comma-Separated Values (.csv) files.

**FR-105:** The system shall validate imported files before processing their contents.

**FR-106:** The system shall validate imported financial data before adding records to the user's account.

**FR-107:** The system shall reject unsupported file formats.

**FR-108:** The system shall reject corrupted files.

**FR-109:** The system shall reject files that cannot be processed.

**FR-110:** The system shall reject files containing invalid financial data.

**FR-111:** The system shall reject files containing incomplete mandatory transaction information.

**FR-112:** PDF files shall not be supported for financial data import in the MVP.

**FR-113:** Image files shall not be supported for financial data import in the MVP.

**FR-114:** Unsupported spreadsheet, image, executable and other unsupported file formats shall be rejected.

### Import Integrity

**FR-115:** The system shall prevent unintended duplicate transactions during financial data import.

**FR-116:** The system shall validate imported records before persistence.

**FR-117:** Imported data shall not overwrite existing financial records without explicit user action.

**FR-118:** The system shall provide appropriate feedback when data is successfully imported.

**FR-119:** The system shall provide appropriate feedback when an import operation fails.

**FR-120:** The system shall provide appropriate feedback when financial data is successfully exported.

**FR-121:** The system shall provide appropriate feedback when an export operation fails.

## 5.7 User Settings

**FR-122:** The system shall allow users to view and manage their account settings.

**FR-123:** The system shall allow users to select a default display currency after registration and authentication.

**FR-124:** Currency selection shall not be required during registration.

**FR-125:** The system shall apply the user's selected default display currency when displaying relevant financial information where currency conversion is required.

**FR-126:** Changing the user's default display currency shall not modify the original amount or currency stored for existing transactions.

**FR-127:** The system shall provide appropriate settings for managing user preferences.

## 5.8 Multi-Currency Financial Management

**FR-128:** The system shall support financial transactions recorded in multiple currencies.

**FR-129:** The system shall preserve the original currency and amount for each transaction.

**FR-130:** The system shall support conversion of transaction values into the user's default display currency where required for financial summaries and analytics.

**FR-131:** Financial calculations shall account for currency differences and shall not treat amounts from different currencies as equivalent values without conversion.

**FR-132:** The system shall display appropriate currency information when presenting transaction data.

**FR-133:** The system shall display appropriate currency information when presenting financial summaries and analytics.

**FR-134:** The system shall ensure that changing the default display currency does not modify stored transaction values.

# 6. Non-Functional Requirements

## 6.1 Performance

**NFR-001:** The application should provide a responsive user experience for normal user operations.

**NFR-002:** Common user actions such as loading the dashboard, viewing transactions and submitting a transaction should normally complete within an acceptable response time.

**NFR-003:** Database queries should be designed efficiently to avoid unnecessary performance degradation as the volume of transaction data increases.

**NFR-004:** The application should remain usable when processing a large number of transaction records.

## 6.2 Security

**NFR-005:** The application shall protect user financial information from unauthorised access.

**NFR-006:** User passwords shall never be stored in plain text.

**NFR-007:** Sensitive information shall not be exposed through application logs, error messages or client-side code.

**NFR-008:** The application shall validate and sanitise user-provided data.

**NFR-009:** The application shall enforce authorisation so that users can only access and modify their own financial data.

**NFR-010:** Communication between the application and backend services shall use secure protocols in production.

**NFR-011:** API endpoints shall enforce appropriate authentication and authorisation controls.

**NFR-012:** The application shall protect against common input injection attacks.

**NFR-013:** Authentication and authorisation failures shall not unnecessarily expose sensitive account information.

**NFR-014:** Authentication credentials and session information shall be handled securely.

**NFR-015:** Sensitive financial information shall not be unnecessarily exposed through browser responses, URLs, logs or debugging information.

## 6.3 Privacy and Data Protection

**NFR-016:** The application shall collect only personal information that is necessary for its intended functionality.

**NFR-017:** The application shall provide users with appropriate information about how their personal data is collected, stored and processed.

**NFR-018:** Users shall be able to request deletion of their account and associated personal data, subject to applicable legal and technical requirements.

**NFR-019:** User financial data shall be protected against unauthorised disclosure or modification.

**NFR-020:** Financial data shall only be processed for purposes supported by the application's functionality and applicable privacy requirements.

## 6.4 Reliability and Availability

**NFR-021:** The application should be available and functional for users under normal operating conditions.

**NFR-022:** The system shall handle expected application and database errors without exposing sensitive technical information to users.

**NFR-023:** Production data shall be backed up using an appropriate backup strategy.

**NFR-024:** The application shall provide an appropriate recovery process in the event of data or service failure.

**NFR-025:** The system shall prevent partial or inconsistent transaction records where an operation fails.

## 6.5 Usability

**NFR-026:** The application shall provide a simple and intuitive interface for recording and reviewing financial transactions.

**NFR-027:** User-facing validation and error messages shall clearly explain what the user needs to correct.

**NFR-028:** The application should minimise the number of steps required to record a common transaction.

**NFR-029:** The application should provide a consistent user experience across its main features.

**NFR-030:** Financial information shall be presented in a clear and understandable manner.

## 6.6 Accessibility

**NFR-031:** The application should support keyboard navigation for core functionality.

**NFR-032:** User interface elements shall have appropriate labels and accessible names.

**NFR-033:** The application should provide sufficient visual contrast and should not rely solely on colour to communicate important information.

**NFR-034:** Core application functionality should be usable with commonly supported assistive technologies.

## 6.7 Compatibility and Responsiveness

**NFR-035:** The application shall support commonly used modern web browsers.

**NFR-036:** The application shall provide a usable experience on desktop, tablet and mobile screen sizes.

**NFR-037:** The application's responsive layout shall maintain access to core functionality across supported screen sizes.

## 6.8 Maintainability

**NFR-038:** The application code shall follow consistent coding standards and project conventions.

**NFR-039:** The application shall use version control throughout development.

**NFR-040:** The application shall be structured into appropriate components and services to support future maintenance and feature development.

**NFR-041:** Important technical decisions and application behaviour shall be documented.

**NFR-042:** The application shall use appropriate separation of concerns between frontend, backend, data access and other application components.

## 6.9 Testability

**NFR-043:** Application components shall be designed so that they can be tested independently where practical.

**NFR-044:** The backend shall expose testable APIs for supported application functionality.

**NFR-045:** The application shall support automated testing using an appropriate testing framework.

**NFR-046:** Automated tests shall be capable of running independently in a controlled test environment.

**NFR-047:** The project shall maintain separate test data and environments where appropriate to prevent testing activities from affecting production data.

**NFR-048:** The application shall support UI, API and database validation where appropriate.

**NFR-049:** Automated tests shall be suitable for integration into a continuous integration pipeline.

## 6.10 Scalability

**NFR-050:** The application architecture should allow the system to support an increasing number of users and transactions without requiring a complete redesign.

**NFR-051:** Database and application components should be designed with future growth in mind.

**NFR-052:** The application should remain performant as the volume of stored transaction data increases.

## 6.11 Observability and Monitoring

**NFR-053:** The production application shall provide appropriate application and error logging.

**NFR-054:** Monitoring mechanisms should allow significant application failures and service issues to be identified.

**NFR-055:** Logs and monitoring data shall avoid unnecessarily storing sensitive user financial information.

**NFR-056:** Application errors shall contain sufficient diagnostic information for authorised technical investigation without exposing sensitive information to end users.

# 7. MVP Scope

The following functionality is included in the initial MVP:

### Authentication

- User registration
- Name validation
- Email validation
- Duplicate email prevention
- Disposable email prevention
- Email verification
- Login
- Logout
- Password management
- Protected resource access
- Session management

### Dashboard

- Financial overview
- Income summary
- Expense summary
- Balance
- Recent transactions
- Period selection
- Multi-currency financial summaries

### Transactions

- Income transactions
- Expense transactions
- Transaction validation
- Transaction confirmation
- Transaction history
- Transaction editing
- Transaction deletion
- Search
- Filtering
- Transaction authorisation
- Multiple currencies
- Currency conversion

### Categories

- Predefined income categories
- Predefined expense categories
- Transaction categorisation
- Category validation

### Financial Analytics

- Income and expense calculations
- Category spending analysis
- Income versus expenses
- Spending trends
- Period selection
- Multi-currency analytics

### Data Management

- Secure transaction storage
- Financial data export
- DOCX import
- TXT import
- CSV import
- File validation
- Imported data validation
- Duplicate handling
- Import/export feedback

### User Settings

- Account settings
- Default display currency
- Currency application
- User preferences

### Quality

- Security
- Privacy
- Accessibility
- Performance
- Reliability
- Browser compatibility
- Responsive design
- Testability
- Maintainability
- Monitoring

# 8. Future Features

The following functionality is outside the initial MVP scope and may be considered in future releases based on user feedback, application usage, technical feasibility and product priorities.

## 8.1 Login OTP and Multi-Factor Authentication

Potential future authentication enhancements include:

- Login OTP
- Two-factor authentication
- Multi-factor authentication
- Additional authentication factors
- Passwordless authentication

## 8.2 Budget Management

Potential functionality:

- Allow users to create monthly or custom budgets.
- Allow users to set spending limits for individual categories.
- Notify users when they approach or exceed a budget.
- Provide budget-versus-actual spending analysis.

## 8.3 Recurring Transactions

Potential functionality:

- Allow users to create recurring income and expense transactions.
- Automatically generate recurring transactions according to the configured schedule.
- Allow users to modify, pause or cancel recurring transactions.
- Prevent duplicate recurring transaction generation.

## 8.4 Debt and EMI Tracking

Potential functionality:

- Allow users to record loans, credit cards and other debts.
- Track outstanding balances and payment schedules.
- Track recurring EMI payments.
- Provide debt repayment summaries and trends.

## 8.5 Financial Goals

Potential functionality:

- Allow users to create savings or financial goals.
- Allow users to define target amounts and target dates.
- Track progress towards financial goals.

## 8.6 Advanced Analytics

Potential functionality:

- Provide more detailed spending and cash-flow analysis.
- Identify spending trends and significant changes in financial behaviour.
- Provide interactive charts and reports.
- Support advanced analytical dashboards.
- Provide personalised financial insights.

## 8.7 AI-Assisted Document and Image Import

The MVP will not support PDF or image-based financial data import.

A future release may explore AI and OCR technologies to extract financial transaction information from:

- PDF documents
- Images
- Photographs of receipts
- Scanned financial documents

A potential future workflow is:

    Upload PDF/image
          ↓
    AI/OCR extraction
          ↓
    Extracted transaction information
          ↓
    User review
          ↓
    User correction where required
          ↓
    Validation
          ↓
    User confirmation
          ↓
    Transaction creation

AI-extracted financial information shall require user review and explicit confirmation before being added to the user's financial records.

## 8.8 Financial Data Integrations

Potential functionality:

- Integration with appropriate financial data providers.
- Automated transaction retrieval where supported.
- Improved transaction categorisation.
- Additional import formats where appropriate.

## 8.9 Notifications

Potential functionality:

- Provide optional reminders for recurring expenses and financial activities.
- Allow users to configure notification preferences.
- Provide configurable financial alerts.

## 8.10 Mobile and Progressive Web Application

Potential functionality:

- Provide an improved mobile experience.
- Explore Progressive Web App functionality.
- Support installation on supported mobile devices.
- Consider dedicated mobile applications in the future.

## 8.11 Community and Open-Source Development

Potential functionality:

- Consider making selected components of the application open source.
- Encourage community feedback and contributions where appropriate.
- Publish technical documentation and development information.

## 8.12 Advertising and Optional Subscription

The core application is intended to remain free.

If the application develops a meaningful base of returning users, non-intrusive advertising may be introduced.

A future optional subscription may allow users to remove advertisements and potentially access additional features.

Advertising and subscription functionality will not be part of the initial MVP and will only be considered after the application has established genuine user adoption.

# 9. Out of MVP Scope

The following items are explicitly excluded from the initial MVP:

- Login OTP
- Two-factor authentication
- Multi-factor authentication
- Passwordless OTP authentication
- PDF financial data import
- Image financial data import
- AI/OCR financial data extraction
- Budget management
- Recurring transactions
- Debt and EMI tracking
- Financial goals
- Advanced personalised financial insights
- Notifications
- Dedicated mobile application
- Advertising
- Paid subscription