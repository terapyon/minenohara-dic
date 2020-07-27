import { Result } from "../models"

export default {
    postSearch(data) {
        console.log(data)
        const result = new Result(data, "訳語", "attr", "追加")
        return result;
    },
};