import ProfileForm from "@/components/UI/ProfileForm";

export default async function Profile({ props }) {
    const { id, token } = props;

    if (!id && !token) {
        throw new Error('User profile not found.');
    };

    const response = await fetch(`${process.env.FRONTEND_HOST}/api/user/profile?id=${id}&token=${token}`, {
        method: 'GET'
    });

    const data = await response.json();

    return (
        <>
            <ProfileForm params={{ user: data, token: token, id: id }} />
        </>
    );
}

export async function getServerSideProps(ctx) {
    return {
        props: {
            id: ctx.id,
            token: ctx.token,
        }
    }
}