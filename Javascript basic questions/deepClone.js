function deepCopy(obj) {
    if (obj instanceof Object) {
        let newObj = {};
        if (Array.isArray(obj)) {
            let arr = [];
            obj.forEach(item => {
                arr.push(deepCopy(item));
            })
            return arr;
        } else {
            for (let key in obj) {
                let value = obj[key];
                if (typeof value == 'function') {
                    newObj[key] = value.bind(newObj);
                } else if (typeof value == 'object') {
                    if (Array.isArray(value)) {
                        newObj[key] = [];
                        value.forEach(item => {
                            newObj[key].push(deepCopy(item));
                        })
                    } else {
                        newObj[key] = deepCopy(value);
                    }
                } else {
                    newObj[key] = value;
                }
            }
        }
        return newObj;
    } else {
        return obj;
    }
}
