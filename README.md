# AI_C

DỰ ÁN: NỀN TẢNG THEO DÕI DỮ LIỆU THỊ TRƯỜNG CRYPTO TỪ OKX
=========================================================

I. TỔNG QUAN DỰ ÁN:
-------------------
- Xây dựng website lấy dữ liệu real-time từ OKX.com
- Lưu dữ liệu vào database (MariaDB/PostgreSQL)
- Hiển thị dữ liệu dạng biểu đồ theo thời gian thực

II. KIẾN TRÚC HỆ THỐNG:
-----------------------
- Backend: Node.js (Express.js hoặc Fastify)
- Database: MariaDB hoặc PostgreSQL
- Cache: Redis
- Queue/Worker: Bull Queue
- Frontend: React (Next.js)
- Chart: TradingView Lightweight Charts
- Hệ điều hành triển khai: Linux Manjaro
- Triển khai: Docker, Docker Compose
- Monitoring: Grafana, Prometheus
- Bảo mật: HTTPS (Let's Encrypt), JWT, Helmet, CORS
- Testing: Jest, Cypress

III. CẤU TRÚC THƯ MỤC GỢI Ý:
----------------------------
project-root/
├── backend/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── workers/
│   ├── index.js
│   ├── package.json
│   └── Dockerfile
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── public/
│   ├── styles/
│   ├── package.json
│   └── Dockerfile
├── database/
│   └── init.sql
├── docker-compose.yml
└── README.md

IV. CÁC BƯỚC TRIỂN KHAI:
------------------------
Bước 1: Chuẩn bị môi trường trên Linux Manjaro
- Cài đặt Node.js, MariaDB/PostgreSQL, Redis, Docker, Docker Compose.

Bước 2: Xây dựng Backend
- Thiết lập backend API với Express/Fastify
- Xây dựng kết nối database và Redis cache
- Xây dựng cơ chế lấy dữ liệu real-time từ OKX API
- Xây dựng Queue xử lý dữ liệu

Bước 3: Xây dựng Frontend
- Cài đặt React Next.js
- Kết nối với backend
- Tích hợp biểu đồ TradingView Lightweight Charts

Bước 4: Cài đặt Monitoring và Logging
- Tích hợp Grafana & Prometheus
- Logging chi tiết ứng dụng (Winston, Morgan)

Bước 5: Bảo mật & Testing
- Triển khai HTTPS (Let's Encrypt)
- Xây dựng JWT Authentication
- Bảo vệ ứng dụng bằng Helmet & CORS
- Xây dựng unit test (Jest) và E2E test (Cypress)

Bước 6: Triển khai & CI/CD
- Dockerize dự án với Docker Compose
- Triển khai tự động lên server
- Setup GitHub Action hoặc GitLab CI/CD pipeline

V. CAM KẾT DỰ ÁN:
------------------
- Đảm bảo hiệu năng cao, bảo mật tốt nhất.
- Liên tục hỗ trợ kỹ thuật.
- Cập nhật tài liệu rõ ràng theo từng thay đổi trên GitHub.

VI. PHỤ LỤC:
------------
Các tài liệu hướng dẫn chi tiết được cập nhật liên tục trong README.md và trên GitHub Wiki của dự án.

