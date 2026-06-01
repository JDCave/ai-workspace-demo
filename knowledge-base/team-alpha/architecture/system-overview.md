# Team Alpha - System Architecture Overview

## Services

### Payment Service
- **Stack**: Java 17, Spring Boot 3.x, PostgreSQL 15
- **Repository**: `gitlab.internal.com/team-alpha/payment-service`
- **Owner**: Backend Squad
- **Key APIs**:
  - `POST /api/v1/payments` — Create payment
  - `GET /api/v1/payments/{id}` — Get payment status
  - `POST /api/v1/payments/{id}/refund` — Process refund

### User Service
- **Stack**: Python 3.11, FastAPI, MongoDB 7
- **Repository**: `gitlab.internal.com/team-alpha/user-service`
- **Owner**: Identity Squad
- **Key APIs**:
  - `POST /api/v1/users` — Register user
  - `GET /api/v1/users/{id}` — Get user profile
  - `PUT /api/v1/users/{id}` — Update profile

### Notification Service
- **Stack**: Node.js 20, Express, Redis 7
- **Repository**: `gitlab.internal.com/team-alpha/notification-service`
- **Owner**: Platform Squad
- **Channels**: Email, SMS, Push, In-App

## Architecture Diagram

```
┌──────────┐     ┌──────────┐     ┌──────────────┐
│  Gateway  │────▶│  Payment  │────▶│  PostgreSQL   │
│  (Kong)   │     │  Service  │     │               │
└──────────┘     └──────────┘     └──────────────┘
     │           ┌──────────┐     ┌──────────────┐
     ├──────────▶│   User    │────▶│   MongoDB    │
     │           │  Service  │     │               │
     │           └──────────┘     └──────────────┘
     │           ┌──────────┐     ┌──────────────┐
     └──────────▶│Notification│───▶│    Redis     │
                 │  Service  │     │               │
                 └──────────┘     └──────────────┘
```

## Infrastructure
- **Cloud**: AWS (ap-southeast-1)
- **Orchestration**: Kubernetes (EKS)
- **CI/CD**: GitLab CI + ArgoCD
- **Monitoring**: Grafana + Prometheus
- **Logging**: ELK Stack
- **Alerting**: PagerDuty

## Key Contacts
- Team Lead: Refer to Confluence team page
- On-call: Check PagerDuty schedule
- Architecture: Architecture Review Board (weekly Tuesday 2PM)
