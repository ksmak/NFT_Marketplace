'use client'
import { useEffect, useState } from "react";

export default function ProfileForm({ params }) {
    const [userId, setUserId] = useState();
    const [token, setToken] = useState(null);
    const [user, setUser] = useState(params.user);
    const [error, setError] = useState();

    useEffect(() => {
        const getUser = async (id, token) => {
            const response = await fetch(`${process.env.FRONTEND_HOST}/api/user/profile?id=${id}&token=${token}`, {
                method: 'GET'
            });

            const data = await response.json();

            setUser(data.result);
        };

        const userId = sessionStorage.getItem('id');
        const accessToken = sessionStorage.getItem('accessToken');

        setUserId(userId);
        setToken(accessToken);

        if (!userId && !accessToken) {
            setError('User profile not found.');
            return;
        };

        getUser(userId, accessToken);
    }, []);

    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setUser(values => ({ ...values, [name]: value }))
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        const data = {
            id: userId,
            token: token,
            user: user
        }

        const response = await fetch(`${process.env.FRONTEND_HOST}/api/user/profile`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(data),
        })

        if (!response.ok) {
            setError('Error! Profile not saved.');
        }
    };

    return (
        <div className="mb-auto">
            <h1 className="text-center text-5xl p-5">Profile</h1>
            <div className="mr-auto ml-auto border-2 w-3/5 rounded-md bg-gray-100">
                <form onSubmit={handleSubmit}>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="email">Email</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="email" name="email" id="email" value={user && user.email ? user.email : null} disabled />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="surname">Surname</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="text" name="surname" id="surname" value={user && user.surname ? user.surname : null} onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="name">Name</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="text" name="name" id="name" value={user && user.name ? user.name : null} onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="patronymic">Patronymic</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="text" name="patronymic" id="patronymic" value={user && user.patronymic ? user.patronymic : null} onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="password">Password</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="password" name="password" id="password" value={user && user.password ? user.password : null} onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="wallet">Wallet</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="text" name="wallet" id="wallet" value={user && user.wallet ? user.wallet : null} onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-center">
                        <button className="border-2 rounded-md border-black p-2 w-64 bg-gray-300 hover:bg-gray-700 hover:text-white" type="Submit">Save</button>
                    </div>
                    <div className="p-5 flex justify-between text-red-500">
                        {error}
                    </div>
                </form>
            </div >
        </div >
    );
}
