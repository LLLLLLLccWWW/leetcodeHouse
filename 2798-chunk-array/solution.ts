type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    const len = arr.length;
    const chunked = new Array<Obj[]>(Math.ceil(len / size));

    for (let i = 0,idx = 0;i < len;i += size,idx++){
        chunked[idx] = arr.slice(i,i + size);
    }

    return chunked;
};

