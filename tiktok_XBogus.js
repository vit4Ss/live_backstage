md5 = require('md5')
// 更换浏览器会导致canvas_id变化
//let query_token = "msToken=J3RWabcbegNghkCL0YXAo6tXXCKro32Zt-eNG0cSewq1PvY0B_mEMJ9drWNavZDvaFbgmNv2XaL9QM60vyB9CinSBl5Qg35hfoZzhrUXsxuHK4P8Yll-0ILkWRF-9kXpPMT3Rg=="
//let post_body = {"DisplayIDList":["newarnimaiya6","kotemarurun","user4853450601197","itshkvcsgww","yuuuuki_521","bts124jin","hinata._.bochi"]}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
let post_list = '\u0000\u0001\u0000'
//referer = "https://live-backstage.tiktok.com/portal/"
let short_str = "Dkdpgh4ZKsQB80/Mfvw36XI1R25-WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe=";
let canvas = 2179632489

for (var Ib = {}, Jb = "0123456789abcdef".split(""), Kb = [], Lb = [], i = 0; i < 256; i++)
    Kb[i] = Jb[i >> 4 & 15] + Jb[15 & i],
    i < 16 && (i < 10 ? Lb[48 + i] = i : Lb[87 + i] = i);
decode = function (e) {
    for (var t = e.length >> 1, r = t << 1, n = new Uint8Array(t), a = 0, o = 0; o < r;) {
        n[a++] = Lb[e.charCodeAt(o++)] << 4 | Lb[e.charCodeAt(o++)];
    }
    return n
};
encode = function (e) {
    for (var t = e.length, r = "", n = 0; n < t;)
        r += Kb[e[n++]];
    return r
};

ua_s = function (e, t) {
    let u, ib;
    ib = [0];
    for (var r, n = [], a = 0, o = "", i = 0; i < 256; i++)
        n[i] = i;
    for (var s = 0; s < 256; s++)
        a = (a + n[s] + e.charCodeAt(s % e.length)) % 256,
            r = n[s],
            n[s] = n[a],
            n[a] = r;
    u = ib[0],
        a = ib[0];
    for (var l = 0; l < t.length; l++)
        a = (a + n[u = (u + 1) % 256]) % 256,
            r = n[u],
            n[u] = n[a],
            n[a] = r,
            o += String.fromCharCode(255 & (t.charCodeAt(l) ^ n[(n[u] + n[a]) % 256]));
    return o
}

function _0x2f2740(a, c, e, b, d, f, t, n, o, i, r, _, x, u, s, l, v, h, g) {
    let w = new Uint8Array(19);
    return w[0] = a,
        w[1] = r,
        w[2] = c,
        w[3] = _,
        w[4] = e,
        w[5] = x,
        w[6] = b,
        w[7] = u,
        w[8] = d,
        w[9] = s,
        w[10] = f,
        w[11] = l,
        w[12] = t,
        w[13] = v,
        w[14] = n,
        w[15] = h,
        w[16] = o,
        w[17] = g,
        w[18] = i,
        String.fromCharCode.apply(null, w);
}

function _0x2b6720(a, c, e) {
    return String.fromCharCode(a) + String.fromCharCode(c) + e;
}

//获取XBogus
function U8ArrayToXBogus(array1) {
    // 打乱数组顺序
    let array2 = [array1[0], array1[2], array1[4], array1[6], array1[8], array1[10], array1[12], array1[14], array1[16], array1[18], array1[1], array1[3], array1[5], array1[7], array1[9], array1[11], array1[13], array1[15], array1[17]];
    // 再一次打乱顺序，得到19位乱码字符串
    let u1 = _0x2f2740.apply(null, array2);
    // 对乱码字符串重新编码(实际上是异或加密)
    let u2 = ua_s.apply(null, [String.fromCharCode(255), u1]);
    // 在乱码字符串开头添加两个固定字符
    let u = _0x2b6720.apply(null, [2, 255, u2]);
    let XBogus = "";
    // 每次循环生成4个字符，循环7次，每次使用乱码字符串的三个字符
    for (let i = 0; i <= 20; i += 3) {
        let charCodeAtNum0 = u.charCodeAt(i);
        let charCodeAtNum1 = u.charCodeAt(i + 1);
        let charCodeAtNum2 = u.charCodeAt(i + 2);
        let baseNum = charCodeAtNum2 | charCodeAtNum1 << 8 | charCodeAtNum0 << 16;
        let str1 = short_str[(baseNum & 0xfc0000) >> 18];
        let str2 = short_str[(baseNum & 0x3f000) >> 12];
        let str3 = short_str[(baseNum & 0xfc0) >> 6];
        let str4 = short_str[(baseNum & 0x3f) >> 0];
        XBogus += str1 + str2 + str3 + str4;
    }
    return XBogus;
}

//let Bogus = U8ArrayToXBogus(array)
//_signature
rf = function (e, t) {
    for (let r = 0; r < t.length; r++)
        e = 65599 * (e ^ t.charCodeAt(r)) >>> 0;
    return e
}

to_en_post_body = function (e, t) {
    for (var r = 0; r < t.length; r++) {
        var n = t.charCodeAt(r);
        if (n >= 55296 && n <= 56319 && r < t.length) {
            var a = t.charCodeAt(r + 1);
            56320 === (64512 & a) && (n = ((1023 & n) << 10) + (1023 & a) + 65536,
                r += 1)
        }
        e = 65599 * e + n >>> 0
    }
    return e
}


let long_0b_f = function (Time_Xor_0b, ob_head) {
    if (parseInt(Time_Xor_0b, 2) > 0) {
        return ob_head.toString() + ((Time_Xor_0b).padStart(32, '0')).toString()
    }
    if (parseInt(Time_Xor_0b, 2) < 0) {
        let b = ((~parseInt(Time_Xor_0b, 2)).toString(2).padStart(32, '0')).toString()
        let res = ""
        for (let i = 0; i < b.length; i++) {
            res += b.charAt(i) === '0' ? '1' : '0'
        }
        return ob_head.toString() + res
    }
}
let nums = [24, 18, 12, 6, 0]
let to_signature = function (num) {
    let res = ""
    for (let i = 0; i < nums.length; i++) {
        let n = (num >> nums[i]) & 63
        res += to_signature_signa(n)
    }
    return res
}
let to_signature_signa = function (n) {
    if (n < 26) {
        return String.fromCharCode(65 + n)
    }
    if (n >= 26 && n < 52) {
        return String.fromCharCode(71 + n)
    }
    //52<62
    if (n >= 52 && n < 62) {
        return String.fromCharCode(n - 4)
    }
    if (n >= 62) {
        return String.fromCharCode(n - 17)
    }
}
//step3
//canvas_id ^ long_0b_to_num
let step3_num = function (long_0b_to_num) {
    let fl1 = canvas ^ long_0b_to_num
    if (fl1 < 0) {
        return (fl1 >>> 6) ^ -1073741824
    }
    if (fl1 > 0) {
        return (fl1 >>> 6) ^ -1073741824
    }

    //可能有其他情况
}

let get_str6 = function (long_0b_to_num,nn) {
        return (nn<<28) ^ ((288 ^ long_0b_to_num) >>> 4)
}
let get_str2 = function (long_0b_to_num) {
    return ((long_0b_to_num ^ 4294967296) << 28) ^ 515
}
let get_signature = function (url_query, post_body, referer) {
    //let timestamp2 = Math.floor(Date.now() / 1000);
    let timestamp2 = 1722518298
    console.log(timestamp2)
    let ob_head = '10000000110000'
    let rf_time = rf(0, timestamp2.toString())
    let referer_noHead = referer.replace(/^https:\/\//, '');
    let rf_referer = rf(rf_time, referer_noHead)

    let referer_mo = rf_referer % 65521
    let sub = referer_mo * 65521
    let Time_Xor = sub ^ timestamp2
    let Time_Xor_0b = Time_Xor.toString(2)
    let long_0b = long_0b_f(Time_Xor_0b, ob_head)
    let long_0b_to_num = parseInt(long_0b, 2)

    let rf_long_0b_to_num = rf(0, long_0b_to_num.toString())

    let body_hash = to_en_post_body(0, JSON.stringify(post_body))

    url_query = "body_hash=" + body_hash + url_query

    let str1 = to_signature(long_0b_to_num >> 2)
    let str2 = to_signature(get_str2(long_0b_to_num))
    let str3 = to_signature(step3_num(long_0b_to_num))
    let str4 = to_signature_signa((canvas ^ long_0b_to_num) & 63)
    let str5 = to_signature((((rf(rf_long_0b_to_num, UA) % 65521) << 16) ^ (rf(rf_long_0b_to_num, url_query) % 65521)) >> 2)
    let nn = (((rf(rf_long_0b_to_num, UA) % 65521) << 16) ^ (rf(rf_long_0b_to_num, url_query) % 65521))
    let str6 = to_signature(get_str6(long_0b_to_num,nn))
    let str7 = to_signature(referer_mo)
    let signature = "_02B4Z6wo00001" + str1 + str2 + str3 + str4 + str5 + str6 + str7
    let signature_la2 = Number(to_en_post_body(0, signature)).toString(16).substring(6, 8)
    signature += signature_la2
    return signature
}

//url = "https://live-backstage.tiktok.com/creators/live/union_platform_api/agency/union_invite/batch_check_anchor/?msToken=7NyXW9IFwlxA-ZtLZFN1L1qUsABmVfZ5t2tx74Ne5FLBtrRRviNO2KRDVrA72OhwfZ_xrN8z2tLQNcWVMmaO5ejMAVtuGE-M3aDOj2vXnl3iYPaMeJBHD9I7P2ama81___xP"

let get_post_url = function (url, data, referer) {
    let post_body = data
    // 创建一个URL对象
    const urlObj = new URL(url);
    // 使用URLSearchParams对象来获取查询参数
    const searchParams = new URLSearchParams(urlObj.search);

    let msToken = searchParams.get('msToken');
    let query_token = "msToken=" + msToken
    let pathname = urlObj.pathname;

    let XBogus = get_XBogus(query_token, post_body)
    let url_query = "&X-Bogus=" + XBogus + "&" + query_token.replace(/=+$/, '') + "&pathname=" + pathname + "&tt_webid=&uuid="
    let signature = get_signature(url_query, post_body, referer)
    return url + "&X-Bogus=" + XBogus + "&_signature=" + signature
}

let get_XBogus = function (query_token, post_body) {
    let decode_query = decode(md5(decode(md5(query_token))))
    let decode_post_body = decode(md5(decode(md5(JSON.stringify(post_body)))))
    let decode_UA = decode(md5(btoa(ua_s(post_list, UA))))

    //let timestamp = Math.floor(Date.now() / 1000);
    let timestamp = 1722518298
    console.log(timestamp)

    let array = [64, 0.00390625, 1, 0,
        decode_query[14],
        decode_query[15],
        decode_post_body[14],
        decode_post_body[15],
        decode_UA[14],
        decode_UA[15],
        (timestamp >> 24) & 255,
        (timestamp >> 16) & 255,
        (timestamp >> 8) & 255,
        (timestamp >> 0) & 255,
        (canvas >> 24) & 255,
        (canvas >> 16) & 255,
        (canvas >> 8) & 255,
        (canvas >> 0) & 255,
    ]
    array.push(array.reduce(function (a, b) {
        return a ^ b;
    }))
    console.log(array)
    return U8ArrayToXBogus(array)
}
url = "https://live-backstage.tiktok.com/creators/live/union_platform_api/agency/union_invite/batch_check_anchor/?msToken=dgTy-W3woG3K7XA7pt4saRGbmfcVX-98kZIa6Xgm4RdWyR_yCvPq-fGlcKaY3F_YQI4TmE75j3txU6uow2Xu6z__kQbTehs8yQl53OpctqZ_PV4rnqxg1vDaeA_sj2BFwpGXpQ=="
data = {"DisplayIDList":["_j_devil","hothithoa.99","youten517","gotohkikuchi.510","ruukun001","ntk__kurusu","sinsin0523","uta_usagi","nanachan08082","yuyuzaw200","princessyurichama","mmm03101","empty.space98"]}
referer = 'https://live-backstage.tiktok.com/portal/'
console.log(get_post_url(url,data,referer))
//
//
// console.log(-391385990<<28)
// // 42677^1722268062
// console.log(-1610612736 ^ 201377853)