var CryptoJS = require("crypto-js");
function Encrypt(word) {
    var tkey = "kingagroot2019ZX";
    var tiv = "kingagroot2019ZX";
    var srcs = CryptoJS.enc.Utf8.parse(word);
    var key = CryptoJS.enc.Utf8.parse(tkey);
    var iv = CryptoJS.enc.Utf8.parse(tiv);
    var encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });

    return encrypted.toString();
}

S = Encrypt(54602011)
console.log(S)