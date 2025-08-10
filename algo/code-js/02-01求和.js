// 计算
// 1 + 2 + 3 + ... +n

// for循环写法
function getSumFor(n) {
    let sum = 0
    for (let i=1; i<=n; i++) {
        sum += i
    }
    return sum
}

// while循环写法
function getSumWhile(n) {
    let sum = 0
    let i = 1
    while (i<=n) {
        sum += i
        i ++
    }
    return sum
}

// 递归写法
function getSumRecur(n){
    if (n===1){
        return 1
    } else {
        return getSumRecur(n-1) + n
    }
}


// 调用函数
n = 100
let result = getSumFor(n)
console.log(result) // 5050
let result2 = getSumWhile(n)
console.log(result2) // 5050
let result3 = getSumRecur(n)
console.log(result3) // 5050