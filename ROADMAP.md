# 🗺️ Project Roadmap

This roadmap outlines key features and improvements planned for the Informal Business Management System. It helps contributors and users understand where the project is headed and how they can participate.

---

## ✅ Completed Milestones

- [x] Core domain models implemented: InventoryItem, Order, Payment
- [x] Service and repository layers developed
- [x] REST API endpoints built using FastAPI
- [x] Unit testing and GitHub Actions CI/CD pipeline
- [x] Basic Swagger documentation enabled
- [x] CONTRIBUTING.md, LICENSE, and CODE_OF_CONDUCT.md added

---

## 🚧 In Progress

- [ ] Refactor response models to support localization
- [ ] Add pagination and filtering support for inventory API
- [ ] Expand test coverage and add test reports to CI

---

## 🧩 Planned Features

### 🔐 Authentication & Security
- [ ] Implement JWT-based user authentication
- [ ] Role-based access control (Admin, Vendor)

### 📦 Inventory Enhancements
- [ ] Barcode scanning integration for stock updates
- [ ] CSV and Excel export/import of inventory data

### 💸 Payment and Finance
- [ ] Add retry mechanism to PaymentService
- [ ] Integrate mobile money APIs for cashless transactions

### 📈 Analytics and Dashboard
- [ ] Real-time dashboard using Vega or Plotly
- [ ] Generate PDF reports (daily/weekly sales summaries)

### 📤 Notifications
- [ ] WhatsApp and SMS alert integration (via Twilio or WhatsApp Cloud API)
- [ ] Email receipts for orders

### 🌐 Offline and Accessibility
- [ ] Add PWA (Progressive Web App) support for offline mode
- [ ] Mobile-first UI refinement

---

## 📝 Ideas for Community Contributions

- Add API versioning support
- Translate Swagger docs into isiXhosa/isiZulu
- Improve database indexing for faster search
- Add audit logs for all actions (create/update/delete)

---

We welcome feature suggestions and issue submissions via GitHub Issues. Please label them accordingly (e.g., `feature-request` or `discussion`).
