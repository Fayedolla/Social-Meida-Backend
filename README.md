# Social Media Backend

A comprehensive backend API for a social media platform built with modern web technologies.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

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
- **Database**: PostgreSQL
- **ORM**: Sequelize / Prisma
- **Authentication**: JWT (JSON Web Tokens)
- **File Upload**: Multer
- **Validation**: Express-validator / Joi
- **Security**: bcrypt, helmet, cors

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Node.js (v14 or higher)
- npm or yarn
- PostgreSQL (v12 or higher)
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

3. **Set up PostgreSQL database**

```bash
# Create a new database
createdb social_media

# Or using psql
psql -U postgres
CREATE DATABASE social_media;
```

## ⚙️ Configuration

1. **Create a `.env` file** in the root directory:

```env
# Server Configuration
PORT=5000
NODE_ENV=development

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=social_media
DB_USER=your_database_username
DB_PASSWORD=your_database_password

# Alternative: Database URL
DATABASE_URL=postgresql://username:password@localhost:5432/social_media

# JWT Configuration
JWT_SECRET=your_secret_key_here
JWT_EXPIRE=7d
JWT_REFRESH_SECRET=your_refresh_secret_here

# File Upload Configuration
MAX_FILE_SIZE=5242880
UPLOAD_PATH=./uploads

# Email Configuration (for password reset)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@example.com
EMAIL_PASSWORD=your_email_app_password

# Frontend URL (for CORS)
CLIENT_URL=http://localhost:3000

# Cloudinary (if using cloud storage)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

2. **Run database migrations**

```bash
# If using Sequelize
npx sequelize-cli db:migrate

# If using Prisma
npx prisma migrate dev
```

3. **Create necessary directories**

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
| POST | `/api/auth/refresh-token` | Refresh access token | No |

### User Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/users/:id` | Get user profile | Yes |
| PUT | `/api/users/:id` | Update user profile | Yes |
| DELETE | `/api/users/:id` | Delete user account | Yes |
| GET | `/api/users/search?q=query` | Search users | Yes |
| POST | `/api/users/:id/follow` | Follow user | Yes |
| DELETE | `/api/users/:id/unfollow` | Unfollow user | Yes |
| GET | `/api/users/:id/followers` | Get user followers | Yes |
| GET | `/api/users/:id/following` | Get users being followed | Yes |

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

### Example Requests

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

**Login User**
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
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
│   ├── database.js        # Database configuration
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
│   ├── Like.js
│   └── Notification.js
├── routes/
│   ├── authRoutes.js
│   ├── userRoutes.js
│   ├── postRoutes.js
│   └── commentRoutes.js
├── migrations/            # Database migrations
├── seeders/               # Database seeders
├── utils/
│   ├── generateToken.js
│   ├── sendEmail.js
│   └── validators.js
├── uploads/               # Uploaded files directory
├── .env                   # Environment variables (DO NOT COMMIT)
├── .env.example           # Example environment variables
├── .gitignore
├── package.json
├── server.js              # Entry point
└── README.md
```

## 🗄️ Database Schema

The application uses PostgreSQL with the following main tables:

- **users**: User account information
- **posts**: User posts and content
- **comments**: Comments on posts
- **likes**: Likes on posts and comments
- **follows**: User follow relationships
- **notifications**: User notifications

## 🧪 Testing

```bash
# Run tests
npm test

# Run tests with coverage
npm run test:coverage

# Run specific test file
npm test -- path/to/test/file
```

## 🔒 Security Features

- Password hashing with bcrypt
- JWT token authentication
- SQL injection prevention via parameterized queries
- XSS protection with helmet
- CORS configuration
- Rate limiting
- Input validation and sanitization

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Coding Standards

- Follow ESLint configuration
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Fayedolla**

- GitHub: [@Fayedolla](https://github.com/Fayedolla)

## 🙏 Acknowledgments

- Thanks to all contributors who have helped this project grow
- Inspired by modern social media platforms

## 📞 Support

For support, open an issue in the repository or contact the maintainers.

## 🚀 Deployment

### Using Heroku

```bash
heroku create your-app-name
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run npm run migrate
```

### Using Docker

```bash
docker build -t social-media-backend .
docker run -p 5000:5000 social-media-backend
```

---

**Happy Coding!** 🚀