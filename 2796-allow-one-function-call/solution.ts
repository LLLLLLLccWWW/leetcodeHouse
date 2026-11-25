type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type OnceFn = (...args: JSONValue[]) => JSONValue | undefined

function once(fn: Function): OnceFn {
    let called = false;
    
    return function (...args) {
        if (!called){
            called = true;
            const result = fn.apply(this,args);
            fn = null as unknown as Function;   // 釋放對原始函式的參照以利 GC
            return result;
        }
        return undefined;
    };
}

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
