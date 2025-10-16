# Social Media Backend

A comprehensive backend API for a social media platform built with modern web technologies.

## 📋 Table of Contents

- [Social Media Backend](#social-media-backend)
  - [📋 Table of Contents](#-table-of-contents)
  - [🌟 Overview](#-overview)
  - [✨ Features](#-features)
  - [🛠 Tech Stack](#-tech-stack)
  - [📋 Prerequisites](#-prerequisites)
  - [🚀 Installation](#-installation)
  - [⚙️ Configuration](#️-configuration)
  - [🏃 Running the Application](#-running-the-application)
    - [Development Mode](#development-mode)
    - [Production Mode](#production-mode)
  - [📚 API Documentation](#-api-documentation)
    - [Authentication Endpoints](#authentication-endpoints)
    - [User Endpoints](#user-endpoints)
    - [Post Endpoints](#post-endpoints)
    - [Comment Endpoints](#comment-endpoints)
    - [Example Request](#example-request)
  - [📁 Project Structure](#-project-structure)
  - [🧪 Testing](#-testing)
  - [🤝 Contributing](#-contributing)
  - [📝 License](#-license)
  - [👤 Author](#-author)
  - [🙏 Acknowledgments](#-acknowledgments)
  - [📞 Support](#-support)

## 🌟 Overview

This project provides a robust REST API for a social media application, handling user authentication, posts, comments, likes, friendships, and real-time notifications.

## ✨ Features

- **User Authentication & Authorization**
  - User registration and login
  - JWT-based authentication
  - Password encryption
  - Password reset functionality

- **User Management**
  - User profiles with customizable information
  - Profile picture upload
  - Follow/Unfollow users
  - User search functionality

- **Post Management**
  - Create, read, update, and delete posts
  - Image/video upload support
  - Post likes and reactions
  - Post sharing

- **Comments & Interactions**
  - Comment on posts
  - Nested replies
  - Like/unlike comments
  - Delete comments

- **Social Features**
  - Friend requests (send, accept, decline)
  - News feed algorithm
  - User notifications
  - Privacy settings

- **Real-time Features**
  - Live notifications
  - Chat messaging (if applicable)

## 🛠 Tech Stack

- **Runtime**: Node.js
- **Framework**: Express.js
- **Database**: MongoDB
- **ODM**: Mongoose
- **Authentication**: JWT (JSON Web Tokens)
- **File Upload**: Multer
- **Validation**: Express-validator / Joi
- **Security**: bcrypt, helmet, cors

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Node.js (v14 or higher)
- npm or yarn
- MongoDB (local or Atlas account)
- Git

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Fayedolla/Social-Meida-Backend.git
cd Social-Meida-Backend
```

2. **Install dependencies**

```bash
npm install
# or
yarn install
```

## ⚙️ Configuration

1. **Create a `.env` file** in the root directory:

```env
# Server Configuration
PORT=5000
NODE_ENV=development

# Database
MONGODB_URI=mongodb://localhost:27017/social-media
# or for MongoDB Atlas:
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/social-media

# JWT Secret
JWT_SECRET=your_jwt_secret_key_here
JWT_EXPIRE=7d

# File Upload
MAX_FILE_SIZE=5242880
UPLOAD_PATH=./uploads

# Email Configuration (for password reset)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-email-password

# Frontend URL (for CORS)
CLIENT_URL=http://localhost:3000
```

2. **Create necessary directories**

```bash
mkdir uploads
mkdir uploads/profiles
mkdir uploads/posts
```

## 🏃 Running the Application

### Development Mode

```bash
npm run dev
# or
yarn dev
```

### Production Mode

```bash
npm start
# or
yarn start
```

The server will start on `http://localhost:5000` (or your configured PORT).

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register` | Register new user | No |
| POST | `/api/auth/login` | Login user | No |
| GET | `/api/auth/me` | Get current user | Yes |
| POST | `/api/auth/forgot-password` | Request password reset | No |
| PUT | `/api/auth/reset-password/:token` | Reset password | No |

### User Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/users/:id` | Get user profile | Yes |
| PUT | `/api/users/:id` | Update user profile | Yes |
| DELETE | `/api/users/:id` | Delete user account | Yes |
| GET | `/api/users/search?q=query` | Search users | Yes |
| POST | `/api/users/:id/follow` | Follow user | Yes |
| DELETE | `/api/users/:id/unfollow` | Unfollow user | Yes |

### Post Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/posts` | Get all posts (feed) | Yes |
| GET | `/api/posts/:id` | Get single post | Yes |
| POST | `/api/posts` | Create new post | Yes |
| PUT | `/api/posts/:id` | Update post | Yes |
| DELETE | `/api/posts/:id` | Delete post | Yes |
| POST | `/api/posts/:id/like` | Like/Unlike post | Yes |
| GET | `/api/posts/user/:userId` | Get user's posts | Yes |

### Comment Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/posts/:postId/comments` | Get post comments | Yes |
| POST | `/api/posts/:postId/comments` | Add comment | Yes |
| PUT | `/api/comments/:id` | Update comment | Yes |
| DELETE | `/api/comments/:id` | Delete comment | Yes |
| POST | `/api/comments/:id/like` | Like comment | Yes |

### Example Request

**Register User**
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

**Create Post (with authentication)**
```bash
curl -X POST http://localhost:5000/api/posts \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "content": "Hello World!",
    "visibility": "public"
  }'
```

## 📁 Project Structure

```
social-media-backend/
├── config/
│   ├── db.js              # Database configuration
│   └── cloudinary.js      # File upload configuration
├── controllers/
│   ├── authController.js
│   ├── userController.js
│   ├── postController.js
│   └── commentController.js
├── middleware/
│   ├── auth.js            # Authentication middleware
│   ├── error.js           # Error handling middleware
│   └── upload.js          # File upload middleware
├── models/
│   ├── User.js
│   ├── Post.js
│   ├── Comment.js
│   └── Notification.js
├── routes/
│   ├── authRoutes.js
│   ├── userRoutes.js
│   ├── postRoutes.js
│   └── commentRoutes.js
├── utils/
│   ├── generateToken.js
│   ├── sendEmail.js
│   └── validators.js
├── uploads/               # Uploaded files directory
├── .env                   # Environment variables
├── .gitignore
├── package.json
├── server.js              # Entry point
└── README.md
```

## 🧪 Testing

```bash
# Run tests
npm test

# Run tests with coverage
npm run test:coverage
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Fayedolla**

- GitHub: [@Fayedolla](https://github.com/Fayedolla)

## 🙏 Acknowledgments

- Thanks to all contributors who have helped this project grow
- Inspired by modern social media platforms

## 📞 Support

For support, email fayeda660@gmail.com or open an issue in the repository.

---

**Happy Coding!** 🚀