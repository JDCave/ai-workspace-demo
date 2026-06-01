# Incident Response Runbook - Payment Service

## Overview
Standard operating procedure for Payment Service production incidents.

## Prerequisites
- VPN access to production network
- Kubernetes CLI (`kubectl`) configured for prod cluster
- PagerDuty account for alert acknowledgment

## Common Issues

### Payment Processing Failures

**Symptoms:**
- High error rate on `POST /api/v1/payments`
- Timeouts in payment gateway responses
- Users reporting "Payment failed" errors

**Diagnosis:**
```bash
# Check pod health
kubectl get pods -n payment-prod -l app=payment-service

# Check recent logs
kubectl logs -n payment-prod deployment/payment-service --tail=100

# Check payment gateway connectivity
curl -s https://payment-gateway.internal/health
```

**Resolution:**
1. Check if payment gateway is responding (status page)
2. If gateway is down: enable circuit breaker, route to backup gateway
3. If database issue: check PostgreSQL replication status
4. Restart pods if needed: `kubectl rollout restart deployment/payment-service -n payment-prod`

### Database Connection Pool Exhaustion

**Symptoms:**
- Slow API responses (>5s)
- "Connection pool exhausted" in logs
- Increasing number of 503 errors

**Diagnosis:**
```bash
# Check active connections
kubectl exec -n payment-prod deployment/payment-service -- \
  python -c "import psutil; print(psutil.net_connections())"

# Check PostgreSQL connections
psql -h $DB_HOST -U admin -c "SELECT count(*) FROM pg_stat_activity;"
```

**Resolution:**
1. Kill idle connections: `SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state='idle' AND query_start < now() - interval '10 minutes';`
2. Increase pool size if persistent (config change requires deployment)
3. Scale horizontally: `kubectl scale deployment/payment-service --replicas=5 -n payment-prod`

## Escalation
- **L1**: On-call engineer (15 min response)
- **L2**: Payment Service owner (30 min)
- **L3**: Engineering Manager
- **External**: Payment gateway vendor support

## Post-Incident Checklist
- [ ] Root cause identified
- [ ] Fix deployed and verified
- [ ] Post-mortem scheduled within 48 hours
- [ ] Runbook updated if new scenario discovered
- [ ] Monitoring/alerting improved if gap found
