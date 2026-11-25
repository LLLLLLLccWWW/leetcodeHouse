function* fibGenerator(): Generator<number, any, number> {
    let curr = 0;
    let next = 1;

    while(true){
        yield curr;
        const sum = curr + next;
        curr = next;
        next = sum;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
