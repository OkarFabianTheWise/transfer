const ethers = require("ethers");
const dotenv = require("dotenv");
dotenv.config();

const RpcEndPoint = 'https://data-seed-prebsc-2-s2.binance.org:8545/';

const W3 = new ethers.JsonRpcProvider(RpcEndPoint);
const private_key = process.env.private_key;

function transfer(amount, to) {
  try {
    const wallet = new ethers.Wallet(private_key, W3);
    const tx = {
      to,
      value: ethers.parseEther(amount.toString()),
    };

    wallet.sendTransaction(tx).then((txObj) => {
      console.log("trx hash", txObj.hash)
    })
  } catch (x) {
    console.log("trx err", x)
  }
}

// call the transfer function
//transfer(0.01, 'address you wonna transfer to')
