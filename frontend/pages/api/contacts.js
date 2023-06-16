const mail = require('@sendgrid/mail');

mail.setApiKey(process.env.SENDGRID_API_KEY);

export default async function handler(req, res) {
    const data = {
        to: req.body.email,
        from: process.env.EMAIL_ADDRESS,
        subject: req.body.subject,
        text: req.body.message,
        html: req.body.message,
    };

    await mail.send(data);

    res.status(200).json({ status: 'OK' });
}