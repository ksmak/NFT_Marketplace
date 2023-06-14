'use client'
import { useState } from "react";

type Props = {
    params: {
        id: string
    }
}

const Profile = ({ params: { id } }) => {
    const [inputs, setInputs] = useState({});
    const [error, setError] = useState();

    const handleChange = (event: any) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({ ...values, [name]: value }))
    };

    const handleSubmit = (event) => {

    };

    return (
        <div className="mb-auto">
            <h1 className="text-center text-5xl p-5">Profile</h1>
            <div className="mr-auto ml-auto border-2 w-3/5 rounded-md bg-gray-100">
                <form onSubmit={handleSubmit}>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="email">Email</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="email" name="email" id="email" disabled />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="surname">Surname</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="text" name="surname" id="surname" onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="name">Name</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="text" name="name" id="name" onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="patronymic">Patronymic</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="text" name="patronymic" id="patronymic" onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="password">Password</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="password" name="password" id="password" onChange={handleChange} />
                    </div>
                    <div className="p-5 flex justify-between">
                        <label className="mr-2" htmlFor="wallet">Wallet</label>
                        <input className="w-3/4 border-2 rounded-md border-black p-1" type="text" name="wallet" id="wallet" onChange={handleChange} />
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

export default Profile;