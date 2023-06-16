'use client'
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function SignUp() {
    const router = useRouter();

    const [inputs, setInputs] = useState({});
    const [error, setError] = useState(null);

    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({ ...values, [name]: value }))
    };

    const isNotVerify = (inputs) => {
        if (inputs.email === null || inputs.email === '' || inputs.email === undefined) {
            setError("Error! Email cannot be empty.");
            return true
        }
        if (inputs.password === null || inputs.password === '' || inputs.password === undefined) {
            setError("Error! Password cannot be empty.");
            return true;
        }
        if (inputs.password !== inputs.repeat_password) {
            setError("Error! Passwords don't match");
            return true;
        }
        return false;
    }

    const registerUser = async (inputs) => {
        const response = await fetch(`${process.env.FRONTEND_HOST}/api/user/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(inputs)
        });

        const result = await response.json();

        return [response, result];
    }

    const sendMail = async (data) => {
        const response = await fetch(`${process.env.FRONTEND_HOST}/api/contacts`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(data),
        });

        return response.ok;
    }

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (isNotVerify(inputs)) {
            return;
        }

        const [reg_response, reg_result] = await registerUser(inputs);

        if (!reg_response.ok) {
            setError("Error! User is not registered.")
            return;
        }

        const activate_url = `${process.env.FRONTEND_HOST}/activate/${reg_result.result}`

        const data = {
            email: inputs.email,
            subject: `Please Verify Your Account for ${process.env.SITE_NAME}`,
            message: `Please follow the following link to activate your account: <a href='${activate_url}'>${activate_url}</a>`
        }

        const isSendingMail = await sendMail(data);

        if (!isSendingMail) {
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
