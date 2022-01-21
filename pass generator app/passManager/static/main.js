window.addEventListener('DOMContentLoaded', () => {

const characterAmountRange = document.getElementById('characterAmountRange')
const characterAmountNumber = document.getElementById('characterAmountNumber')
const includeUppercaseElement = document.getElementById('includeUppercase')
const includeNumbersElement = document.getElementById('includeNumbers')
const includeSymbolsElement = document.getElementById('includeSymbols')
const form = document.getElementById('passwordGeneratorForm')
const passwordDisplay = document.getElementById('passwordDisplay')

const UPPERCASE_CHAR_CODES = arrayFromLowToHigh(65, 90)
const LOWERCASE_CHAR_CODES = arrayFromLowToHigh(97, 122)
const NUMBER_CHAR_CODES = arrayFromLowToHigh(48, 57)
const SYMBOL_CHAR_CODES = arrayFromLowToHigh(33, 47).concat(
  arrayFromLowToHigh(58, 64)
).concat(
  arrayFromLowToHigh(91, 96)
).concat(
  arrayFromLowToHigh(123, 126)
)

characterAmountNumber.addEventListener('input', syncCharacterAmount,false)
characterAmountRange.addEventListener('input', syncCharacterAmount,false)

form.addEventListener('submit', e => {
  e.stopPropagation();
  e.preventDefault()
  const characterAmount = characterAmountNumber.value
  const includeUppercase = includeUppercaseElement.checked
  const includeNumbers = includeNumbersElement.checked
  const includeSymbols = includeSymbolsElement.checked
  const password = generatePassword(characterAmount, includeUppercase, includeNumbers, includeSymbols)
  passwordDisplay.innerText = password
}, false)

function generatePassword(characterAmount, includeUppercase, includeNumbers, includeSymbols) {
  let charCodes = LOWERCASE_CHAR_CODES
  if (includeUppercase) charCodes = charCodes.concat(UPPERCASE_CHAR_CODES)
  if (includeSymbols) charCodes = charCodes.concat(SYMBOL_CHAR_CODES)
  if (includeNumbers) charCodes = charCodes.concat(NUMBER_CHAR_CODES)

  const passwordCharacters = []
  for (let i = 0; i < characterAmount; i++) {
    const characterCode = charCodes[Math.floor(Math.random() * charCodes.length)]
    passwordCharacters.push(String.fromCharCode(characterCode))
  }
  return passwordCharacters.join('')
}

function arrayFromLowToHigh(low, high) {
  const array = []
  for (let i = low; i <= high; i++) {
    array.push(i)
  }
  return array
}

function syncCharacterAmount(e) {
  e.stopPropagation();
  const value = e.target.value
  characterAmountNumber.value = value
  characterAmountRange.value = value
}
function copy(){
  let inpElem = document.createElement("input");
  inpElem.type = "text";
  let copyText = document.getElementById("passwordDisplay").innerHTML;
  inpElem.value = copyText;
  document.body.appendChild(inpElem);
  inpElem.select();
  document.execCommand('copy');
  document.body.removeChild(inpElem);
  
  document.getElementById("fa-copy").style.backgroundColor = "lightGreen";
  document.getElementById("passwordDisplay").innerHTML = ("<p id='pp'>Copied</p>");
  setTimeout(function(){
      document.getElementById("fa-copy").style.backgroundColor = "rgba(255, 255, 255, 0.08)";
      document.getElementById("pp").innerHTML = (copyText);
  }, 1000);
}

document.getElementById("fa-copy").addEventListener('click', copy);
});

// cm = document.getElementById("CM");
// cm.addEventListener('click', ()=>{
//   alert("clicked");
// }, false)