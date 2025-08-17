// 九九乘法表


function mulTable() {
    let table = ''
    for (let i=1; i<=9; i++){
        for (let j=1; j<=i; j++) {
            table += `${j}*${i}=${j*i}\t`
        }
        table += '\n'
    }
    return table
}

// 调用函数
let table = mulTable()
console.log(table)