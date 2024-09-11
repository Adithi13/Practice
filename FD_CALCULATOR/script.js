function calculateMaturityAmount(){
    // get input values from the form elements

    const principle = parseFloat(document.getElementById('principle').value);
    const intrestRate = parseFloat(document.getElementById('intrestRate').value);
    const tenure = parseFloat(document.getElementById('tenure').value);

    //perform calculation
    // const maturityAmount = principle * Math.pow((1 + intrestRate/100), tenure);
    const maturityAmount = principle + (principle * intrestRate * tenure)/100;
    
    // return the result
    // return maturityAmount;
    document.getElementById('result').innerText = 'Maturity Amount: ₹{maturityAmount.toFixed(2)}';
}

//attach the event listener to calulate button
document.getElementById('calculateBtn').addEventListener('click', calculateMaturityAmount);
