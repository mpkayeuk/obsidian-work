# Form E Data Model

This document maps the UK Form E (Financial Statement for Financial Remedy Proceedings) to a data model for 4mie's conversational AI system.

**Source**: [Gov.uk Form E](https://www.gov.uk/government/publications/form-e-financial-statement-for-a-financial-order-matrimonial-causes-act-1973-civil-partnership-act-2004-for-financial-relief-after-an-overseas)

---

## Section 1: General Information

### 1.1 Personal Details
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| full_name | string | Yes | Including middle names |
| date_of_birth | date | Yes | |
| current_occupation | string | Yes | |
| current_address | address | Yes | |

### 1.2 Marriage/Partnership Details
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| marriage_date | date | Yes | Date of marriage/civil partnership |
| separation_date | date | Yes | |
| petition_issue_date | date | Yes | |
| decree_nisi_date | date | No | If applicable |
| decree_absolute_date | date | No | If applicable |

### 1.3 Current Relationship Status
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| remarried | boolean | Yes | |
| remarriage_date | date | No | If remarried |
| cohabiting | boolean | Yes | Currently living with new partner |
| intend_to_cohabit | boolean | Yes | Within next 6 months |

### 1.4 Children of the Family (Array)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| child_full_name | string | Yes | |
| child_dob | date | Yes | |
| child_living_with | enum | Yes | 'applicant', 'respondent', 'shared', 'other' |
| child_relationship | enum | Yes | 'biological', 'adopted', 'step' |

### 1.5 Health
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| health_conditions | text | No | Long-term conditions affecting earning capacity |
| children_health_conditions | text | No | Conditions affecting children |

### 1.6 Education
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| children_current_education | text | No | Current school arrangements |
| children_future_education | text | No | Planned arrangements |

### 1.7 Child Maintenance
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| maintenance_arrangements | enum | Yes | 'csa', 'private_agreement', 'none', 'to_be_agreed' |
| maintenance_amount | currency | No | Current or proposed amount |
| maintenance_frequency | enum | No | 'weekly', 'monthly', 'annually' |

### 1.8 Other Proceedings
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| other_proceedings | boolean | Yes | Any other court proceedings between parties |
| other_proceedings_details | text | No | Details if yes |

### 1.9 Current Housing
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| housing_status | enum | Yes | 'owned', 'rented', 'living_with_family', 'temporary' |
| housing_details | text | No | |

---

## Section 2: Financial Details

### 2.1 Family Home
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| property_address | address | Yes | |
| land_registry_title | string | No | |
| ownership_type | enum | Yes | 'sole', 'joint_tenants', 'tenants_in_common' |
| ownership_share | percentage | No | If tenants in common |
| property_valuation | currency | Yes | Within last 6 months |
| valuation_date | date | Yes | |
| valuation_basis | enum | Yes | 'estate_agent', 'surveyor', 'agreed' |
| mortgage_lender | string | No | |
| mortgage_balance | currency | No | |
| mortgage_type | enum | No | 'repayment', 'interest_only', 'mixed' |
| early_repayment_charge | currency | No | |
| estimated_sale_costs | currency | No | Agent fees, conveyancing |
| net_equity | currency | Calculated | |
| your_interest_value | currency | Calculated | |

### 2.2 Other Properties (Array)
Same structure as 2.1, repeated for each additional property

### 2.3 Bank Accounts (Array)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| bank_name | string | Yes | |
| account_type | enum | Yes | 'current', 'savings', 'isa', 'other' |
| account_number_last4 | string | Yes | Last 4 digits only |
| sole_or_joint | enum | Yes | 'sole', 'joint' |
| joint_holder_name | string | No | If joint |
| current_balance | currency | Yes | |
| your_share | percentage | Yes | 100% if sole |
| your_interest_value | currency | Calculated | |

### 2.4 Investments (Array)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| institution_name | string | Yes | |
| investment_type | enum | Yes | 'stocks_shares_isa', 'bonds', 'unit_trusts', 'shares', 'crypto', 'other' |
| description | string | No | |
| sole_or_joint | enum | Yes | |
| current_value | currency | Yes | |
| your_share | percentage | Yes | |
| your_interest_value | currency | Calculated | |

### 2.5 Life Insurance Policies (Array)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| insurance_company | string | Yes | |
| policy_type | enum | Yes | 'term', 'whole_life', 'endowment', 'joint' |
| policy_number | string | Yes | |
| surrender_value | currency | Yes | |
| death_benefit | currency | No | |
| maturity_date | date | No | |
| beneficiary | string | No | |
| your_interest_value | currency | Yes | |

### 2.6 Monies Owed to You (Array)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| debtor_description | string | Yes | Who owes you money |
| reason | string | Yes | Why it's owed |
| amount_owed | currency | Yes | |

### 2.7 Cash Holdings
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| cash_held | boolean | Yes | Cash over £500 |
| cash_location | string | No | Where held |
| cash_amount | currency | No | |
| cash_currency | string | No | If not GBP |

### 2.8 Personal Property Over £500 (Array)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| item_description | string | Yes | e.g., 'Car', 'Jewellery', 'Art' |
| estimated_value | currency | Yes | |
| sole_or_joint | enum | Yes | |
| your_interest_value | currency | Yes | |

### 2.9 Liabilities/Debts (Array)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| creditor_name | string | Yes | |
| debt_type | enum | Yes | 'credit_card', 'loan', 'overdraft', 'hire_purchase', 'other' |
| sole_or_joint | enum | Yes | |
| joint_debtor_name | string | No | |
| total_outstanding | currency | Yes | |
| your_share | percentage | Yes | |
| your_liability | currency | Calculated | |

### 2.10 Capital Gains Tax Liability
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| cgt_assets | text | No | Assets that would trigger CGT if sold |
| estimated_cgt | currency | No | |

### 2.11 Business Interests (Array)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| business_name | string | Yes | |
| business_description | string | Yes | What the business does |
| business_type | enum | Yes | 'sole_trader', 'partnership', 'ltd_company', 'llp' |
| ownership_percentage | percentage | Yes | |
| accounting_year_end | date | Yes | |
| latest_accounts_reflect_current | boolean | Yes | |
| accounts_explanation | text | No | If no, explain |
| amounts_owed_by_business | currency | No | Director's loan etc. |
| business_valuation | currency | No | |
| valuation_method | string | No | How valued |
| cgt_if_sold | currency | No | |
| net_value | currency | Calculated | |

### 2.12 Directorships
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| directorships | text | No | Other directorships in last 12 months |

### 2.13 Pensions (Array)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| pension_provider | string | Yes | |
| pension_type | enum | Yes | 'defined_benefit', 'defined_contribution', 'state_additional', 'personal' |
| pension_reference | string | Yes | |
| cetv | currency | Yes | Cash Equivalent Transfer Value |
| cetv_date | date | Yes | Must be within 12 months |
| in_payment | boolean | Yes | Already receiving pension |
| payment_amount | currency | No | If in payment |
| payment_frequency | enum | No | |

### 2.14-2.19 Income Details

#### Employment Income
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| employer_name | string | No | |
| job_title | string | No | |
| gross_annual_salary | currency | No | |
| net_monthly_income | currency | No | |
| bonuses | currency | No | Annual |
| benefits_in_kind | text | No | Car, health insurance, etc. |

#### Self-Employment Income
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| self_employed | boolean | Yes | |
| business_name | string | No | |
| net_profit_last_year | currency | No | |
| drawings_last_year | currency | No | |
| estimated_current_year | currency | No | |

#### Investment Income
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| dividend_income | currency | No | Annual |
| interest_income | currency | No | Annual |
| rental_income | currency | No | Annual |

#### State Benefits
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| benefits_received | array[enum] | No | 'universal_credit', 'child_benefit', 'disability', 'other' |
| benefits_amount | currency | No | Monthly total |

#### Other Income
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| other_income_description | string | No | |
| other_income_amount | currency | No | |

### 2.20 Summary of Assets
| Field | Type | Calculated |
|-------|------|------------|
| total_property | currency | Sum of all property interests |
| total_bank_accounts | currency | |
| total_investments | currency | |
| total_life_insurance | currency | |
| total_monies_owed | currency | |
| total_cash | currency | |
| total_personal_property | currency | |
| total_business_interests | currency | |
| total_pensions_cetv | currency | |
| **gross_assets** | currency | Sum of above |
| total_liabilities | currency | |
| **net_assets** | currency | Gross - liabilities |

---

## Section 3: Financial Requirements

### 3.1 Income Needs (Budget)

#### Your Monthly Expenses
| Category | Field | Type |
|----------|-------|------|
| Housing | mortgage_rent | currency |
| Housing | council_tax | currency |
| Housing | utilities_gas_electric | currency |
| Housing | water_rates | currency |
| Housing | building_insurance | currency |
| Housing | contents_insurance | currency |
| Housing | repairs_maintenance | currency |
| Transport | car_finance | currency |
| Transport | car_insurance | currency |
| Transport | fuel | currency |
| Transport | repairs_mot | currency |
| Transport | public_transport | currency |
| Living | food_groceries | currency |
| Living | clothing | currency |
| Living | toiletries_haircare | currency |
| Living | medical_dental | currency |
| Living | phone_internet | currency |
| Living | tv_subscriptions | currency |
| Leisure | holidays | currency |
| Leisure | entertainment | currency |
| Leisure | hobbies | currency |
| Financial | pension_contributions | currency |
| Financial | life_insurance | currency |
| Financial | savings | currency |
| Financial | debt_repayments | currency |
| Other | other_expenses | currency |
| **Total** | total_monthly_needs | currency |

#### Children's Monthly Expenses (if applicable)
| Field | Type |
|-------|------|
| school_fees | currency |
| childcare | currency |
| children_clothing | currency |
| children_activities | currency |
| children_other | currency |
| **Total** | children_total_monthly | currency |

### 3.2 Capital Needs
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| housing_needs | text | No | What housing do you need |
| housing_budget | currency | No | Can be 'to be confirmed' |
| furniture_needs | currency | No | |
| car_needs | currency | No | |
| other_capital_needs | text | No | |

---

## Section 4: Other Information

### 4.1 Significant Changes
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| changes_last_12_months | text | No | Significant changes to assets/income |
| anticipated_changes | text | No | Expected future changes |

### 4.2 Contributions
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| contributions_made | text | No | Financial/non-financial contributions to family |

### 4.3 Standard of Living
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| standard_of_living | text | No | Description of lifestyle during marriage |

### 4.4 Conduct
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| conduct_relevant | boolean | Yes | Is conduct relevant to financial outcome |
| conduct_details | text | No | Only for exceptional cases (abuse, dissipation) |

### 4.5 Other Relevant Information
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| other_information | text | No | Anything else the court should know |

---

## Section 5: Order Sought

### 5.1 Settlement Proposal
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| seeking_maintenance | boolean | Yes | Periodical payments |
| maintenance_sought | currency | No | Amount if yes |
| maintenance_term | enum | No | 'joint_lives', 'fixed_term', 'nominal' |
| seeking_lump_sum | boolean | Yes | |
| lump_sum_amount | currency | No | |
| seeking_property_transfer | boolean | Yes | |
| property_transfer_details | text | No | |
| seeking_pension_share | boolean | Yes | |
| pension_share_details | text | No | |
| clean_break | boolean | Yes | No ongoing claims |

### 5.2 Statement of Truth
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| declaration_understood | boolean | Yes | Understands duty of full disclosure |
| declaration_truthful | boolean | Yes | Information is true |
| signature_date | date | Yes | |

---

## Document Requirements

### Required Attachments
| Section | Documents Required |
|---------|-------------------|
| 2.1-2.2 | Property valuations (within 6 months), mortgage statements |
| 2.3 | 12 months bank statements for ALL accounts |
| 2.4 | Investment valuations |
| 2.5 | Life insurance surrender values |
| 2.11 | Last 2 years business accounts, tax returns |
| 2.13 | Pension CETV statements (within 12 months) |
| 2.14+ | 12 months payslips, P60, or self-employment accounts |

---

## AI Conversation Flow Mapping

### Suggested Interview Phases

**Phase 1: Introduction & Personal (10-15 questions)**
- Sections 1.1-1.9
- Establish basics, verify understanding of process

**Phase 2: Family & Children (5-10 questions)**
- Sections 1.4-1.7 (if applicable)
- Child arrangements, education, maintenance

**Phase 3: Property (5-15 questions per property)**
- Sections 2.1-2.2
- Main home, then other properties

**Phase 4: Financial Assets (10-20 questions)**
- Sections 2.3-2.8
- Accounts, investments, insurance, valuables

**Phase 5: Debts & Liabilities (5-10 questions)**
- Sections 2.9-2.10
- All debts, CGT exposure

**Phase 6: Business Interests (5-15 questions if applicable)**
- Sections 2.11-2.12
- Complex area, flag for solicitor review if significant

**Phase 7: Pensions (3-5 questions per pension)**
- Section 2.13
- Critical: ensure CETVs obtained

**Phase 8: Income (10-15 questions)**
- Sections 2.14-2.19
- Employment, self-employment, other income

**Phase 9: Budget & Needs (20-30 questions)**
- Section 3
- Monthly expenses, capital needs

**Phase 10: Narrative & Context (5-10 questions)**
- Section 4
- Changes, contributions, standard of living

**Phase 11: Settlement Goals (5-10 questions)**
- Section 5
- What outcome are you hoping for

**Phase 12: Forensic Audit & Validation (The "Solicitor Simulator")**
- **Internal Step**: AI analyzes full JSON state
- **Checks**:
    - Income vs. Expense deficit check
    - Asset listing vs. Bank Statement transfers
    - Narrative vs. Evidence consistency
- **Output**: Mandatory "Fix List" before finalization

**Phase 13: Review & Documents**
- Summary review
- Document checklist

---

## Complexity Flags

Flag for solicitor review if any of:
- [ ] Business interests valued over £50k
- [ ] Multiple pensions with complex sharing
- [ ] Overseas assets
- [ ] Trust interests
- [ ] Conduct allegations
- [ ] Significant income disparity
- [ ] Complex property ownership (shared ownership, trust)
- [ ] Significant dissipation allegations
- [ ] Non-disclosure concerns

---

*Document created: 2025-12-19*
*Sources: [Gov.uk](https://www.gov.uk/government/publications/form-e-financial-statement-for-a-financial-order-matrimonial-causes-act-1973-civil-partnership-act-2004-for-financial-relief-after-an-overseas), [Wikivorce](https://divorce.wikivorce.com/library/divorce-finances/form-e.html), [Cripps](https://www.cripps.co.uk/thinking/how-to-fill-in-your-form-e-tips-tricks-and-points-to-consider/), [AdviceNow](https://www.advicenow.org.uk/get-help/family-and-children/divorce-and-separation/how-fill-your-financial-statement-form-e)*
