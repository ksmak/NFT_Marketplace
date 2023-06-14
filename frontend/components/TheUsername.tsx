import Link from "next/link";
import useSessionStorage from "./useSessionStorage";

export default function TheUsername() {
    const [username, setUsername] = useSessionStorage<string>('username', '');

    if (username !== '') {
        return (
            <div className="flex-none p-10">
                <div className="">{username}</div>
                <div>account:{ }</div>
                <Link className="underline mr-5" href={`/profile/${username}`}>open profile</Link>
                <Link className="underline" href="/logout">log out</Link>
            </div>
        )
    } else {
        return (
            <div className="flex-none p-10">Guest</div>
        )
    }
}