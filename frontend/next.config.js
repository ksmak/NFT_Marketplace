/** @type {import('next').NextConfig} */
const nextConfig = {
    env: {
        FRONTEND_HOST: 'http://localhost:3000',
        BACKEND_HOST: 'http://localhost:8000',
        EMAIL_ADDRESS: 'ksmakov@gmail.com',
        SENDGRID_API_KEY: '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',
        SITE_NAME: 'Marketplace Art',
    },
}

module.exports = nextConfig
