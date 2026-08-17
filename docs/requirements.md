# Personal Finance Tracker — Requirements

## 1. Project Overview

This application is a Personal Finance Tracker.

Users can record their income and expenses and see their financial position.

The purpose is to help people understand where their money is going.

The application will be simple and easy to use, with analytics and
features that help users make better financial decisions.

## 2. Problem Statement

Managing personal finances can become difficult when income and expenses
come from different sources. Users may not have a simple way to understand
their overall financial position.

Users may record transactions but still struggle to understand their
spending patterns, recurring expenses and monthly cash flow.

This application aims to provide a simple way to record financial
transactions and turn that data into useful information.

## 3. Target Users

### 1. General Users
People who want a simple way to record income and expenses and understand
their monthly spending.

### 2. Students
Students who need to manage limited income and track their spending.

### 3. International Users
Users who receive income or make payments in different currencies.

## 4. Project Goals

The main goals of the Personal Finance Tracker are:

### 1. Simplify personal finance management by providing users with an easy way to record and manage their income and expenses.
### 2. Help users understand their financial position by showing their income, expenses, balance and overall cash flow in a clear format.
### 3. Provide useful financial analytics that help users identify spending patterns, major expense categories and changes in their financial behaviour.
### 4. Support informed financial decisions by presenting financial information in a simple and understandable way.
### 5. Protect user financial information through appropriate security, privacy and data-protection practices.
### 6. Provide a reliable and user-friendly application that works effectively across commonly used devices and screen sizes.
### 7. Make the application freely available to the public so that users can access the core personal finance tracking features without paying for the service.
### 8. Build the application using professional software-development and testing practices, including version control, automated testing, API testing, database testing and continuous integration.
### 9. Continuously improve the application using user feedback, application usage data and identified defects or usability issues.

## 5. Functional Requirements

### 5.1 User Account and Authentication

**FR-001:** The system shall allow a new user to create an account using the required registration information.

**FR-002:** The system shall allow registered users to log in using valid credentials.

**FR-003:** The system shall prevent users from accessing protected financial information without authentication.

**FR-004:** The system shall allow authenticated users to log out of their account.

**FR-005:** The system shall provide appropriate validation and error messages when registration or login information is invalid.

**FR-006:** The system shall provide a secure mechanism for users to reset or change their password.

### 5.2 Dashboard

**FR-007:** The system shall provide an overview of the user's financial information after successful authentication.

**FR-008:** The dashboard shall display the user's total income for the selected period.

**FR-009:** The dashboard shall display the user's total expenses for the selected period.

**FR-010:** The dashboard shall display the user's calculated balance for the selected period.

**FR-011:** The dashboard shall display a summary of recent financial transactions.

**FR-012:** The dashboard shall allow the user to select or change the financial period being analysed.

### 5.3 Transactions

**FR-013:** The system shall allow authenticated users to create an income transaction.

**FR-014:** The system shall allow authenticated users to create an expense transaction.

**FR-015:** A transaction shall contain, at minimum, a transaction type, amount, date, category and currency.

**FR-016:** The system shall allow users to optionally provide additional transaction information, such as a description and payment method.

**FR-017:** The system shall validate transaction information before saving the transaction.

**FR-018:** The system shall prevent invalid transaction data from being saved.

**FR-019:** The system shall display a confirmation when a transaction has been successfully created.

**FR-020:** The system shall display saved transactions in the user's transaction history.

**FR-021:** The system shall allow users to edit their own transactions.

**FR-022:** The system shall allow users to delete their own transactions.

**FR-023:** The system shall require appropriate confirmation before permanently deleting a transaction.

**FR-024:** The system shall allow users to search and filter their transactions.

**FR-025:** The system shall ensure that users can only view and modify transactions belonging to their own account.

### 5.4 Categories

**FR-026:** The system shall provide predefined income and expense categories.

**FR-027:** The system shall allow users to assign a category to a transaction.

**FR-028:** The system shall prevent a transaction from being saved when a mandatory category is missing.

**FR-029:** The system shall allow users to manage personal categories in a future release.

### 5.5 Financial Analytics

**FR-030:** The system shall calculate total income and expenses for a selected period.

**FR-031:** The system shall provide a breakdown of expenses by category.

**FR-032:** The system shall display income versus expenses for a selected period.

**FR-033:** The system shall provide spending trends over time.

**FR-034:** The system shall allow users to change the period used for financial analysis.

**FR-035:** The system shall ensure that analytics are calculated using the user's authorised transaction data.

### 5.6 Data Management

**FR-036:** The system shall securely store user transaction data.

**FR-037:** The system shall allow users to export their financial transaction data in a supported format.

**FR-038:** The system shall validate imported financial data before adding it to the user's account.

**FR-039:** The system shall prevent invalid or corrupted data from being imported into the system.

**FR-040:** The system shall provide appropriate feedback when data is successfully imported or exported.

### 5.7 User Settings

**FR-041:** The system shall allow users to view and manage their account settings.

**FR-042:** The system shall allow users to select their preferred default currency.

**FR-043:** The system shall apply the user's selected currency to relevant financial information.

**FR-044:** The system shall provide appropriate settings for managing user preferences.

### Future Functional Requirements

The following functionality is outside the initial MVP and may be considered for future releases:

* Recurring income and expenses
* Budget management
* Credit-card tracking
* Loan and EMI tracking
* Multi-currency financial management
* GBP/INR conversion
* Financial goals and savings tracking
* Notifications and reminders
* Advanced financial analytics
* Personalised financial insights
* Mobile/PWA functionality
* Advertising
* Optional subscription to remove advertisements


## 6. Non-Functional Requirements

### 6.1 Performance

**NFR-001:** The application should provide a responsive user experience for normal user operations.

**NFR-002:** Common user actions such as loading the dashboard, viewing transactions and submitting a transaction should normally complete within an acceptable response time.

**NFR-003:** Database queries should be designed efficiently to avoid unnecessary performance degradation as the volume of transaction data increases.

### 6.2 Security

**NFR-004:** The application shall protect user financial information from unauthorised access.

**NFR-005:** User passwords shall never be stored in plain text.

**NFR-006:** Sensitive information shall not be exposed through application logs, error messages or client-side code.

**NFR-007:** The application shall validate and sanitise user-provided data.

**NFR-008:** The application shall enforce authorisation so that users can only access and modify their own financial data.

**NFR-009:** Communication between the application and backend services shall use secure protocols in production.

### 6.3 Privacy and Data Protection

**NFR-010:** The application shall collect only personal information that is necessary for its intended functionality.

**NFR-011:** The application shall provide users with appropriate information about how their personal data is collected, stored and processed.

**NFR-012:** Users shall be able to request deletion of their account and associated personal data, subject to applicable legal and technical requirements.

**NFR-013:** User financial data shall be protected against unauthorised disclosure or modification.

### 6.4 Reliability and Availability

**NFR-014:** The application should be available and functional for users under normal operating conditions.

**NFR-015:** The system shall handle expected application and database errors without exposing sensitive technical information to users.

**NFR-016:** Production data shall be backed up using an appropriate backup strategy.

**NFR-017:** The application shall provide an appropriate recovery process in the event of data or service failure.

### 6.5 Usability

**NFR-018:** The application shall provide a simple and intuitive interface for recording and reviewing financial transactions.

**NFR-019:** User-facing validation and error messages shall clearly explain what the user needs to correct.

**NFR-020:** The application should minimise the number of steps required to record a common transaction.

**NFR-021:** The application should provide a consistent user experience across its main features.

### 6.6 Accessibility

**NFR-022:** The application should support keyboard navigation for core functionality.

**NFR-023:** User interface elements shall have appropriate labels and accessible names.

**NFR-024:** The application should provide sufficient visual contrast and should not rely solely on colour to communicate important information.

### 6.7 Compatibility and Responsiveness

**NFR-025:** The application shall support commonly used modern web browsers.

**NFR-026:** The application shall provide a usable experience on desktop, tablet and mobile screen sizes.

### 6.8 Maintainability

**NFR-027:** The application code shall follow consistent coding standards and project conventions.

**NFR-028:** The application shall use version control throughout development.

**NFR-029:** The application shall be structured into appropriate components and services to support future maintenance and feature development.

**NFR-030:** Important technical decisions and application behaviour shall be documented.

### 6.9 Testability

**NFR-031:** Application components shall be designed so that they can be tested independently where practical.

**NFR-032:** The backend shall expose testable APIs for supported application functionality.

**NFR-033:** The application shall support automated testing using an appropriate testing framework.

**NFR-034:** Automated tests shall be capable of running independently in a controlled test environment.

**NFR-035:** The project shall maintain separate test data and environments where appropriate to prevent testing activities from affecting production data.

### 6.10 Scalability

**NFR-036:** The application architecture should allow the system to support an increasing number of users and transactions without requiring a complete redesign.

**NFR-037:** Database and application components should be designed with future growth in mind.

### 6.11 Observability and Monitoring

**NFR-038:** The production application shall provide appropriate application and error logging.

**NFR-039:** Monitoring mechanisms should allow significant application failures and service issues to be identified.

**NFR-040:** Logs and monitoring data shall avoid unnecessarily storing sensitive user financial information.


## 7. Future Features

## 7. Future Features

The following features are outside the initial MVP scope but may be considered in future releases based on user feedback, application usage and product priorities.

### 7.1 Budget Management

* Allow users to create monthly or custom budgets.
* Allow users to set spending limits for individual categories.
* Notify users when they approach or exceed a budget.
* Provide budget-versus-actual spending analysis.

### 7.2 Recurring Transactions

* Allow users to create recurring income and expense transactions.
* Automatically generate recurring transactions according to the configured schedule.
* Allow users to modify, pause or cancel recurring transactions.

### 7.3 Debt and EMI Tracking

* Allow users to record loans, credit cards and other debts.
* Track outstanding balances and payment schedules.
* Track recurring EMI payments.
* Provide debt repayment summaries and trends.

### 7.4 Multi-Currency Support

* Allow users to record transactions in different currencies.
* Support currency conversion for financial summaries.
* Display transactions using the original transaction currency where appropriate.
* Provide support for common currency pairs such as GBP and INR.

### 7.5 Financial Goals

* Allow users to create savings or financial goals.
* Allow users to define target amounts and target dates.
* Track progress towards financial goals.

### 7.6 Advanced Analytics

* Provide more detailed spending and cash-flow analysis.
* Identify spending trends and significant changes in financial behaviour.
* Provide interactive charts and reports.
* Support advanced analytical dashboards.

### 7.7 Data Import and Integration

* Support importing transactions from supported CSV formats.
* Provide improved transaction categorisation for imported data.
* Explore integrations with appropriate financial data providers in future releases.

### 7.8 Notifications

* Provide optional reminders for recurring expenses and financial activities.
* Allow users to configure notification preferences.

### 7.9 Mobile and Progressive Web Application

* Provide an improved mobile experience.
* Explore Progressive Web App functionality.
* Support installation on supported mobile devices.

### 7.10 Community and Open-Source Development

* Consider making selected components of the application open source.
* Encourage community feedback and contributions where appropriate.
* Publish technical documentation and development information.

### 7.11 Advertising and Optional Subscription

The core application is intended to remain free.

If the application develops a meaningful base of returning users, non-intrusive advertising may be introduced.

A future optional subscription may allow users to remove advertisements and potentially access additional features.

Advertising and subscription functionality will not be part of the initial MVP and will only be considered after the application has established genuine user adoption.