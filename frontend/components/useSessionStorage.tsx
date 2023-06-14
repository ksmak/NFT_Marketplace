import { useEffect, useState } from "react";

export default function useSessionStorage<T>(key: string, fallbackValue: T) {
    const [value, setValue] = useState(fallbackValue);

    useEffect(() => {
        const stored = sessionStorage.getItem(key);
        setValue(stored ? JSON.parse(stored) : fallbackValue);
    }, [fallbackValue, key]);

    useEffect(() => {
        sessionStorage.setItem(key, JSON.stringify(value));
    }, [key, value]);

    return [value, setValue] as const;
}