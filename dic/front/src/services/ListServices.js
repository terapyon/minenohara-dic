import { Candidate } from "../models"

export default {
    getList(word) {
        console.log(word)
        const candidates = [
            new Candidate(word, "init2", "訳"),
            new Candidate("initial", "", ""),
            new Candidate("initialization", "", "initialize")
        ]
        return candidates;
    },
};