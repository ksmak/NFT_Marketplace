export default async function handler(req, res) {
    if (req.method == 'GET') {
        const { id, token } = req.query;
        const response = await fetch(`${process.env.BACKEND_HOST}/api/users/${id}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': `Bearer ${token}`
            },
        })

        const result = await response.json();

        res.status(response.status).json(result);

    } else {
        const data = JSON.parse(req.body);

        const response = await fetch(`${process.env.BACKEND_HOST}/api/users/${data.id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': `Bearer ${data.token}`
            },
            body: JSON.stringify(data.user),
        })

        const result = await response.json();

        res.status(response.status).json(result);
    }
}