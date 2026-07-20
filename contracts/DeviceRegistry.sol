// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract DeviceRegistry {

    struct Device {
        string deviceID;
        string deviceName;
        address wallet;
        bytes32 credentialHash;
        bool registered;
        bool authenticated;
        bool revoked;
    }

    mapping(string => Device) private devices;

    event DeviceRegistered(
        string deviceID,
        address wallet
    );

    event AuthenticationSuccess(
        string deviceID,
        uint timestamp
    );

    event AuthenticationFailed(
        string deviceID,
        uint timestamp
    );

    event DeviceRevoked(
        string deviceID
    );

    // Register Device
    function registerDevice(
        string memory _deviceID,
        string memory _deviceName,
        bytes32 _credentialHash
    ) public {

        require(
            !devices[_deviceID].registered,
            "Device already registered"
        );

        devices[_deviceID] = Device(
            _deviceID,
            _deviceName,
            msg.sender,
            _credentialHash,
            true,
            false,
            false
        );

        emit DeviceRegistered(
            _deviceID,
            msg.sender
        );
    }

    // Authenticate Device
    function authenticateDevice(
        string memory _deviceID,
        bytes32 _credentialHash
    ) public returns(bool){

        require(
            devices[_deviceID].registered,
            "Device not registered"
        );

        require(
            !devices[_deviceID].revoked,
            "Device revoked"
        );

        if(
            devices[_deviceID].credentialHash == _credentialHash
        ){

            devices[_deviceID].authenticated = true;

            emit AuthenticationSuccess(
                _deviceID,
                block.timestamp
            );

            return true;

        }else{

    devices[_deviceID].authenticated = false;

    emit AuthenticationFailed(
        _deviceID,
        block.timestamp
    );

    return false;
        }
}

    // Get Device Status
    function getDeviceStatus(
        string memory _deviceID
    )
    public
    view
    returns(
        bool registered,
        bool authenticated,
        bool revoked
    ){

        Device memory d = devices[_deviceID];

        return(
            d.registered,
            d.authenticated,
            d.revoked
        );
    }

    // Revoke Device
   function revokeDevice(
    string memory _deviceID
) public {

    require(
        devices[_deviceID].registered,
        "Device not found"
    );

    devices[_deviceID].revoked = true;
    devices[_deviceID].authenticated = false;

    emit DeviceRevoked(
        _deviceID
    );
}

}