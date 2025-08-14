// 计算斐波拉契数列第n项


function fib(n) {
    if (n === 1 || n === 2) {
        return n - 1
    } else {
        return fib(n-1) + fib(n-2)
    }
}

// 调用函数
let n = 5
console.log(fib(n)) // 3