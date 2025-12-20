You've raised a very good point about the Cost of Sales (COS), especially in Year 1. Let me clarify how it's calculated based on the assumptions and the parallelization model.

### How COS is Calculated

In this financial model, the Cost of Sales (COS) is primarily driven by the **"Fully Loaded Consultant Cost"** and the **"Number of Hired Consultants Required"**.

1.  **Fully Loaded Consultant Cost:** This is assumed to be **£5,000 per FTE (Full-Time Equivalent) per month**. This figure is intended to cover not just the consultant's salary, but also benefits, employer taxes, and a portion of direct overheads associated with their role. This cost applies only to *hired* consultants.
2.  **Consultant Capacity & Load Units:**
    *   Each consultant (including the founder) is assumed to have a total capacity of **4 "load units"**.
    *   Each client, depending on their subscription tier, consumes a certain number of these load units:
        *   Essentials Client: 1 load unit
        *   Growth Client: 2 load units
        *   Transformation Client: 3 load units
        *   Technical Co-Founder Client: 2 load units
3.  **Number of Hired Consultants Required:**
    *   In Year 1, the founder acts as the sole consultant. For the purpose of cash flow projections, the founder's time is *not* accounted for as a direct cash Cost of Services (COS). This assumes the founder is either not taking a salary or their salary is covered by initial investment/equity and not a direct operational expense impacting COS.
    *   Additional consultants are hired only when the total client load exceeds the capacity of the *existing* consultants (including the founder's capacity).
    *   The calculation is: `Ceiling((Total Load Units - Founder's Capacity) / Hired Consultant's Capacity)`.

### Why COS Appears Low (or Zero) in Year 1

Let's look at Year 1 specifically with the founder's involvement:

*   **Clients:** 2 clients (1 Essentials, 1 Growth)
*   **Total Load Units:**
    *   1 Essentials client * 1 load unit/client = 1 load unit
    *   1 Growth client * 2 load units/client = 2 load units
    *   Total = 1 + 2 = **3 load units**
*   **Hired Consultants Required:** Since the total load units (3) are less than or equal to the founder's capacity (4), no additional consultants are hired in Year 1.
*   **Calculated COS:** 0 hired consultants * £5,000/month * 12 months = **£0**.

The COS is zero in Year 1 because the founder is handling all client work within their assumed capacity, and their time is not being expensed as a direct cash cost of services in this model.

As the business grows and the total client load exceeds the founder's capacity, additional consultants will be hired, and their costs will then contribute to the COS. This model reflects the initial bootstrapping phase where founder effort directly contributes to service delivery without immediate cash outlay for that specific role.
