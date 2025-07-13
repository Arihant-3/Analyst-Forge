### Answer

1.  1. Daily Active Users (DAU)
    Pattern: Fairly stable with normal fluctuations around 790 users/day.  
    Insight: No significant drop or spike, indicating steady user engagement. A healthy baseline.
    
    2. Retention Rate
    Pattern: Oscillates between 0.3 and 0.5, centered around ~0.4.
    Insight: This variability is typical in early product stages. If retention dips consistently below 0.35, it could indicate friction in user experience.

    3. Bug Reports
    Pattern: Mostly stable around 4–6 bug reports/day, some minor spikes.
    Insight: The volume is moderate.

    4. Crash Rate (%)
    Pattern: Varies daily between 0.2% and 1.5%. And average bug report is 0.8% per day.
    Insight: A few spikes may warrant investigation. 48% of the crash reports are above average which is quite concerning.

2.  - Done
    - Bug reports and New sign ups are correlated.  
      DAU and crash rate are correlated

3.  - Fix 1 (Infra): Optimize backend crash recovery to reduce crash rate spikes.  
      Fix 2 (UX): Improve onboarding flow to increase new signups and retention.
    - Experiment - Push notifications to boost daily engagement and retention.

---

- **What does a healthy launch look like?**  
DAU is increasing, bug reports should stable, crash rate should be minimum, retention rate should always be greater that averge over time. 

- **What metric matters most in the first 90 days?**  
Bug reports because the more we get to know the flaws, the more we improve that by focus on that one problem.

- **What hidden problem could hurt growth?**  
The hidden problem is technical instability (bugs, crashes) undermining user trust and loyalty, especially for new users — even if DAU looks healthy short-term


