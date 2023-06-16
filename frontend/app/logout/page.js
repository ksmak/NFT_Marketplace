'use client'
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function Logout() {
    const router = useRouter();
    const [username, setUsername] = useState(null);

    useEffect(() => {
        setUsername(sessionStorage.getItem('username'));
        sessionStorage.clear();
        setTimeout(router.push('/'), 5000);
    }, []);

    return (
        <>
            <h1 className="text-center text-5xl p-10">Log out</h1>
            <h2 className="text-center text-3xl p-10">User [ {username} ] logged out</h2>
        </>
    );
} 