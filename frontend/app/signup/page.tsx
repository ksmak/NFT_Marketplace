'use client'
import { useRouter } from "next/navigation";
import { useState } from "react";

const SignUp = () => {
    const router = useRouter();
    const [inputs, setInputs] = useState({});
    const [error, setError] = useState();

    const handleChange = (event: any) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({ ...values, [name]: value }))
    };

    const isNotVerifyPassword = (pas1: string, pas2: string) => {
        if (pas1 == null) {
            setError('Error! The password cannot is empty');
            return true;
        }
        if (pas1 !== pas2) {
            setError('Error! Passwords not same!');
            return true;
        }
        return false;
    }

    const handleSubmit = async (event: any) => {
        event.preventDefault();
        if (isNotVerifyPassword(inputs.password, inputs.repeat_password)) {
            return
        }
        const response = await fetch("http://127.0.0.1:8000/api/user/register/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inputs)
        });

        const result = await response.json();

        if (!response.ok) {
            setError(result.error);
            return;
        }

        interface Result {
            email: string;
            subject: string;
            message: string;
        }

        const activate_url = `http://127.0.0.1:8000/api/user/activate/?code=${result.activate_code}`

        const data: Result = {
            email: inputs.email,
            subject: 'Please Verify Your Account for Marketplace NFT',
            message: `Please follow the following link to activate your account: <a href='${activate_url}'>${activate_url}</a>`
        }

        const resp = await fetch("/api/contacts", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!resp.ok) {
            setError("Error sending email!");
            return;
        }

        router.push('/success');
    };

    return (
        <div className="mb-auto">
            <h1 className="text-center text-5xl p-10">Sign Up</h1>
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
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="password">Repeat password</label>
                        <input className="border-2 rounded-md border-black p-1" type="password" name="repeat_password" id="repeat_password" onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-center">
                        <button className="border-2 rounded-md border-black p-2 w-64 bg-gray-300 hover:bg-gray-700 hover:text-white" type="Submit">Sign Up</button>
                    </div>
                    <div className="p-5 flex justify-between text-red-500">
                        {error}
                    </div>
                </form>
            </div >
        </div >
    );
}


export default SignUp