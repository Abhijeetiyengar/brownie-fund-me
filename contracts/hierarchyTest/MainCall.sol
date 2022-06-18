// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

import "./AnotherCall.sol";

contract MainCall {
    AnotherCall public base;

    constructor() public {
        base = new AnotherCall();
    }

    function getBaseAddres() public view returns (address) {
        return address(base);
    }

    function baseGetA() public view returns (uint256) {
        return base.getBaseA();
    }

    function baseGetB() public view returns (bytes32) {
        return base.getBaseB();
    }

    function baseSetAB(uint256 a, bytes32 b) public returns (bool success) {
        base.setAB(a, b);
        return true;
    }
}
