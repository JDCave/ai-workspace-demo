# Incident Communication Template

## Slack Channel: #incident-response

### Incident Start
```
🚨 INCIDENT [SEV<N>]
────────────────────
Service:    <service-name>
Status:     INVESTIGATING
Started:    <timestamp UTC>
Impact:     <description of user/business impact>
On-call:    @<on-call-engineer>
Next Update: <timestamp - typically 15-30 min>
```

### Incident Update
```
🔄 INCIDENT UPDATE [SEV<N>]
────────────────────
Service:    <service-name>
Status:     <INVESTIGATING|MITIGATING|MONITORING|RESOLVED>
Update:     <what has been found/done>
Impact:     <updated impact description>
Next Update: <timestamp>
```

### Incident Resolved
```
✅ INCIDENT RESOLVED [SEV<N>]
────────────────────
Service:    <service-name>
Duration:   <total duration>
Root Cause: <brief description>
Resolution: <what fixed it>
Follow-up:  Post-mortem scheduled for <date/time>
```

## Stakeholder Email Template

**Subject:** [INCIDENT] <Service> - <Brief Description>

```
Hi team,

We experienced an incident affecting <service>.

Incident Details:
- Start Time: <UTC timestamp>
- End Time: <UTC timestamp>
- Duration: <duration>
- Severity: SEV<N>
- Impact: <number of users/transactions affected>

Root Cause:
<description>

Resolution:
<what was done to fix>

Action Items:
1. <action item 1>
2. <action item 2>

Post-mortem will be scheduled within 48 hours.

Regards,
<on-call engineer>
```
