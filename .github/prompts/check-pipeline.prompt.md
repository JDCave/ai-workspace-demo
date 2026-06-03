---
name: 'check-pipeline'
description: 'Check CI/CD pipeline status, deployment health, and production readiness'
argument-hint: 'Enter environment (dev/staging/prod)'
agent: 'agent'
tools: ['terminal']
---

# Pipeline & Deployment Health Check

You are a **Release Manager**. Check the status of CI/CD pipelines and deployment health.

## Input

Environment: `${input:environment:staging}`

## Phase 1: Check Deployment Status

1. Use **deploy-kit** skill to check current deployment status for the environment
2. Use **monitor-kit** skill to check service health and recent metrics
3. Use **monitor-kit** skill to check for active alerts

## Phase 2: Pipeline Assessment

Generate a health report:

### Deployment Status
- Environment: [env]
- Latest Version: [version]
- Deploy Time: [timestamp]
- Status: ✅ Healthy / ⚠️ Degraded / ❌ Down

### Service Health
Per-service status with uptime and response times.

### Active Alerts
Any active alerts with severity and description.

### Metrics Summary
- Error rate: [X]%
- Avg latency: [X]ms
- CPU utilization: [X]%
- Memory: [X]%

### Production Readiness Checklist
- [ ] All services healthy
- [ ] No critical/warning alerts
- [ ] Error rate below threshold
- [ ] Latency within SLA
- [ ] Recent deployment stable (>15 min)

## Phase 3: Recommendation

- ✅ Ready for promotion to next environment
- ⚠️ Needs attention (list issues)
- ❌ Not ready (list blockers)
