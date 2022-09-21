let fibonacciSequence = (n) => {
    if(n < 2){
        return n;
    } else if (n === 2){
        return 1;
    }
    return fibonacciSequence(n-1) + fibonacciSequence(n-2);
}

