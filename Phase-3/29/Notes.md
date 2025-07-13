### Answer

1.  - Done
    - 1. **Weekly Signups** - We can see spikes on week 9 and 18 and increasing
      2. **Active Users** - We can see spikes in week 3 and 14, noticeable dip in week 14-15 and stay lower ~ week 16-18
      3. **Support Tickets** - Spikes in week 9 and week 12-14
      4. **Crash Rate (%)** - A gradual upward drift begins around Week 15–16

2.  - Crash Rate - Initially it is low but after week 13, it stays elevated. 
    - Week 13
    - Hypothesis for Root Cause :
        1. Backend changes or updates post week 13 could've introduced failures
        2. Active users started to drop after 1 week
        3. Support tickets spike in between week 13 to 14, maybe because user start noticing

3.  - | Metric          | Alert Condition                        | Why?                  |
      | --------------- | -------------------------------------- | --------------------- |
      | Crash Rate (%)  | > 1.5% OR increase > 0.2% over 2 weeks | Early backend failure |
      | Active Users    | Drop > 10% over 2 weeks                | Retention risk        |
      | Support Tickets | Spike > 30% vs previous week           | Usability/breakage    |
      | Signups         | Drop > 20% vs 4-week average           | Marketing drop        |

    - 1. Time Series Charts
      2. KPI Cards
      3. Anomaly Alerts

---

- **Why do teams often miss early warning signs?**  
Neglegence or sometime miss to consider all factors which are equally relevant and correlate with each othr to gain insights.

- **How would you test if a drop is temporary vs. long-term decay?**  
If all the features equally dip and stays or decrease more, it would be a long-term decay.  
But if only 1 or few features showing decay without affecting the others, it could be a temporary decay

- **What’s the tradeoff between reacting early and over-alerting?**  
Reacting early helps catch issues before users churn, but it risks false alarms that fatigue teams and lead to ignored alerts. 

---
---


