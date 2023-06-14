// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "OpenZeppelin/openzeppelin-contracts@4.9.0/contracts/token/ERC721/ERC721.sol";
import "OpenZeppelin/openzeppelin-contracts@4.9.0/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "OpenZeppelin/openzeppelin-contracts@4.9.0/contracts/access/Ownable.sol";
import "OpenZeppelin/openzeppelin-contracts@4.9.0/contracts/utils/Counters.sol";

contract SimpleNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    mapping(address => uint) public balances;

    enum Status {
        ForSale,
        Sold
    }

    struct Art {
        Status status;
        string uri;
        address owner;
        uint price;
        string date_of_creation;
        string title;
    }

    mapping(uint => Art) private arts;

    constructor(
        string memory _name,
        string memory _symbol
    ) ERC721(_name, _symbol) {}

    event ArtCreated(Art art);

    event ArtSold(Art art);

    event ArtResell(Art art);

    event Withdraw(address, uint);

    function sendMoney() public payable {
        balances[msg.sender] += msg.value;
    }

    function createArt(
        string memory _uri,
        address _seller,
        uint _price,
        string memory _date_of_creation,
        string memory _title
    ) public onlyOwner {
        require(_price > 0, "The price cannot be empty");
        require(bytes(_uri).length > 0, "The uri cannot be empty");
        require(
            bytes(_date_of_creation).length > 0,
            "The date cannot be empty"
        );
        require(bytes(_title).length > 0, "The title cannot be empty");

        uint _tokenId = _tokenIdCounter.current();

        _safeMint(msg.sender, _tokenId);
        _setTokenURI(_tokenId, _uri);

        arts[_tokenId] = Art(
            Status.ForSale,
            _uri,
            _seller,
            _price,
            _date_of_creation,
            _title
        );

        _tokenIdCounter.increment();

        emit ArtCreated(arts[_tokenId]);
    }

    function buyArt(
        address _buyer,
        uint _tokenId,
        uint _markup
    ) public onlyOwner {
        require(arts[_tokenId].owner != address(0), "The token is incorrect");
        require(
            arts[_tokenId].status == Status.ForSale,
            "The art is not selling."
        );
        require(arts[_tokenId].owner != _buyer, "The owner cannot be buyer.");
        require(
            balances[_buyer] >= (arts[_tokenId].price + _markup),
            "Insuffience payment."
        );

        payable(arts[_tokenId].owner).transfer(arts[_tokenId].price);

        balances[_buyer] -= arts[_tokenId].price + _markup;

        safeTransferFrom(owner(), _buyer, _tokenId, "");

        emit ArtSold(arts[_tokenId]);
    }

    function _afterTokenTransfer(
        address from,
        address to,
        uint256 firstTokenId,
        uint256 batchSize
    ) internal override {
        arts[firstTokenId].owner = to;
        if (to == owner()) {
            arts[firstTokenId].status = Status.ForSale;
        } else {
            arts[firstTokenId].status = Status.Sold;
        }
    }

    function resellArt(uint _tokenId, uint _price) public onlyOwner {
        require(arts[_tokenId].owner != address(0), "The token is incorrect");

        arts[_tokenId].status = Status.ForSale;
        arts[_tokenId].price = _price;

        emit ArtResell(arts[_tokenId]);
    }

    function getAllArts() public view returns (Art[] memory) {
        uint _tokenId = _tokenIdCounter.current();
        Art[] memory result = new Art[](_tokenId);
        for (uint i = 0; i < _tokenId; i++) {
            result[i] = arts[i];
        }
        return result;
    }

    function getBalances(address _buyer) public view returns (uint) {
        return balances[_buyer];
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    function withdrawAll() public onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    function safeMint(address to, string memory uri) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    // The following functions are overrides required by Solidity.

    function _burn(
        uint256 tokenId
    ) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(
        uint256 tokenId
    ) public view override(ERC721, ERC721URIStorage) returns (string memory) {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(
        bytes4 interfaceId
    ) public view override(ERC721, ERC721URIStorage) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
