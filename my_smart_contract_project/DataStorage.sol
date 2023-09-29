// DataStorage.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataStorage {
    struct Data {
        string name;
        string nationality;
        string contact;
        string image_path;
    }

    mapping(uint256 => Data) public dataMap;
    uint256 public dataCount;

    function addData(
        string memory _name,
        string memory _nationality,
        string memory _contact,
        string memory _image_path
    ) public {
        dataCount++;
        dataMap[dataCount] = Data(_name, _nationality, _contact, _image_path);
    }

    function getData(uint256 _id)
        public
        view
        returns (
            string memory name,
            string memory nationality,
            string memory contact,
            string memory image_path
        )
    {
        Data memory data = dataMap[_id];
        return (data.name, data.nationality, data.contact, data.image_path);
    }
}
