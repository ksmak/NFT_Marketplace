type Props = {
    params: {
        id: string
    }
}

const TokenItem = ({ params: { id } }) => {
    return (
        <div>
            Token {id}
        </div>
    );
}

export default TokenItem;