import { NextRequest, NextResponse } from "next/server";

const mail = require('@sendgrid/mail');

mail.setApiKey(process.env.SENDGRID_API_KEY);

export default async function handler(req: NextRequest, res: NextResponse) {
    const body = req.body;

    const data = {
        to: body.email,
        from: process.env.EMAIL_ADDRESS,
        subject: body.subject,
        text: body.message,
        html: body.message,
    };

    await mail.send(data);

    res.status(200).json({ status: 'OK' });
}