let JSEncrypt = require('node-jsencrypt');
let MD5 = require('crypto-js/MD5');

function getUuid() {
    var s = [];
    var a = "0123456789abcdef";
    for (var i = 0; i < 32; i++) {
        s[i] = a.substr(Math.floor(Math.random() * 0x10), 1)
    }
    s[14] = "4";
    s[19] = a.substr((s[19] & 0x3) | 0x8, 1);
    s[8] = s[13] = s[18] = s[23];
    var b = s.join("");
    return b
}


function sort_ASCII(a) {
    var b = new Array();
    var c = 0;
    for (var i in a) {
        b[c] = i;
        c++
    }
    var d = b.sort();
    var e = {};
    for (var i in d) {
        e[d[i]] = a[d[i]]
    }
    return e
}

function dataTojson(a) {
    var b = [];
    var c = {};
    b = a.split('&');
    for (var i = 0; i < b.length; i++) {
        if (b[i].indexOf('=') != -1) {
            var d = b[i].split('=');
            if (d.length == 2) {
                c[d[0]] = d[1]
            } else {
                c[d[0]] = ""
            }
        } else {
            c[b[i]] = ''
        }
    }
    return c
}

JSEncrypt.prototype.encryptUnicodeLong = function (string) {
    var k = this.getKey();
    //根据key所能编码的最大长度来定分段长度。key size - 11：11字节随机padding使每次加密结果都不同。
    var maxLength = ((k.n.bitLength() + 7) >> 3) - 11;
    try {
        var subStr = "", encryptedString = "";
        var subStart = 0, subEnd = 0;
        var bitLen = 0, tmpPoint = 0;
        for (var i = 0, len = string.length; i < len; i++) {
            //js 是使用 Unicode 编码的，每个字符所占用的字节数不同
            var charCode = string.charCodeAt(i);
            if (charCode <= 0x007f) {
                bitLen += 1;
            } else if (charCode <= 0x07ff) {
                bitLen += 2;
            } else if (charCode <= 0xffff) {
                bitLen += 3;
            } else {
                bitLen += 4;
            }
            //字节数到达上限，获取子字符串加密并追加到总字符串后。更新下一个字符串起始位置及字节计算。
            if (bitLen > maxLength) {
                subStr = string.substring(subStart, subEnd)
                encryptedString += k.encrypt(subStr);
                subStart = subEnd;
                bitLen = bitLen - tmpPoint;
            } else {
                subEnd = i;
                tmpPoint = bitLen;
            }
        }
        subStr = string.substring(subStart, len)
        encryptedString += k.encrypt(subStr);
        return hex2b64(encryptedString);
    } catch (ex) {
        return false;
    }
};

function hex2b64(h) {
    var b64map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var b64pad = "=";
    var i;
    var c;
    var ret = "";
    for (i = 0; i + 3 <= h.length; i += 3) {
        c = parseInt(h.substring(i, i + 3), 16);
        ret += b64map.charAt(c >> 6) + b64map.charAt(c & 63);
    }
    if (i + 1 == h.length) {
        c = parseInt(h.substring(i, i + 1), 16);
        ret += b64map.charAt(c << 2);
    } else if (i + 2 == h.length) {
        c = parseInt(h.substring(i, i + 2), 16);
        ret += b64map.charAt(c >> 2) + b64map.charAt((c & 3) << 4);
    }
    while ((ret.length & 3) > 0) {
        ret += b64pad;
    }
    return ret;
}


function fn(data) {
    var paramPublicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCvxXa98E1uWXnBzXkS2yHUfnBM6n3PCwLdfIox03T91joBvjtoDqiQ5x3tTOfpHs3LtiqMMEafls6b0YWtgB1dse1W5m+FpeusVkCOkQxB4SZDH6tuerIknnmB/Hsq5wgEkIvO5Pff9biig6AyoAkdWpSek/1/B7zYIepYY0lxKQIDAQAB";
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(paramPublicKey);

    var c = Date.parse(new Date());
    var d = getUuid();
    var e = JSON.stringify(sort_ASCII(dataTojson(data || '{}')));
    var ee = encrypt.encryptUnicodeLong(e);
    var f = MD5(e + d + c).toString();
    // a.setRequestHeader("timestamp", c);
    // a.setRequestHeader('requestId', d);
    // a.setRequestHeader('sign', f)
    return {
        "timestamp": c,
        'requestId': d,
        'post_data': ee,
        'sign': f,
        'original': e
    }
}


if (require.main === module) {
    data = 'page=5&limit=20&taxonid=&startTime=&endTime=&province=%E9%9D%92%E6%B5%B7%E7%9C%81&city=&district=&pointname=&username=&serial_id=&ctime=&taxonname=&state=&mode=0&outside_type=0'
    console.log(fn(data));
}
