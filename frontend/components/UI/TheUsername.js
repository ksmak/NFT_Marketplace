'use client'
import Link from "next/link";
import { useEffect, useState } from "react";

export default function TheUsername() {
    const [userId, setUserId] = useState(null);
    const [username, setUsername] = useState(null);
    const [accessToken, setAccessToken] = useState(null);

    useEffect(() => {
        setUserId(sessionStorage.getItem('id'))
        setUsername(sessionStorage.getItem('username'));
        setAccessToken(sessionStorage.getItem('accessToken'));
    }, [])

    return (
        <div className="text-end mr-3.5 mt-3">
            {username
                ? <div>
                    <span className="mr-2.5 font-bold">{username}</span>
                    <span>
                        <Link className="underline mr-5"
                            href={{
                                pathname: '/profile',
                                query: { id: userId, token: accessToken },
                            }}>open profile</Link>
                    </span>
                    <span>
                        <Link className="underline" href="/logout">log out</Link>
                    </span>
                </div>
                : <strong>Guest</strong>
            }
        </div >
    );
}