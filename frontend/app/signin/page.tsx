'use client'
import useSessionStorage from "@/components/useSessionStorage";
import { useRouter } from "next/navigation";
import { useState } from "react";

const SignIn = () => {
    const router = useRouter();
    const [inputs, setInputs] = useState({});
    const [error, setError] = useState();
    const [username, setUsername] = useSessionStorage('username', '');
    const [accessToken, setAccessToken] = useSessionStorage('accessToken', '');
    const [refreshToken, setRefreshToken] = useSessionStorage('refreshToken', '');

    const handleChange = (event: any) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({ ...values, [name]: value }))
    };

    const handleSubmit = async (event: any) => {
        event.preventDefault();

        const response = await fetch("http://127.0.0.1:8000/api/token/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inputs)
        });

        const result = await response.json();

        if (!response.ok) {
            setError('Error! Email or password incorrect.');
            return;
        }

        console.log(result);

        setUsername(inputs.email);
        setAccessToken(result.access);
        setRefreshToken(result.refresh);

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


export default SignIn;