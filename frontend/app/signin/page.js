'use client'
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function SignIn() {
    const router = useRouter();

    const [inputs, setInputs] = useState({});
    const [error, setError] = useState();

    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({ ...values, [name]: value }))
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        const response = await fetch(`${process.env.FRONTEND_HOST}/api/user/login/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(inputs)
        });

        if (!response.ok) {
            setError('Error! Invalid email or password.');
            return;
        }

        const result = await response.json();

        sessionStorage.setItem('id', result.id);
        sessionStorage.setItem('username', result.username);
        sessionStorage.setItem('accessToken', result.access);
        sessionStorage.setItem('refreshToken', result.refresh);

        router.push('/');
    };

    return (
        <div className="mb-auto">
            <h1 className="text-center text-5xl p-10">Sign In</h1>
            <div className="mr-auto ml-auto border-2 w-2/5 rounded-md bg-gray-100">
                <form onSubmit={handleSubmit}>
                    <div className="p-5 flex justify-between">
                        <label htmlFor="email">Email</label>
                        <input className="border-2 rounded-md border-black p-1" type="email" name="email" id="email" onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="password">Password</label>
                        <input className="border-2 rounded-md border-black p-1" type="password" name="password" id="password" onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-center">
                        <button className="border-2 rounded-md border-black p-2 w-64 bg-gray-300 hover:bg-gray-700 hover:text-white" type="Submit">Sign In</button>
                    </div>
                    <div className="p-5 flex justify-between text-red-500">
                        {error}
                    </div>
                </form>
            </div >
        </div >
    );
}
