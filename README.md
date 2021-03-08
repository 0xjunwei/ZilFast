# ZilFast
A proposed Zilliqa Payment Service

<strong>Motivation</strong>
<br>
As a Zilliqa supporter since early 2020, I noticed that websites that were supporting cryptocurrency as a payment takes a significant amount of time to process.
This includes Zilliqa Official Merchandise site, whereby payment via Zilliqa would require up to 45 minutes to complete. This would result in consumers being reluctant to use cryptocurrency as a form of payment and not utilizing Zilliqa high throughput network.
Privacy is also another aspect where I uphold dearly, studying in Infocomm Security has shown me the number of hacks occuring whereby consumers Personally Identifiable Information is leaked and sold online through various means.
By allowing payment through blockchain the only detail that is available to the merchant is the public address of the buyer. No credit card details are involved.
Riding in the popularity of Stablecoins and XSGD being on the Zilliqa network, merchants would be more willing to take stablecoins as payment as opposed to cryptocurrency with high volatility which may result in merchants loss of profit.

<strong>Goals</strong>
<br>
Create a Payment System based on Zilliqa network for XSGD to be paid to merchants
Allow more types of Stablecoins (e.g. USDT, USDC, BUSD) to be used as a form of payment once the ETH - ZIL bridge is completed
Charge low fees to merchant as opposed to traditional credit card payment fees, which would promote uptake on the service
Privacy, Using Zilswap users could connect their cold wallet and swap their coins into XSGD and make purchases online, once eth - zil bridge has been complete more users could use their tokens for purchases online, therefore details of user would not be available to merchants only public wallet address which is not considered PII as opposed to Credit Card details.

API shall be looped to constantly check for user transaction matching XSGD wallet, Merchant address, and Transaction being successful
<br>
![image](https://user-images.githubusercontent.com/53926665/110338561-1ad13280-8062-11eb-8901-c35d571a720b.png)

In the event that the latest transaction is not XSGD, we would not clear the transaction
<br>
![API Transaction if no XSGD](https://user-images.githubusercontent.com/53926665/110338654-39372e00-8062-11eb-8836-b20dea29ed13.PNG)

