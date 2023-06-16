import Link from "next/link";

export default async function Activate({ params }) {
    const result = await activateUser(params.code);

    if (!result) {
        throw new Error();
    }

    return (
        <div className="mb-auto">
            <h1 className="text-center text-5xl p-10">Congratulations!</h1>
            <p className="text-center">User activation was successful</p>
            <div className="text-center p-20">
                <Link href="/signin">
                    <button className="border-2 rounded-md border-black p-2 w-40 bg-gray-300 hover:bg-gray-700 hover:text-white">
                        Sign In
                    </button>
                </Link>
            </div>
        </div>
    )
}

async function activateUser(code) {
    const response = await fetch(`${process.env.FRONTEND_HOST}/api/user/activate/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        body: JSON.stringify({ activate_code: code })
    });

    return response.ok;
}

