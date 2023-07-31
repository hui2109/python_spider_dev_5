// 以下代码运行条件：每次运行，特定的值都是不一样的；如果网站只在第一次加载时运行，其他时候运行是一样的，就需要加在整个js运行的第一行
// hook cookie, 也是hook属性的写法
let v = '';
Object.defineProperty(document, 'cookie', {
    set(val) {
        debugger;
        v = val;
        return v;
    },
    get() {
        return v;
    }
})

// hook headers 必须是ajax请求才能用  --> 网站最下面有 XMLHTTPRequest 的东西, 也是hook方法的写法
let set_headers = window.XMLHttpRequest.prototype.setRequestHeader  // 先把这个方法保存一份
window.XMLHttpRequest.prototype.setRequestHeader = function (name, value) {
    if (name.indexOf('xxx') !== -1) {
        debugger;
    }
    return set_headers(name, value);
}

// hook eval函数
let eval_ = window.eval;
window.eval = function (s) {
    // do something
    debugger;
    // return eval_(s);
    return eval_.apply(this, arguments);
}
