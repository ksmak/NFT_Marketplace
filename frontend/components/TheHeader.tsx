'use client'
import Link from "next/link";
import TheUsername from "./TheUsername";

const TheHeader = () => {
    return (
        <header className="h-20 bg-black text-white flex flex-row items-center">
            <nav className="grow flex flex-row items-center justify-center">
                <Link className="p-5" href="/">Home</Link>
                <Link className="p-5" href="/signin">Sign In</Link>
                <Link className="p-5" href="/signup">Sign Up</Link>
                <Link className="p-5" href="/about">About</Link>
            </nav>
            <TheUsername />
        </header>
    );
}


export default TheHeader;