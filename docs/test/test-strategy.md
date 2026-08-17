# Personal Finance Tracker - Test Strategy

## 1. Test Objectives

The primary objective of testing is to verify that the Personal Finance Tracker meets its defined functional and non-functional requirements and provides a reliable, secure and user-friendly experience.

The testing process will aim to:

1. **Verify functional correctness**

   * Confirm that application features behave according to the approved requirements.
   * Verify that users can successfully perform supported financial operations.
   * Ensure that calculations, transaction processing and financial summaries are accurate.

2. **Identify defects early**

   * Identify defects as early as possible during the development lifecycle.
   * Prevent defects from progressing into later stages of development or production.
   * Support developers in reproducing, investigating and resolving identified issues.

3. **Validate data accuracy and integrity**

   * Verify that financial data entered by users is correctly validated and stored.
   * Confirm that data displayed by the application matches the underlying database data where appropriate.
   * Verify that financial calculations and analytical results are accurate.

4. **Verify security and access control**

   * Ensure that authenticated users can access only authorised functionality and data.
   * Verify that users cannot access or modify another user's financial information.
   * Identify common security weaknesses in application functionality and APIs.

5. **Verify usability and accessibility**

   * Confirm that the application is understandable and easy to use.
   * Verify that users receive clear feedback when operations succeed or fail.
   * Validate core functionality against appropriate accessibility expectations.

6. **Verify compatibility and responsiveness**

   * Confirm that the application functions correctly across supported browsers and screen sizes.
   * Verify that core functionality remains usable on desktop, tablet and mobile devices.

7. **Verify performance and reliability**

   * Identify performance issues affecting common user operations.
   * Verify that the application handles expected transaction volumes appropriately.
   * Confirm that application and database failures are handled without exposing sensitive information.

8. **Provide confidence through automation**

   * Automate suitable regression and end-to-end test scenarios using Playwright with TypeScript.
   * Automate appropriate API-level tests.
   * Integrate automated tests into the development and CI/CD workflow.

9. **Support continuous quality improvement**

   * Use test results, defect trends, user feedback and application metrics to identify areas for improvement.
   * Continuously review and improve the testing approach as the application evolves.

## 2. Test Scope

### 2.1 In Scope

### 2.1 In Scope

The following areas are within the scope of testing for the initial MVP:

#### User Account and Authentication

* User registration
* User login
* User logout
* Password management
* Authentication validation
* Access control for protected resources
* Session and authentication behaviour

#### Dashboard

* Financial summary
* Income calculations
* Expense calculations
* Balance calculations
* Recent transactions
* Period selection and filtering

#### Transactions

* Creating income transactions
* Creating expense transactions
* Editing transactions
* Deleting transactions
* Transaction validation
* Transaction history
* Transaction search and filtering
* Transaction calculations
* User ownership and authorisation

#### Categories

* Predefined income categories
* Predefined expense categories
* Assigning categories to transactions
* Category validation

#### Financial Analytics

* Income versus expenses
* Category-based spending analysis
* Spending trends
* Period-based analysis
* Accuracy of analytical calculations

#### Data Management

* Data persistence
* Data validation
* Data export
* Data import where implemented
* Data integrity

#### User Settings

* User preferences
* Default currency
* Account settings

#### Non-Functional Testing

* Performance
* Security
* Accessibility
* Usability
* Browser compatibility
* Responsive behaviour
* Reliability
* Error handling

#### Technical Testing

* Unit testing where appropriate
* API testing
* Database testing
* Integration testing
* End-to-end testing
* Regression testing
* Automated testing using Playwright with TypeScript
* CI/CD test execution

### 2.2 Out of Scope

The following areas are outside the scope of the initial MVP and will not be tested until the corresponding functionality is introduced:

* Direct bank account integration
* Automatic bank transaction retrieval
* Investment management
* Investment recommendations or financial advice
* Real-time banking functionality
* Advanced AI-based financial recommendations
* Advertising
* Subscription and payment functionality
* Advanced debt and EMI management
* Advanced multi-currency functionality
* Native mobile applications
* Third-party financial service integrations
* Large-scale production load testing beyond the requirements of the initial release

Out-of-scope functionality may be added to the test scope when it is introduced in a future release.

# 3. Test Levels

### 3.1 Unit Testing

Unit testing will verify individual functions, methods or components in isolation.

Examples for this application include:

* Validating transaction amounts.
* Calculating balances.
* Calculating total income and expenses.
* Validating transaction dates.
* Validating categories.
* Testing individual backend services.

Unit tests should be fast and should normally not depend on external systems such as the production database.

### 3.2 Integration Testing

Integration testing will verify that multiple application components work correctly together.

Examples include:

* Backend services communicating with the PostgreSQL database.
* Authentication services interacting with user data.
* Transaction APIs storing and retrieving database records.
* Financial calculations using persisted transaction data.
* API components interacting with other backend services.

Integration tests will identify problems that may not be visible when individual components are tested separately.

### 3.3 System Testing

System testing will verify the behaviour of the complete application against its defined requirements.

Testing will cover complete functional areas such as:

* User registration and authentication.
* Transaction management.
* Dashboard calculations.
* Categories.
* Financial analytics.
* User settings.
* Data management.

System testing will include both positive and negative scenarios.

### 3.4 End-to-End Testing

End-to-end testing will verify complete user journeys through the application from the user interface through the backend and database.

Examples include:

* Register → Login → Add income → View updated balance.
* Login → Add expense → Verify transaction → Verify dashboard.
* Login → Edit transaction → Verify updated analytics.
* Login → Delete transaction → Verify removal from dashboard.
* Login → Filter transactions → Verify displayed results.

Suitable end-to-end scenarios will be automated using Playwright with TypeScript.

### 3.5 User Acceptance Testing

User Acceptance Testing will verify that the application meets the intended business and user requirements before a public release.

UAT will focus on realistic user workflows rather than detailed technical implementation.

Examples include:

* A user successfully records their monthly salary.
* A user records everyday expenses.
* A user reviews their monthly spending.
* A user identifies their largest spending category.
* A user exports their financial data.

UAT will be performed using realistic test data and representative user scenarios before major public releases.

## 4. Test Types

The project will use a combination of manual and automated testing techniques. The testing approach will be selected based on the purpose, risk and repeatability of each test.

### 4.1 Functional Testing

Functional testing will verify that application features behave according to the defined functional requirements.

Examples include:

* User registration
* User login
* Adding transactions
* Editing transactions
* Deleting transactions
* Dashboard calculations
* Filtering transactions
* Exporting data

Functional testing will include both positive and negative scenarios.

### 4.2 Positive Testing

Positive testing will verify that the application behaves correctly when valid inputs and expected user actions are provided.

Examples:

* Creating an expense with valid information.
* Logging in with valid credentials.
* Selecting a valid transaction category.
* Exporting valid transaction data.

### 4.3 Negative Testing

Negative testing will verify that the application handles invalid, unexpected or unsupported inputs correctly.

Examples:

* Submitting an expense without an amount.
* Entering invalid characters into a numeric field.
* Using invalid login credentials.
* Attempting to access another user's transaction.
* Submitting unsupported data formats.

The system should reject invalid input without creating incorrect or corrupted data.

### 4.4 Boundary Value Testing

Boundary value analysis will be used to test values at and around the limits defined by application requirements.

Examples include:

* Minimum and maximum transaction amounts.
* Minimum and maximum field lengths.
* Date boundaries.
* Maximum supported transaction records where applicable.

### 4.5 Equivalence Partitioning

Equivalence partitioning will be used to divide input data into groups where the system is expected to behave similarly.

For example, if a transaction amount must be greater than zero:

* Valid partition: positive amounts.
* Invalid partition: zero.
* Invalid partition: negative amounts.
* Invalid partition: non-numeric values.

Representative values from each partition will be tested rather than testing every possible input.

### 4.6 Smoke Testing

Smoke testing will be performed after a new build or deployment to determine whether the application is stable enough for more detailed testing.

Core smoke scenarios may include:

* Application loads successfully.
* User can log in.
* Dashboard loads.
* User can create a transaction.
* Transaction appears in transaction history.
* User can log out.

### 4.7 Sanity Testing

Sanity testing will be performed after targeted changes or bug fixes to verify that the affected functionality works correctly and that the change has not introduced obvious related issues.

For example, after fixing transaction editing:

* Verify that a transaction can be edited.
* Verify that the updated transaction is displayed correctly.
* Verify that related dashboard calculations are updated.

### 4.8 Regression Testing

Regression testing will verify that existing functionality continues to work after application changes.

A regression suite will be maintained for critical functionality.

Suitable repeatable regression tests will be automated using Playwright and other appropriate testing tools.

### 4.9 Exploratory Testing

Exploratory testing will be used to investigate the application without relying exclusively on predefined test cases.

Testers will use their knowledge, observations and previous results to explore unexpected behaviours, usability issues and potential defects.

Exploratory testing will be particularly useful during early development and when new features are introduced.

### 4.10 API Testing

API testing will verify backend endpoints independently of the user interface.

Testing will cover:

* Request methods
* Request parameters
* Request bodies
* Response status codes
* Response data
* Response schemas
* Authentication
* Authorisation
* Validation
* Error handling
* Data persistence

API tests will initially support manual investigation and will subsequently be automated where appropriate.

### 4.11 Database Testing

Database testing will verify that application data is stored, retrieved, updated and deleted correctly.

Testing will include:

* Data integrity
* Data types
* Constraints
* Relationships
* Transaction persistence
* Update operations
* Delete operations
* User data isolation
* Accuracy of calculated data

SQL queries will be used to validate database results where appropriate.

### 4.12 Integration Testing

Integration testing will verify interactions between application components and external dependencies.

Examples include:

* Backend and database communication.
* Authentication and user data.
* Transaction APIs and database persistence.
* Analytics services and transaction data.

### 4.13 End-to-End Testing

End-to-end testing will validate complete user journeys through the application.

Critical and repeatable user journeys will be automated using Playwright with TypeScript.

### 4.14 Usability Testing

Usability testing will evaluate whether users can understand and efficiently use the application's main functionality.

Testing will consider:

* Navigation
* Form design
* Error messages
* Transaction entry flow
* Dashboard clarity
* Consistency
* Ease of completing common tasks

### 4.15 Accessibility Testing

Accessibility testing will verify that core application functionality can be used by people with different accessibility needs.

Testing will include:

* Keyboard navigation
* Accessible names and labels
* Focus behaviour
* Form accessibility
* Appropriate colour contrast
* Screen-reader compatibility where applicable

Automated accessibility checks will be supplemented with manual testing.

### 4.16 Compatibility Testing

Compatibility testing will verify application behaviour across supported:

* Web browsers
* Operating systems where applicable
* Desktop screen sizes
* Tablet screen sizes
* Mobile screen sizes

Playwright browser projects may be used to automate cross-browser testing.

### 4.17 Responsive Testing

Responsive testing will verify that the application remains usable at different viewport sizes and that content, forms, navigation and dashboards adapt appropriately.

### 4.18 Performance Testing

Performance testing will evaluate application responsiveness and behaviour under expected workloads.

Testing may include:

* Page load performance
* API response times
* Database query performance
* Dashboard performance
* Transaction processing performance

More advanced load and stress testing may be introduced as the application grows.

### 4.19 Security Testing

Security testing will identify weaknesses that could expose user accounts or financial information.

Testing will include:

* Authentication
* Authorisation
* Session handling
* Input validation
* Access control
* API security
* Sensitive data exposure
* Common web application security risks

Security testing will be performed throughout development rather than only before release.

### 4.20 Data Validation Testing

Data validation testing will verify that financial data is accurate throughout the application.

For example:


                        User Interface
                            ↓
                           API
                            ↓
                        Database
                            ↓
                        Analytics
                            ↓
                        Dashboard


The same transaction should remain accurate throughout this flow.

### 4.21 Manual Testing

Manual testing will be used where human observation, exploratory investigation, usability assessment or rapidly changing functionality makes automation unsuitable.

Manual testing will also be used during early development before stable automated tests are created.

### 4.22 Automated Testing

Automated testing will be used for repeatable, stable and high-value scenarios.

The primary UI automation framework will be:

**Playwright with TypeScript**

Automated testing may include:

* UI tests
* API tests
* End-to-end tests
* Regression tests
* Cross-browser tests
* Accessibility checks

Automated tests will be integrated into the CI/CD pipeline where appropriate.

## 5. Test Environment and Test Data

### 5.1 Test Environments

The application will use separate environments for development, testing and production where practical.

#### Development Environment

The development environment will be used for:

* Application development
* Local debugging
* Unit testing
* Initial feature validation
* Developer-level integration testing

Development data may be reset or recreated as required.

#### Test Environment

The test environment will be used for:

* Formal functional testing
* Integration testing
* API testing
* Database testing
* End-to-end testing
* Regression testing
* Cross-browser testing
* Performance and security testing where appropriate

The test environment should be isolated from production data.

#### Production Environment

The production environment will contain the live application and real user data.

Testing activities in production will be limited to safe, controlled checks and must not intentionally modify or expose real user financial information.

### 5.2 Test Data

Test data will be created specifically for testing purposes wherever possible.

Test data may include:

* User accounts
* Income transactions
* Expense transactions
* Categories
* Dates
* Currency values
* Different transaction amounts
* Valid and invalid input values
* Boundary values
* Large transaction datasets

Financial test data should be synthetic and must not contain real users' sensitive financial information.

### 5.3 Test Accounts

Dedicated test accounts will be created for automated and manual testing.

Different accounts may be used to verify authorisation and data isolation.

For example:

Test User A
Test User B

Testing will verify that Test User A cannot access or modify Test User B's financial information.

Automated tests should use dedicated test credentials rather than personal accounts.

### 5.4 Test Data Management

Test data shall be managed so that tests can be repeated consistently.

Where appropriate:

* Test data will be created automatically before automated test execution.
* Tests should avoid depending on data created by unrelated tests.
* Test data may be cleaned up after test execution.
* Automated tests should be independent and repeatable.
* Sensitive credentials shall not be stored directly in source code.
* Environment variables or secure secret-management mechanisms shall be used for test credentials and other secrets.

Test data should cover normal, boundary, invalid and unexpected scenarios.

### 5.5 Data Privacy

Real personal financial information should not be copied into development or test environments.

If production data is ever required for diagnostic or analytical purposes, it must be appropriately anonymised or otherwise handled in accordance with applicable privacy and data-protection requirements.

### 5.6 Test Data Categories

The test suite should include the following categories of data:

| Data Category   | Examples                                  |
| --------------- | ----------------------------------------- |
| Valid data      | £50, £1,000, valid date, valid category   |
| Invalid data    | Text in amount field, invalid date        |
| Boundary data   | Minimum/maximum supported values          |
| Empty data      | Missing mandatory fields                  |
| Large data      | Large transaction history                 |
| Duplicate data  | Repeated transaction submissions          |
| Security data   | Unauthorised user/access attempts         |
| Multi-user data | Transactions belonging to different users |

## 6. Defect Management

### 6.1 Defect Lifecycle

Defects identified during testing shall be documented and tracked through an appropriate lifecycle.

The expected defect lifecycle is:


                                    New
                                     ↓
                                    Triaged
                                     ↓
                                    Assigned
                                     ↓
                                    In Progress
                                     ↓
                                    Fixed
                                     ↓
                                    Ready for Retest
                                     ↓
                                    Retest
                                     ↓
                                ┌───────────────┐
                                │               │
                              Pass             Fail
                                │               │
                                ↓               ↓
                              Closed         Reopened


A defect may also be rejected, deferred, duplicated or marked as not reproducible following investigation.

### 6.2 Defect Severity

Severity describes the **technical or functional impact of a defect on the application**.

The project will use the following severity levels:

#### Critical

A defect that causes severe application failure, major security exposure or loss/corruption of critical user data.

Example:

* Users can access another user's financial information.
* A production defect causes widespread financial data corruption.

#### High

A defect that significantly affects important functionality and prevents users from completing a major business or user journey.

Example:

* Users cannot log in.
* Users cannot create transactions.
* Dashboard calculations are fundamentally incorrect.

#### Medium

A defect that affects functionality but has a workaround or does not prevent the majority of the application's core functionality.

Example:

* A transaction filter does not work for one supported category.

#### Low

A defect with limited functional impact, such as a minor visual or usability issue.

Example:

* Minor alignment issue on a dashboard component.

### 6.3 Defect Priority

Priority describes **how urgently a defect should be addressed**.

The project will initially use:

* **P1 — Critical:** Fix immediately or before release.
* **P2 — High:** Fix as soon as possible and normally before release.
* **P3 — Medium:** Fix according to release priorities.
* **P4 — Low:** Fix when resources and release priorities allow.

Severity and priority are independent attributes.

For example, a minor visual issue may have low severity but high priority if it affects an important public release or key user journey.

### 6.4 Defect Reporting

Each defect should contain enough information for another team member to understand and reproduce the problem.

Where applicable, a defect report should include:

* Defect ID
* Short, descriptive title
* Environment
* Application version/build
* Preconditions
* Steps to reproduce
* Test data used
* Expected result
* Actual result
* Severity
* Priority
* Evidence such as screenshots, videos, logs or traces
* Related requirement or test case
* Defect status

A defect should be written clearly and objectively without making assumptions about the cause unless the cause has been confirmed.

### 6.5 Defect Retesting and Closure

After a defect has been fixed:

1. The original defect shall be reviewed.
2. The same steps used to reproduce the defect shall be executed again.
3. The expected result shall be verified.
4. Relevant regression tests shall be performed.
5. If the defect is resolved, it may be closed.
6. If the defect still exists, it shall be reopened with updated evidence.

A defect shall not be considered resolved solely because a developer has marked it as fixed. The tester must verify the behaviour.

## 7. Test Documentation and Traceability

### 7.1 Test Scenarios

Test scenarios will describe high-level functionality or user journeys that need to be verified.

Examples:

* Verify that a user can register successfully.
* Verify that a user can log in with valid credentials.
* Verify that a user can create an expense.
* Verify that an expense appears in transaction history.
* Verify that the dashboard reflects a newly created transaction.
* Verify that a user cannot access another user's financial data.

Test scenarios will be derived from the approved functional and non-functional requirements.

### 7.2 Test Cases

Test cases will provide detailed instructions for verifying individual behaviours.

Where appropriate, a test case will contain:

* Test Case ID
* Requirement ID
* Test scenario
* Preconditions
* Test data
* Test steps
* Expected result
* Actual result
* Test status
* Environment
* Tester
* Execution date
* Defect ID, if applicable

Test cases will cover positive, negative, boundary and other relevant test conditions.

### 7.3 Requirement Traceability

Each important requirement shall be traceable to one or more test scenarios and test cases.

The expected relationship is:


                                    Requirement
                                        ↓
                                    User Story
                                        ↓
                                    Acceptance Criteria
                                        ↓
                                    Test Scenario
                                        ↓
                                    Test Case
                                        ↓
                                    Test Execution
                                        ↓
                                    Defect (if applicable)


A Requirement Traceability Matrix (RTM) will be maintained to provide visibility of test coverage.

Example:

| Requirement ID | Requirement                | Test Scenario IDs | Test Case IDs  | Status     |
| -------------- | -------------------------- | ----------------- | -------------- | ---------- |
| FR-013         | Create income transaction  | TS-001            | TC-001, TC-002 | Not Tested |
| FR-014         | Create expense transaction | TS-002            | TC-003, TC-004 | Not Tested |

The RTM will be updated as requirements and test cases evolve.

### 7.4 Test Evidence

Appropriate evidence shall be retained for significant test executions and defects.

Evidence may include:

* Screenshots
* Screen recordings
* Playwright traces
* Test reports
* API responses
* Database query results
* Application logs
* Console logs

Evidence should contain only the information necessary to demonstrate the test result and must not expose unnecessary sensitive financial or personal information.

### 7.5 Test Results

Test execution results shall be recorded using appropriate statuses.

The initial statuses will include:

* **Not Run**
* **Passed**
* **Failed**
* **Blocked**
* **Skipped**

Failed test cases should be linked to the corresponding defect where applicable.

Test results will be used to assess release readiness and identify areas requiring further testing.

## 8. Test Automation Strategy

### 8.1 Automation Objectives

The primary objectives of test automation are to:

* Reduce repetitive manual testing.
* Provide fast feedback during development.
* Improve regression test coverage.
* Verify critical user journeys consistently.
* Support cross-browser testing.
* Detect defects earlier in the development lifecycle.
* Integrate automated testing into the CI/CD process.
* Maintain reliable and repeatable test execution.

Automation will complement manual testing rather than replace it.

### 8.2 Automation Scope

Automation will initially focus on stable, repeatable and high-value scenarios.

The automation scope will include:

* Critical user journeys.
* Authentication flows.
* Transaction creation and management.
* Dashboard validation.
* API functionality.
* Important negative scenarios.
* Regression scenarios.
* Cross-browser scenarios where appropriate.
* Selected accessibility checks.

Exploratory testing, usability evaluation and rapidly changing functionality will generally remain primarily manual.

### 8.3 Automation Framework

The primary UI automation framework will be:

**Playwright with TypeScript**

Playwright will be used for:

* End-to-end testing.
* UI functional testing.
* Cross-browser testing.
* API testing where appropriate.
* Screenshots and video/trace evidence.
* Automated regression testing.

TypeScript will be used as the primary automation programming language.

Python may be used for other project components and analytical or supporting tasks where appropriate, but the primary UI automation implementation will remain TypeScript with Playwright.

### 8.4 Test Structure

Automated tests will follow a maintainable and scalable structure.

The project will use appropriate patterns and practices such as:

* Page Object Model where beneficial.
* Reusable fixtures.
* Shared test utilities.
* Environment-specific configuration.
* Independent tests.
* Clear test naming conventions.
* Appropriate test grouping and tagging.
* Separation of test data from test logic.

The automation framework should avoid unnecessary duplication and should remain understandable to other developers and testers.

### 8.5 Test Data and Fixtures

Automated tests will use controlled test data.

Where appropriate:

* Test data will be generated automatically.
* Fixtures will provide reusable test setup.
* Tests will avoid depending on the execution order of other tests.
* Test accounts will be isolated from real user accounts.
* Test data will be cleaned up where necessary.
* Sensitive credentials will be stored using environment variables or secure secrets.

Automated tests should be repeatable and capable of running in a clean test environment.

### 8.6 Reporting

Automated test execution shall produce useful results that allow failures to be investigated.

Reports may include:

* Passed tests
* Failed tests
* Skipped tests
* Execution duration
* Error messages
* Screenshots
* Videos where appropriate
* Playwright traces
* Browser information
* Test environment information

Failure evidence should provide enough information to reproduce and investigate the problem.

### 8.7 CI/CD Integration

Automated tests will eventually be integrated into a CI/CD pipeline.

The intended workflow is:


                                Code Change
                                    ↓
                                Git Push / Pull Request
                                    ↓
                                Build
                                    ↓
                                Unit Tests
                                    ↓
                                API / Integration Tests
                                    ↓
                                Playwright Tests
                                    ↓
                                Test Report
                                    ↓
                                Pass → Continue
                                Fail → Investigate


Critical automated tests should run automatically before changes are deployed to production.

### 8.8 Automation Maintenance

Automated tests shall be maintained as the application evolves.

Maintenance activities will include:

* Updating tests when requirements change.
* Removing obsolete tests.
* Improving unstable tests.
* Investigating flaky tests.
* Updating test data.
* Updating Playwright dependencies when appropriate.
* Reviewing test coverage.
* Refactoring duplicated automation code.

Automation quality will be reviewed regularly rather than assuming that an automated test remains reliable indefinitely.

### 8.9 Automation Principles

The automation framework will follow these principles:

1. Automate for value rather than simply increasing the number of automated tests.
2. Keep tests independent and repeatable.
3. Prefer stable and meaningful locators.
4. Avoid unnecessary hard-coded waits.
5. Keep test data controlled.
6. Validate meaningful user outcomes rather than implementation details.
7. Keep failures easy to investigate.
8. Run appropriate tests at the appropriate stage of the development lifecycle.
9. Treat automated tests as production-quality code.
10. Review and maintain the automation suite as part of normal development.


## 9. Entry and Exit Criteria

### 9.1 Entry Criteria

Testing for a feature or release may begin when the applicable entry criteria have been satisfied.

The entry criteria may include:

* Relevant requirements have been reviewed and are sufficiently clear.
* Acceptance criteria have been defined.
* The required application build is available.
* The required test environment is available and accessible.
* Required test accounts and test data are available.
* Major environment or infrastructure dependencies are operational.
* Required test scenarios and test cases have been prepared.
* Known blocking defects from previous testing have been resolved or formally accepted.
* The feature is considered ready for testing by the development team.

Entry criteria may vary depending on the testing level and release stage.

### 9.2 Exit Criteria

Testing for a feature or release may be considered complete when the agreed exit criteria have been satisfied.

The exit criteria may include:

* Planned functional test cases have been executed.
* Critical and high-priority test scenarios have been completed.
* Required regression testing has been completed.
* Critical functionality has passed testing.
* No unresolved Critical defects remain unless formally accepted as a release risk.
* High-severity defects have been reviewed and an appropriate release decision has been made.
* Required automated tests are passing.
* Significant test failures have been investigated.
* Required test evidence has been recorded.
* Known limitations and accepted risks have been documented.
* Test results have been reviewed before release.

Testing may be stopped or extended if significant risks, defects or changes to requirements affect the release.

## 10. Test Metrics

The project will use appropriate test metrics to understand testing progress, quality and risk.

### 10.1 Test Execution Metrics

The following metrics may be tracked:

* Number of planned test cases
* Number of executed test cases
* Number of passed test cases
* Number of failed test cases
* Number of blocked test cases
* Number of skipped test cases
* Test pass percentage
* Test failure percentage

### 10.2 Defect Metrics

The project may track:

* Total defects identified
* Defects by severity
* Defects by priority
* Open versus closed defects
* Defect reopen rate
* Defect resolution time
* Defects identified during regression testing

### 10.3 Test Coverage Metrics

Coverage may include:

* Requirement coverage
* Test scenario coverage
* Functional test coverage
* Automated test coverage
* API test coverage
* Critical user journey coverage

### 10.4 Automation Metrics

The automation framework may track:

* Number of automated tests
* Automation execution time
* Automation pass/failure rate
* Flaky test rate
* Automated regression coverage
* Failed test investigation time

Metrics will be used to support quality decisions rather than treated as the sole measure of application quality.

## 11. Risks and Mitigations 

The project will identify and manage risks that could affect application quality, user data, testing effectiveness or release readiness.

## 11. Risks and Mitigations

The project will identify and manage risks that could affect application quality, user data, testing effectiveness or release readiness.

| Risk                               | Potential Impact                                             | Mitigation                                                                                      |
| ---------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| Incorrect financial calculations   | Users may receive inaccurate financial information           | Use unit tests, API tests, database validation and end-to-end tests for financial calculations. |
| Unauthorised access to user data   | Sensitive financial information may be exposed               | Implement authentication, authorisation, access-control testing and security testing.           |
| Data loss or corruption            | Users may lose important financial records                   | Use database constraints, validation, backups and recovery testing.                             |
| Inadequate input validation        | Invalid or malicious data may enter the system               | Validate input at both frontend and backend levels and perform negative testing.                |
| Defects reaching production        | Users may experience incorrect or broken functionality       | Use regression testing, automated tests and CI/CD quality gates.                                |
| Flaky automated tests              | Unreliable test results may reduce confidence in automation  | Investigate flaky tests, improve test isolation and avoid unnecessary waits.                    |
| Test environment differences       | A feature may pass testing but fail in production            | Keep environments consistent where practical and perform production smoke checks.               |
| Insufficient test coverage         | Important defects may remain undetected                      | Maintain requirement traceability and regularly review test coverage.                           |
| Uncontrolled test data             | Tests may produce inconsistent or unreliable results         | Use controlled, isolated and repeatable test data.                                              |
| Sensitive information in test data | User privacy may be compromised                              | Use synthetic test data and avoid using real financial information.                             |
| Third-party dependency failure     | Application functionality may become unavailable             | Monitor dependencies and implement appropriate error handling.                                  |
| Changing requirements              | Test cases and automation may become outdated                | Maintain traceability and review tests whenever requirements change.                            |
| Excessive project scope            | Development and testing may be delayed                       | Prioritise MVP functionality and manage future features separately.                             |
| Poor database performance          | Dashboards and transactions may become slow                  | Optimise database queries, use appropriate indexes and perform performance testing.             |
| Browser or device incompatibility  | Some users may be unable to use the application correctly    | Perform cross-browser and responsive testing.                                                   |
| Accessibility issues               | Some users may be unable to use the application effectively  | Include accessibility requirements, automated checks and manual accessibility testing.          |
| Inadequate production monitoring   | Production defects may remain undetected                     | Implement appropriate logging, monitoring and error reporting.                                  |
| Incorrect deployment configuration | The application may fail or behave differently in production | Use environment-specific configuration, CI/CD validation and deployment checks.                 |


## 12. Roles and Responsibilities

The project will use clearly defined responsibilities throughout the software development and testing lifecycle. During the initial development stage, one person may perform multiple roles.

| Role                      | Responsibilities                                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Product Owner             | Define product goals, prioritise features, review requirements and provide decisions on product behaviour.                            |
| Developer                 | Design and implement application functionality, fix defects, write unit tests and maintain application code.                          |
| Test Analyst              | Analyse requirements, identify test conditions, design test scenarios and test cases, execute tests, report defects and verify fixes. |
| Automation Engineer       | Design, implement and maintain automated tests using Playwright with TypeScript and integrate automation into CI/CD.                  |
| Data Analyst              | Analyse application data, develop SQL queries, validate analytical results and create meaningful dashboards and reports.              |
| DevOps / Deployment Owner | Manage application environments, CI/CD pipelines, deployment configuration, monitoring and release processes.                         |
| Project Owner             | Coordinate the overall project, review progress, manage scope and ensure project objectives are met.                                  |

### 12.1 Initial Project Responsibilities

During the initial development phase, the project owner will perform the responsibilities of the Product Owner, Developer, Test Analyst, Automation Engineer, Data Analyst and DevOps / Deployment Owner.

As the project grows, these responsibilities may be separated into dedicated roles or contributors.

## 13. Test Deliverables

The following testing deliverables will be created and maintained throughout the project.

| Deliverable                     | Purpose                                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------------- |
| Test Strategy                   | Defines the overall testing approach, scope, objectives, levels, types, tools and processes.  |
| Test Scenarios                  | Defines high-level conditions and user journeys that need to be tested.                       |
| Test Cases                      | Provides detailed steps, test data and expected results for individual tests.                 |
| Requirement Traceability Matrix | Maps requirements to test scenarios and test cases to demonstrate coverage.                   |
| Test Data                       | Provides controlled data required for manual and automated testing.                           |
| Defect Reports                  | Records defects identified during testing and tracks their resolution.                        |
| Test Execution Results          | Records the outcome of executed test cases.                                                   |
| Automated Test Suite            | Contains automated API and end-to-end tests.                                                  |
| Test Reports                    | Summarises automated and manual testing results.                                              |
| Test Evidence                   | Provides screenshots, traces, logs, API responses and other supporting evidence.              |
| CI/CD Test Results              | Provides evidence of automated test execution during the development and deployment pipeline. |
| Release Test Summary            | Provides an overall assessment of testing completed and known quality risks before a release. |