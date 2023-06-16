export default async function handler(req, res) {
    const response = await fetch(`${process.env.BACKEND_HOST}/api/users/register/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        body: JSON.stringify(req.body),
    })

    const result = await response.json();

    res.status(response.status).json(result);
}