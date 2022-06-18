// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract AnotherCall {
    uint256 public dataA;
    bytes32 public dataB;

    function setAB(uint256 a, bytes32 b) public {
        dataA = a;
        dataB = b;
    }

    function getBaseA() public view returns (uint256) {
        return dataA;
    }

    function getBaseB() public view returns (bytes32) {
        return dataB;
    }
}
