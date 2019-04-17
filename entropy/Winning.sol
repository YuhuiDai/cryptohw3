pragma solidity^0.5.7;

contract EtheremonLite {

    function initMonster(string memory _monsterName) public {
    }

    function battle() public returns(uint256){
    }

    function getName(address _monsterAddress) public view returns(string memory) {
    }

    function getNumWins(address _monsterAddress) public view returns(uint) {
    }

    function getNumLosses(address _monsterAddress) public view returns(uint) {
    }

}

contract WinBattle {

    // Placeholder; TODO for Q2
    address monsterAddr = 0xF3259eEC5B4a46748a1F608eC3D74b89058bB3aD;
    EtheremonLite el;

    constructor() public {
        el = EtheremonLite(monsterAddr);
        el.initMonster("yd229");
    }

    function winning() public {
        uint dice = uint(blockhash(block.number - 1));
        dice = dice / 85;
        if (dice % 3 == 0) {
    	    el.battle();
        }
    }
}


